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

class ExampleAnalysis(Module):
	def __init__(self):
		self.writeHistFile = True

	def beginJob(self, histFile=None, histDirName=None):
		Module.beginJob(self, histFile, histDirName)
		#################### reco #################
		# pt
		self.addObject(ROOT.TH1F('first_tau','first_tau',400,0.,4000.))
		self.addObject(ROOT.TH1F('real_first_tau', 'real_first_tau', 400, 0., 4000.))
		self.addObject(ROOT.TH1F('second_tau','second_tau',400,0.,4000.))
		
		#mass
		self.addObject(ROOT.TH1F('N_mass','N_mass',750,0.,7500.)) #N
		self.addObject(ROOT.TH1F('tau_WR_mass','tau_WR_mass',750,0.,7500.)) # WR
		self.addObject(ROOT.TH1F('real1tau_WR_mass','real1tau_WR_mass',750,0.,7500.)) # WR

		#real mass
		self.addObject(ROOT.TH1F('WR_mass_real', 'WR_mass_real', 750, 0., 7500.)) # WR
		self.addObject(ROOT.TH1F('WR_mass_Hard', 'WR_mass_Hard', 750, 0., 7500.)) # WR
		

		
	


	def analyze(self, event):
		
		isNoCut = False

		rawGenParts = Collection(event,"GenPart")
		
		
		N =[];WR=[];realfirsttau=[];firsttau=[];sectau=[];t =[]; b=[]; c =[]; s=[]; u=[]; d=[];
		for idx, rawGenPartss in enumerate(rawGenParts):
			
			if abs(rawGenPartss.pdgId) == 9900016:
				N.append(idx)  # 객체 대신 인덱스를 저장
			if abs(rawGenPartss.pdgId) == 34:
				WR.append(idx)
				self.WR_mass_real.Fill(rawGenPartss.mass)
		
	
		for rawGenParts in rawGenParts:
			##  hard process ( LHE 만  사용 )
			if not isHardProcess(rawGenParts):
				continue
			if abs(rawGenParts.pdgId) == 34:
				self.WR_mass_Hard.Fill(rawGenParts.mass)
			if abs(rawGenParts.pdgId) == 15:
				if rawGenParts.genPartIdxMother in N : # tau from N
					sectau.append(rawGenParts)
					self.second_tau.Fill(rawGenParts.pt)
				else:
					firsttau.append(rawGenParts)
					self.first_tau.Fill(rawGenParts.pt)
				if rawGenParts.genPartIdxMother in WR :
					realfirsttau.append(rawGenParts)
					self.real_first_tau.Fill(rawGenParts.pt)
			if rawGenParts.genPartIdxMother in N : # quark from N
				if abs(rawGenParts.pdgId) == 1:
					d.append(rawGenParts)
					
				if abs(rawGenParts.pdgId) == 2:
					u.append(rawGenParts)
					
				if abs(rawGenParts.pdgId) == 3:
					s.append(rawGenParts)
					
				if abs(rawGenParts.pdgId) == 4:
					c.append(rawGenParts)
					
				if abs(rawGenParts.pdgId) == 5:
					b.append(rawGenParts)
				if abs(rawGenParts.pdgId) == 6:
					t.append(rawGenParts)
			## pt sorting -> no needed
			
			# tau 중에 N에서 오지 않은 tau
			if (len(firsttau)>0 and len(sectau)>0):
				if ( len(t) > 0 and len(b) >0):
					Np4  = sectau[0].p4() + t[0].p4() + b[0].p4() 
					WRp4 = firsttau[0].p4() + Np4
					self.tau_WR_mass.Fill(WRp4.M())
					self.N_mass.Fill(Np4.M())
				if ( len(s) > 0 and len(c) >0):
					Np4  = sectau[0].p4() + s[0].p4() + c[0].p4() 
					WRp4 = firsttau[0].p4() + Np4
					self.tau_WR_mass.Fill(WRp4.M())
					self.N_mass.Fill(Np4.M())
				if ( len(u) > 0 and len(d) >0):
					
					Np4  = sectau[0].p4() + u[0].p4() + d[0].p4()
					WRp4 = firsttau[0].p4() + Np4
					self.tau_WR_mass.Fill(WRp4.M())
					self.N_mass.Fill(Np4.M())
			
			
			## tau 중에 WR에서 직접 온 tau
			if (len(realfirsttau)>0 and len(sectau)>0):
				if ( len(t) > 0 and len(b) >0):
					Np4  = sectau[0].p4() + t[0].p4() + b[0].p4() 
					WRp4 = realfirsttau[0].p4() + Np4
					self.real1tau_WR_mass.Fill(WRp4.M())
					self.N_mass.Fill(Np4.M())
				if ( len(s) > 0 and len(c) >0):
					Np4  = sectau[0].p4() + s[0].p4() + c[0].p4() 
					WRp4 = realfirsttau[0].p4() + Np4
					self.real1tau_WR_mass.Fill(WRp4.M())
					self.N_mass.Fill(Np4.M())
				if ( len(u) > 0 and len(d) >0):
					
					Np4  = sectau[0].p4() + u[0].p4() + d[0].p4()
					WRp4 = realfirsttau[0].p4() + Np4
					self.real1tau_WR_mass.Fill(WRp4.M())
					self.N_mass.Fill(Np4.M())
	

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