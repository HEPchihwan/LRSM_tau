#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
#from PhysicsTools.NanoAODTools.postprocessing.analyser.ID.GenStatus import *
#from PhysicsTools.NanoAODTools.postprocessing.analyser.AnalyserHelper.AnalyserHelper import *
from importlib import import_module
import os
import sys
import ROOT
import argparse
import linecache
ROOT.PyConfig.IgnoreCommandLineOptions = True


### file with WR reconstruction with Gen paricle - hadronic scattering process
### It is hard to reconstruct WR with proper tau that which one is leading tau so it is more efficient
### to reconstruct with finding mother particle , which avaliable in Gen particle.

## 참고로 N mass 는 직접적으로 .mass 로 안 나오고 

def Select(inputcoll,etamax,ptmin) :
    output = []
    for obj in inputcoll :
        if abs(obj.eta) < etamax and obj.pt > ptmin : output.append(obj)
    return output 
def FlagIsOn(status,flag_n) :
    if status & (1 << (flag_n -1)) : return True
    else : return False

def isHardProcess(gen) : return FlagIsOn(gen.statusFlags,8)
def Process2(gen) : return FlagIsOn(gen.statusFlags,2)
def Process3(gen) : return FlagIsOn(gen.statusFlags,3)
def Process4(gen) : return FlagIsOn(gen.statusFlags,4)
def Process5(gen) : return FlagIsOn(gen.statusFlags,5)

def get_mother_pdg(genparts, idx):
    """ 특정 입자의 모입자 PDG ID를 찾는 함수 """
    if idx < 0 or idx >= len(genparts["pdgId"]):  # 유효한 인덱스인지 체크
        return None
    mother_idx = genparts["genPartIdxMother"][idx]
    if mother_idx < 0 or mother_idx >= len(genparts["pdgId"]):
        return None
    return genparts["pdgId"][mother_idx]  # 모입자의 PDG ID 반환

