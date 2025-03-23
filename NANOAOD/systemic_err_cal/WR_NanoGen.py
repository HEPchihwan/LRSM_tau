#!/usr/bin/env python
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.analyser.ID.GenStatus import *
from PhysicsTools.NanoAODTools.postprocessing.analyser.AnalyserHelper.AnalyserHelper import *
from importlib import import_module
import os
import sys
import ROOT
import argparse
import linecache
ROOT.PyConfig.IgnoreCommandLineOptions = True



class ExampleAnalysis(Module):
	def __init__(self):
		self.writeHistFile = True

	def beginJob(self, histFile=None, histDirName=None):
		Module.beginJob(self, histFile, histDirName)

		oblist = ['pt','eta'] ; binning=0 ; minval=0 ; maxval=0 ; 
		histlist = [] 

		for i in range(0,2) :
			for ob in oblist :
				if ob == 'pt' : 
					binning = 50 ;minval = 0;maxval = 2500
				if ob == 'eta' :
					binning = 24 ; minval = -6.0 ; maxval = 6.0
				for region in ["resolved","merged"] :
					histlist.append(ROOT.TH1F(region+'_Lepton'+str(i)+'_'+ob,region+'_Lepton'+str(i)+'_'+ob,binning,minval,maxval))
					histlist.append(ROOT.TH1F(region+'_Jet'+str(i)+'_'+ob,region+'_Jet'+str(i)+'_'+ob,binning,minval,maxval))
					histlist.append(ROOT.TH1F(region+'_FatJet'+str(i)+'_'+ob,region+'_FatJet'+str(i)+'_'+ob,binning,minval,maxval))


		for hist in histlist :
			self.addObject(hist)

		self.addObject(ROOT.TH1F('dRll','dRll',60,0.,6.))
		self.addObject(ROOT.TH1F('dRJj0','dRJj0',60,0.,6.))
		self.addObject(ROOT.TH1F('dRJj1','dRJj1',60,0.,6.))
		self.addObject(ROOT.TH1F('dRjj','dRjj',60,0.,6.))
		self.addObject(ROOT.TH1F('mjj','mjj',100,0.,1000.))
				
		self.addObject(ROOT.TH1F('Cutflow','Cutflow',6,0,6))
		self.addObject(ROOT.TH1F('nAK4_unclean','nAK4_unclean',10,0,10))
		self.addObject(ROOT.TH1F('nLep','nLep',10,0,10))
		self.addObject(ROOT.TH1F('nTau','nTau',5,0.,5.))
		# FinalStates : 0=th+th 1=te+th 2=tmu+th 3=te+tmu 4=te+te 5=tmu+tmu
		self.addObject(ROOT.TH1F('FinalStates','FinalStates',6,0.,6.))

		self.addObject(ROOT.TH1F('resolved_dRll','resolved_dRll',60,0.,6.))
		self.addObject(ROOT.TH1F('resolved_WR_mass','resolved_WR_mass',1000,0.,5000.))
		self.addObject(ROOT.TH1F('resolved_WR_eta','resolved_WR_eta',24,-6.,6.))
		self.addObject(ROOT.TH1F('resolved_WR_pT','resolved_WR_pT',20,0.,1000.))
		self.addObject(ROOT.TH1F('resolved_N_mass','resolved_N_mass',1000,0.,5000.))
		self.addObject(ROOT.TH1F('resolved_N_eta','resolved_N_eta',120,-6.,6.))
		self.addObject(ROOT.TH1F('resolved_N_pT','resolved_N_pT',60,0.,3000.))
		self.addObject(ROOT.TH1F('resolved_MET','resolved_MET',1000,0.,5000.))
		self.addObject(ROOT.TH1F('resolved_nAK4','resolved_nAK4',10,0,10))
		self.addObject(ROOT.TH1F('resolved_nAK4_taucleaned','resolved_nAK4_taucleaned',10,0,10))
		self.addObject(ROOT.TH1F('resolved_nAK8','resolved_nAK8',10,0,10))

		self.addObject(ROOT.TH1F('merged_dRll','merged_dRll',60,0.,6.))
		self.addObject(ROOT.TH1F('merged_dRJl_primary','merged_dRll',60,0.,6.))
		self.addObject(ROOT.TH1F('merged_dRJl_secondary','merged_dRll',60,0.,6.))
		self.addObject(ROOT.TH1F('merged_WR_mass','merged_WR_mass',1000,0.,5000.))
		self.addObject(ROOT.TH1F('merged_WR_mass_test','merged_WR_mass_test',1000,0.,5000.))
		self.addObject(ROOT.TH1F('merged_WR_eta','merged_WR_eta',24,-6.,6.))
		self.addObject(ROOT.TH1F('merged_WR_pT','merged_WR_pT',20,0.,1000.))
		self.addObject(ROOT.TH1F('merged_N_mass','merged_N_mass',1000,0.,5000.))
		self.addObject(ROOT.TH1F('merged_N_mass_test','merged_N_mass_test',1000,0.,5000.))
		self.addObject(ROOT.TH1F('merged_N_eta','merged_N_eta',120,-6.,6.))
		self.addObject(ROOT.TH1F('merged_N_pT','merged_N_pT',60,0.,3000.))
		self.addObject(ROOT.TH1F('merged_nAK8','merged_nAK8',10,0,10))


	def analyze(self, event):

		isNoCut = False

		rawGenParts = Collection(event,"GenPart")
		rawGenJets = Collection(event, "GenJet")
		rawGenFatJets = Collection(event,"GenJetAK8")
		GenMETv = Object(event, "GenMET")
		GenMETv_LorentzVector = GetGenMETLorentzVector(GenMETv)
		Generator = Object(event,"Generator")	
		w = Generator.weight

		rawGenVisTaus = Collection(event,"GenVisTau")
		rawGenLeptons = [] ; rawGenMuons = [] ; rawGenElectrons = []; rawGenTaus =[]

		for rawGenPart in rawGenParts :
			if rawGenPart.status == 1  : #and fromHardProcess(rawGenPart)
				if abs(rawGenPart.pdgId) == 13 or abs(rawGenPart.pdgId) == 11 : rawGenLeptons.append(rawGenPart)
			else :
				if abs(rawGenPart.pdgId) == 15 : rawGenTaus.append(rawGenPart)	
 
		# Jets
		GenJets = []	
		GenFatJets = [] 

		GenMuons = []
		GenTaus = []		   # All Taus

		for rawGenLepton in rawGenLeptons :
			if abs(rawGenLepton.pdgId) == 13 : rawGenMuons.append(rawGenLepton)
			elif abs(rawGenLepton.pdgId) == 11 : rawGenElectrons.append(rawGenLepton)

		Muons = Select(rawGenMuons,2.4,50.)
		Taus = Select(rawGenVisTaus,2.4,50.)

		GenJets_tmp1 = JetLeptonCleaning(rawGenJets,rawGenMuons,0.1)
		GenJets_tmp2 = JetTauCleaning(GenJets_tmp1,rawGenVisTaus,0.1)
		Jets = Select(GenJets_tmp2,2.4,50) 
		FatJets = Select(rawGenFatJets,2.4,200)

		FinalLeptons = Taus + Muons

		l_obj = [Muons,Taus,Jets,FatJets,FinalLeptons]

		for l in l_obj :
			l.sort(key=lambda x : x.pt , reverse=True)

		self.Cutflow.Fill(0)

		isFinalState = (len(Taus) == 1 and len(Muons) == 1)

		if not isFinalState : return
		self.Cutflow.Fill(1)

		isResolved = False ; isBoosted = False 

		if len(Jets) > 1 :
			dRlj = []
			for lep in FinalLeptons :
				for jet in Jets :
					dRlj.append(deltaR(lep,jet))
			if min(dRlj) > 0.4 : isResolved = True

		if not isResolved :
			if FinalLeptons[0].pt > 63 :
				if deltaR(FinalLeptons[0],FatJets[0]) < 0.8 or deltaR(FinalLeptons[1],FatJets[0]) < 0.8 : isBoosted = True

		print("{},{}".format(isResolved,isBoosted))

		WR = ROOT.TLorentzVector()
		N = ROOT.TLorentzVector()
		
		N_id = [9900016]
		WR_id = [34]

		if isResolved == False and isBoosted == True :
			WR = FinalLeptons[0].p4()+FinalLeptons[1].p4()+FatJets[0].p4()
			secondaryidx = 0; primaryidx = 0
			for i in range(0,2) :
				if HasAncestor(N_id,FinalLeptons[i],rawGenParts) : 
					secondaryidx = i
				elif not HasAncestor(N_id,FinalLeptons[i],rawGenParts) : primaryidx = i
				else : return

			N_test = FatJets[0].p4()
			N = FatJets[0].p4() + FinalLeptons[secondaryidx].p4()
			WR_test = FinalLeptons[primaryidx].p4() + N_test
			self.Cutflow.Fill(2)
			self.merged_nAK8.Fill(len(FatJets))
			self.merged_dRll.Fill(deltaR(FinalLeptons[0],FinalLeptons[1]))
			self.merged_Lepton0_pt.Fill(FinalLeptons[primaryidx].pt)
			self.merged_Lepton1_pt.Fill(FinalLeptons[secondaryidx].pt)
			self.merged_Lepton0_eta.Fill(FinalLeptons[primaryidx].eta)
			self.merged_Lepton1_eta.Fill(FinalLeptons[secondaryidx].eta)
			self.merged_WR_mass.Fill(WR.M())
			self.merged_WR_mass_test.Fill(WR_test.M())
			self.merged_WR_eta.Fill(WR.Eta())
			self.merged_WR_pT.Fill(WR.Pt())
			self.merged_N_mass.Fill(N.M())
			self.merged_N_mass_test.Fill(N_test.M())
			self.merged_N_eta.Fill(N.Eta())
			self.merged_N_pT.Fill(N.Pt()) 
			self.merged_FatJet0_pt.Fill(FatJets[0].pt)
			self.merged_FatJet0_eta.Fill(FatJets[0].eta)
			self.merged_dRJl_primary.Fill(deltaR(FinalLeptons[primaryidx],FatJets[0]))
			self.merged_dRJl_secondary.Fill(deltaR(FinalLeptons[secondaryidx],FatJets[0]))


		elif isResolved == True and isBoosted == False :
			WR = FinalLeptons[0].p4()+FinalLeptons[1].p4()+Jets[0].p4()+Jets[1].p4() 
			debug = 0; secondaryidx = 0; primaryidx = 0
			for i in range(0,2) :
				if HasAncestor(N_id,FinalLeptons[i],rawGenParts) : 
					debug +=1 
					secondaryidx = i
				elif not HasAncestor(N_id,FinalLeptons[i],rawGenParts) : primaryidx = i
			N = FinalLeptons[secondaryidx].p4() + Jets[0].p4()+Jets[1].p4() 

			self.Cutflow.Fill(3)
			self.resolved_nAK4.Fill(len(Jets))
			self.resolved_dRll.Fill(deltaR(FinalLeptons[0],FinalLeptons[1]))
			self.resolved_Lepton0_pt.Fill(FinalLeptons[primaryidx].pt)
			self.resolved_Lepton1_pt.Fill(FinalLeptons[secondaryidx].pt)
			self.resolved_Lepton0_eta.Fill(FinalLeptons[primaryidx].eta)
			self.resolved_Lepton1_eta.Fill(FinalLeptons[secondaryidx].eta)
			self.resolved_WR_mass.Fill(WR.M())
			self.resolved_WR_eta.Fill(WR.Eta())
			self.resolved_WR_pT.Fill(WR.Pt())
			self.resolved_N_mass.Fill(N.M())
			self.resolved_N_eta.Fill(N.Eta())
			self.resolved_N_pT.Fill(N.Pt()) 
			self.resolved_Jet0_pt.Fill(Jets[0].pt)
			self.resolved_Jet1_pt.Fill(Jets[1].pt)
			self.resolved_Jet0_eta.Fill(Jets[0].eta)
			self.resolved_Jet1_eta.Fill(Jets[1].eta)
			self.dRjj.Fill(deltaR(Jets[0],Jets[1]))

		else : return
		self.Cutflow.Fill(4)

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