class ExampleAnalysis(Module):
	def __init__(self):
		self.writeHistFile = True

	def beginJob(self, histFile=None, histDirName=None):
		Module.beginJob(self, histFile, histDirName)
		#################### reco #################
		# pt
		self.addObject(ROOT.TH1F('not_by_N_tau','not_by_N_tau',400,0.,4000.)) 			# mother is not N
		self.addObject(ROOT.TH1F('by_WR_tau', 'by_WR_tau', 400, 0., 4000.)) 	# mother is WR
		self.addObject(ROOT.TH1F('by_N_tau','by_N_tau',400,0.,4000.)) 				# mother is N
		self.addObject(ROOT.TH1F('quark_parent_tau','quark_parent_tau',400,0.,4000.)) 	# quark parent tau

		self.addObject(ROOT.TH1F('hard_parent_tau_pt', 'tau_pt', 400, 0., 4000.)) 		# tau pt from hard process mother
		self.addObject(ROOT.TH1F('not_hard_parent_tau_pt', 'tau_pt', 400, 0., 4000.)) 	# tau pt from not hard process mother
		
		#mass
		self.addObject(ROOT.TH1F('N_mass','N_mass',750,0.,7500.)) 						# N reco by quark mass
		self.addObject(ROOT.TH1F('not_using_tau_from_N_WR_mass','not_using_tau_from_N_WR_mass',750,0.,7500.)) 			# WR that using tau is not from N
		self.addObject(ROOT.TH1F('using_tau_from_WR_WR_mass','using_tau_from_WR_WR_mass',750,0.,7500.)) 	# WR that using tau is from WR
		self.addObject(ROOT.TH1F('off_shell_secWR_mass','off_shell_secWR_mass',750,0.,7500.)) 				# WR that using tau is from WR
		self.addObject(ROOT.TH1F('offshell_FirstWR_mass','offshell_WR_mass',1500,0.,15000.)) 				# WR that using tau is from WR

		#real mass
		self.addObject(ROOT.TH1F('onshell_WR_mass', 'onshell_WR_mass', 750, 0., 7500.)) 		# all the onshell (first , second)WR mass
		self.addObject(ROOT.TH1F('onshell_hard_WR_mass', 'onshell_hard_WR_mass', 750, 0., 7500.)) 		# all the onshell hard process (first , second)WR mass
		self.addObject(ROOT.TH1F('not_by_N_WR_mass', 'not_by_N_WR_mass', 750, 0., 7500.))		# WR not by N
		self.addObject(ROOT.TH1F('onshell_by_N_WR_mass', 'onshell_by_N_WR_mass', 750, 0., 7500.))				# WR by N
		
		self.addObject(ROOT.TH1F('onshell_WR_mass_notHard', 'onshell_WR_mass_notHard', 750, 0., 7500.)) 				# all not hardprocess WR (not hard)  ## onshell
		self.addObject(ROOT.TH1F('onshell_WR_first_nothard_mass', 'onshell_WR_first_nothard_mass', 750, 0., 7500.)) 	# not hardprocess WR not by N 
		self.addObject(ROOT.TH1F('onshell_WR_second_nothard_mass', 'onshell_WR_second_nothard_mass', 750, 0., 7500.)) 	# not hardprocess WR by N
		

		
	


	def analyze(self, event):
		
		isNoCut = False

		rawGenParts = Collection(event,"GenPart")
		
		
		N =[];WR=[];secWR=[];realfirsttau=[];firsttau=[];sectau=[];t =[]; b=[]; c =[]; s=[]; u=[]; d=[];
		hadN=[];offshellN=[];hadWR=[];nonhadWR=[];quark=[];quark_mother_is_tau_idx=[]; quark_mother_is_tau=[];
		idx_and_id = {};idx_and_id_had={}; tau =[];
		########################################################################
			# WR , N 인덱스 등록
		########################################################################
		for idx, rawGenPartss in enumerate(rawGenParts):
			if abs(rawGenPartss.pdgId) == 9900016:
				N.append(idx)  					# all N index
				if isHardProcess(rawGenPartss): ## hard process N index
					hadN.append(idx)
			if abs(rawGenPartss.pdgId) == 34: 
				WR.append(idx) 					# all WR index
				self.onshell_WR_mass.Fill(rawGenPartss.mass)
				if isHardProcess(rawGenPartss):
					hadWR.append(idx) 			# hard process WR index
				else :
					nonhadWR.append(idx) 		# not hard process WR index
			if abs(rawGenPartss.pdgId) == 1 or abs(rawGenPartss.pdgId) == 2 or abs(rawGenPartss.pdgId) == 3 or abs(rawGenPartss.pdgId) == 4 or abs(rawGenPartss.pdgId) == 5 or abs(rawGenPartss.pdgId) == 6:
				if isHardProcess(rawGenPartss): # hard process quark index
					quark.append(idx) 			# hard process quark index
		
		for idx , rawGenPartss in enumerate(rawGenParts):
			if abs(rawGenPartss.pdgId) == 34:
				if rawGenPartss.genPartIdxMother in N :
					secWR.append(idx)			# WR from N index (sec WR)
					#print( "there is direct secWR")
			if abs(rawGenPartss.pdgId) ==9900016:
				if rawGenPartss.genPartIdxMother not in WR :
					offshellN.append(rawGenPartss)		# N from N index (offshell N)
		########################################################################
			#WR mass finding from hardprocess by N or not by N
		########################################################################
		for rawGenPartss in rawGenParts: 		## WR mass 
			if isHardProcess(rawGenPartss):
				if abs(rawGenPartss.pdgId) == 34: 
					self.onshell_hard_WR_mass.Fill(rawGenPartss.mass) 		#WR mass by hard process
					if rawGenPartss.genPartIdxMother in N :
						self.onshell_by_N_WR_mass.Fill(rawGenPartss.mass) 	## WR second mass by N
						self.off_shell_secWR_mass.Fill(rawGenPartss.mass) ## onshell sec WR mass ...1
					else:
						self.not_by_N_WR_mass.Fill(rawGenPartss.mass)	## WR first mass (not by N)
				
		########################################################################
			# Is WR hard process or not , Is daughter of WR hard process or not
		########################################################################
		
			## 부모가 Hard process인 WR찾기
			if rawGenPartss.genPartIdxMother in hadWR:
				if isHardProcess(rawGenPartss):
					a=1;#print ( "WR (mom) -hard ,  I(", rawGenPartss.pdgId,") -hard")
				else:	
					a=1;#print ( "WR (mom) -hard ,  I(", rawGenPartss.pdgId,") -not hard")
			if rawGenPartss.genPartIdxMother in nonhadWR:
				if isHardProcess(rawGenPartss):
					a=1;#print ( "WR (mom) -not hard ,  I(", rawGenPartss.pdgId, ") -hard")
				else:
					a=1;#print ("WR (mom) -not hard, I(", rawGenPartss.pdgId, ") -not hard")


		########################################################################
			# soft tau  부모 찾기 
		########################################################################
			# 모든 GenParticle의 인덱스와 PDG ID를 매핑
		
		for idx, rawGenPartssss in enumerate(rawGenParts):
			idx_and_id[idx] = rawGenPartssss.pdgId  # 모든 입자 인덱스와 PDG ID
			if isHardProcess(rawGenPartssss):
				idx_and_id_had[idx]=rawGenPartssss.pdgId # hard process 입자 인덱스와 PDG ID
			
		for idx, rawGenPartsss in enumerate(rawGenParts):
			if abs(rawGenPartsss.pdgId) == 15: #and rawGenPartsss.pt < 1000: 									# pt가 1000이하인 tau
					mother_index = rawGenPartsss.genPartIdxMother  											# tau mother 인덱스 가져오기
					if mother_index not in idx_and_id_had and mother_index not in N: 						# mother 가 hadronic particle 이 아닌 경우
						a=1;#print("mother is not hadronic particle , mother pdg id is", idx_and_id[mother_index])
					if mother_index in idx_and_id_had and mother_index not in N: 							#mother 가 hadronic particle 인 경우
						a=1;#print("mother is hadronic particle, mother pdg id is", idx_and_id[mother_index])
					if (mother_index not in (hadWR or hadN) ) and (mother_index in (WR or N)) :
						a=1;#print("mother of tau is not both hadronic WR and N , mother is,", idx_and_id[mother_index]) 
					if (mother_index in (hadWR or hadN) ) and (mother_index not in (WR or N)) :
						a=1;#print("mother of tau is both hadronic WR and N , mother is,", idx_and_id[mother_index])
					if mother_index in hadWR:
						self.hard_parent_tau_pt.Fill(rawGenPartsss.pt)
					if mother_index in WR and mother_index not in hadWR:
						self.not_hard_parent_tau_pt.Fill(rawGenPartsss.pt) 
					if mother_index in quark:
						quark_mother_is_tau_idx = idx_and_id[mother_index]		
						quark_mother_is_tau.append(rawGenPartsss)							# tau의 엄마 quark인덱스 찾기
		for idx, rawGenPartsss in enumerate(rawGenParts):												# tau의 엄마 quark의 엄마 찾기 
			if idx == quark_mother_is_tau_idx:
				print()
				#if rawGenPartsss.genPartIdxMother is not None:
				#	print("tau의 엄마인 쿼크의 엄마는 ", idx_and_id[rawGenPartsss.genPartIdxMother] )
					
				
			########################################################################
			#reco
			########################################################################
		for rawGenPartss in rawGenParts:
			if isHardProcess(rawGenPartss):
				if abs(rawGenPartss.pdgId) == 15:						## tau	
					tau.append(rawGenPartss)
					if rawGenPartss.genPartIdxMother in N : 				# tau from N
						sectau.append(rawGenPartss)
						self.by_N_tau.Fill(rawGenPartss.pt)
					else:
						firsttau.append(rawGenPartss) 					# tau not from N (first tau)
						self.not_by_N_tau.Fill(rawGenPartss.pt)
					if rawGenPartss.genPartIdxMother in WR :
						realfirsttau.append(rawGenPartss) 				# tau from WR (realfirsttau)
						self.by_WR_tau.Fill(rawGenPartss.pt)
					if 	rawGenPartss.genPartIdxMother in quark:
						self.quark_parent_tau.Fill(rawGenPartss.pt)      #tau from quark ( if WR is offshell first tau)
			
																		## quark

				if len(secWR)>0 and rawGenPartss.genPartIdxMother in secWR : # quark from sec WR ( on shell WR)
					if abs(rawGenPartss.pdgId) == 1:
						d.append(rawGenPartss)
						#print( "there is on shell WR quark")
					if abs(rawGenPartss.pdgId) == 2:
						u.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 3:
						s.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 4:
						c.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 5:
						b.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 6:
						t.append(rawGenPartss)
				
				if len(N)>0 and rawGenPartss.genPartIdxMother in N:      	# quark from N ( off shell WR)
					if abs(rawGenPartss.pdgId) == 1:
						d.append(rawGenPartss)
						#print( "there is off shell WR quark")
					if abs(rawGenPartss.pdgId) == 2:
						u.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 3:
						s.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 4:
						c.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 5:
						b.append(rawGenPartss)
					if abs(rawGenPartss.pdgId) == 6:
						t.append(rawGenPartss)
			
																			## N and WR reco					
			
																			# tau 중에 N에서 오지 않은 tau를 첫번째 tau로 사용 
				if (len(firsttau)>0 and len(sectau)>0):						# on off shell first WR 
					if ( len(t) > 0 and len(b) >0):
						secWRp4 = t[0].p4() + b[0].p4()							## offshell sec WR mass ...2
						self.off_shell_secWR_mass.Fill(secWRp4.M())			# on shell off shell 모두 포함한 WR mass (쿼크만으로 구성시 on offshell 포함해서 나와야함 )
						Np4  = sectau[0].p4() + t[0].p4() + b[0].p4() 
						WRp4 = firsttau[0].p4() + Np4
						self.not_using_tau_from_N_WR_mass.Fill(WRp4.M())						# on shell off shell 모두 포함한 WR mass (쿼크만으로 구성시 on offshell 포함해서 나와야함 ) 
						self.N_mass.Fill(Np4.M())
						


					if ( len(s) > 0 and len(c) >0):
						secWRp4 = s[0].p4() + c[0].p4()
						self.off_shell_secWR_mass.Fill(secWRp4.M())
						Np4  = sectau[0].p4() + s[0].p4() + c[0].p4() 
						WRp4 = firsttau[0].p4() + Np4
						self.not_using_tau_from_N_WR_mass.Fill(WRp4.M())
						self.N_mass.Fill(Np4.M())
						

					if ( len(u) > 0 and len(d) >0):
						secWRp4 = u[0].p4() + d[0].p4()
						self.off_shell_secWR_mass.Fill(secWRp4.M())
						Np4  = sectau[0].p4() + u[0].p4() + d[0].p4()
						WRp4 = firsttau[0].p4() + Np4
						self.not_using_tau_from_N_WR_mass.Fill(WRp4.M())
						self.N_mass.Fill(Np4.M())
						
					
																			## tau 중에 WR에서 직접 온 tau ( off shell WR로 부터 온 tau는 포함되지 않음 )
				if (len(realfirsttau)>0 and len(sectau)>0):						# onshell first WR 
					if ( len(t) > 0 and len(b) >0):
						Np4  = sectau[0].p4() + t[0].p4() + b[0].p4() 
						WRp4 = realfirsttau[0].p4() + Np4
						self.using_tau_from_WR_WR_mass.Fill(WRp4.M())
						self.N_mass.Fill(Np4.M())
					if ( len(s) > 0 and len(c) >0):
						Np4  = sectau[0].p4() + s[0].p4() + c[0].p4() 
						WRp4 = realfirsttau[0].p4() + Np4
						self.using_tau_from_WR_WR_mass.Fill(WRp4.M())
						self.N_mass.Fill(Np4.M())
					if ( len(u) > 0 and len(d) >0):
						Np4  = sectau[0].p4() + u[0].p4() + d[0].p4()
						WRp4 = realfirsttau[0].p4() + Np4
						self.using_tau_from_WR_WR_mass.Fill(WRp4.M())
						self.N_mass.Fill(Np4.M())
					#print("number of tau is",len(tau))
				
				if (len(sectau)) > 0 and len(quark_mother_is_tau)>0 and len(offshellN)>0: ## offshell first WR
					print("ok1")
					if  ( len(t) > 0 and len(b) >0):
						Np4  = sectau[0].p4() + t[0].p4() + b[0].p4()
						WRp4 = quark_mother_is_tau[0].p4() + Np4
						self.offshell_FirstWR_mass.Fill(WRp4.M())
					if  ( len(s) > 0 and len(c) >0):
						Np4  = sectau[0].p4() + s[0].p4() + c[0].p4()
						WRp4 = quark_mother_is_tau[0].p4() + Np4
						self.offshell_FirstWR_mass.Fill(WRp4.M())
					if  ( len(u) > 0 and len(d) >0):
						print("ok2")
						Np4  = sectau[0].p4() + u[0].p4() + d[0].p4()
						WRp4 = quark_mother_is_tau[0].p4() + Np4
						self.offshell_FirstWR_mass.Fill(WRp4.M())
						

				
			else: 															# hard process 가 아닌 경우
				if abs(rawGenPartss.pdgId) == 34: 							# Hard process 가 아닌 WR mass
					self.onshell_WR_mass_notHard.Fill(rawGenPartss.mass)
					if rawGenPartss.genPartIdxMother in N :
						self.onshell_WR_second_nothard_mass.Fill(rawGenPartss.mass)
					else:
						self.onshell_WR_first_nothard_mass.Fill(rawGenPartss.mass)

		


		return True



parser = argparse.ArgumentParser(description='WRTau NanoGen')
parser.add_argument('-d', dest='directory',default="")
parser.add_argument('-f', dest='singlefile',default="")
parser.add_argument('-o', dest='output',default="histOut.root")
args = parser.parse_args()

directory = "" ; outputname = "" ; preselection = "" ; singlefile = ""

if args.directory == "" and args.singlefile == "" :
	print("Directory(-d) or file(-f) should be given")
	quit()

outputname = args.output
files=[]

if args.directory != "" and args.singlefile == "" :
	directory = args.directory
	for filename in os.listdir(directory) :
		if filename.endswith(".root") :
			files.append(os.path.join(directory, filename))
			print(os.path.join(directory,filename))
		else : continue

if args.directory == "" and args.singlefile != "" :
	singlefile = args.singlefile	
	files.append(singlefile)

p = PostProcessor(".", files, cut=preselection, branchsel=None, modules=[
	ExampleAnalysis()], noOut=True, histFileName=outputname, histDirName="plots")
p.run()	