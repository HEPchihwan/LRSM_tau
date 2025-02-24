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


def Select(inputcoll,etamax,ptmin) :
    output = []
    for obj in inputcoll :
        if abs(obj.eta) < etamax and obj.pt > ptmin : output.append(obj)
    return output 




class ExampleAnalysis(Module):
	def __init__(self):
		self.writeHistFile = True

	def beginJob(self, histFile=None, histDirName=None):
		Module.beginJob(self, histFile, histDirName)


		#mass
		self.addObject(ROOT.TH1F('WRrecomass','WRrecomass',750,0.,10000.)) #WR
		self.addObject(ROOT.TH1F('Nrecomass','Nrecomass',750,0.,8000.)) #N
		self.addObject(ROOT.TH1F('Nup200_secWRrecomass','Nup200_secWRrecomass',750,0.,10000.)) #qq, N>200
		self.addObject(ROOT.TH1F('Ndown200_secWRrecomass','Ndown200_secWRrecomass',750,0.,10000.))#qq N<200
		self.addObject(ROOT.TH1F('Ndown200_sectaumass','Ndown200_sectaumass',750,0.,20.))#qq N<200

		## N over 200
		# pt
		self.addObject(ROOT.TH1F('Nup200_quarks_pt','Nup200_quarks_pt',100,0.,1000.)) #qq, N>200
		self.addObject(ROOT.TH1F('Nup200_leading_tau_pt','Nup200_leading_tau_pt',100,0.,5000.))
		self.addObject(ROOT.TH1F('Nup200_subleading_tau_pt','Nup200_subleading_tau_pt',100,0.,5000.))
		#eta
		self.addObject(ROOT.TH1F('Nup200_quarks_eta','Nup200_quarks_eta',100,-6.,6.)) #qq, N>200
		self.addObject(ROOT.TH1F('Nup200_leading_tau_eta','Nup200_leading_tau_eta',100,-6.,6.))
		self.addObject(ROOT.TH1F('Nup200_subleading_tau_eta','Nup200_subleading_tau_eta',100,-6.,6.))
		
		
		## N down 200
		#pt
		self.addObject(ROOT.TH1F('Ndown200_quarks_pt','Ndown200_quarks_pt',100,0.,1000.)) #qq, N>200
		self.addObject(ROOT.TH1F('Ndown200_leading_tau_pt','Ndown200_leading_tau_pt',100,0.,5000.))
		self.addObject(ROOT.TH1F('Ndown200_subleading_tau_pt','Ndown200_subleading_tau_pt',100,0.,5000.))
		#eta
		self.addObject(ROOT.TH1F('Ndown200_quarks_eta','Ndown200_quarks_eta',100,-6.,6.)) #qq, N>200
		self.addObject(ROOT.TH1F('Ndown200_leading_tau_eta','Ndown200_leading_tau_eta',100,-6.,6.))
		self.addObject(ROOT.TH1F('Ndown200_subleading_tau_eta','Ndown200_subleading_tau_eta',100,-6.,6.))
		


	def analyze(self, event):
		
		isNoCut = False

		rawLHEParts = Collection(event,"LHEPart")
		
		
		squark = []; cquark = []; uquark = []; dquark = []; bquark = []; tquark = [];
		tau=[];
		Np4 =[];
		
		
				
		
		#------------#------------#------------#------------#------------#------------
		#------------#------------#------------#------------#------------#------------
		## reco particle 
		#------------#------------#------------#------------#------------#------------
		#------------#------------#------------#------------#------------#------------


		for rawParts in rawLHEParts:
			# leptons
			if abs(rawParts.pdgId) == 15:
				tau.append(rawParts)
				
				
			# quarks
			
			if abs(rawParts.pdgId) == 1:
				if rawParts.status == 1:
					dquark.append(rawParts)
			if abs(rawParts.pdgId) == 2:
				if rawParts.status == 1:
					uquark.append(rawParts)
			if abs(rawParts.pdgId) == 3:
				if rawParts.status == 1:
					squark.append(rawParts)
			if abs(rawParts.pdgId) == 4:
				if rawParts.status == 1:
					cquark.append(rawParts)
			if abs(rawParts.pdgId) == 5:
				if rawParts.status == 1:
					bquark.append(rawParts)
			if abs(rawParts.pdgId) == 6:
				if rawParts.status == 1:
					tquark.append(rawParts)
								



		## pt sorting
		tau.sort(key=lambda x : x.pt, reverse=True)
		

		uquark.sort(key=lambda x : x.pt, reverse=True)
		dquark.sort(key=lambda x : x.pt, reverse=True)
		squark.sort(key=lambda x : x.pt, reverse=True)
		cquark.sort(key=lambda x : x.pt, reverse=True)
		bquark.sort(key=lambda x : x.pt, reverse=True)
		tquark.sort(key=lambda x : x.pt, reverse=True)
		## N reco 
		
		if len(uquark) !=0 and len(dquark) !=0 and len(tau) >1:	
			Np4 = uquark[0].p4() + dquark[0].p4() + tau[1].p4()
			WRp4 = Np4 + tau[0].p4()
			sectaup4 = tau[1].p4()
			## case of N over 200 and below 200
			if Np4.M() > 200:
				#mass
				secWR = uquark[0].p4() + dquark[0].p4() 
				self.Nup200_secWRrecomass.Fill(secWR.M())
				#print ("taumass for N over 200 ud",tau[0].p4().M())
				#pt
				self.Nup200_quarks_pt.Fill(uquark[0].pt)
				self.Nup200_quarks_pt.Fill(dquark[0].pt)
				self.Nup200_leading_tau_pt.Fill(tau[0].pt)
				self.Nup200_subleading_tau_pt.Fill(tau[1].pt)
				#eta
				self.Nup200_quarks_eta.Fill(uquark[0].eta)
				self.Nup200_quarks_eta.Fill(dquark[0].eta)
				self.Nup200_leading_tau_eta.Fill(tau[0].eta)
				self.Nup200_subleading_tau_eta.Fill(tau[1].eta)
			else:
				#mass
				secWR = uquark[0].p4() + dquark[0].p4()
				self.Ndown200_secWRrecomass.Fill(secWR.M())
				self.Ndown200_sectaumass.Fill(sectaup4.M())
				#print ("taumass for N low 200 ud",tau[0].p4().M())
				#pt
				self.Ndown200_quarks_pt.Fill(uquark[0].pt)
				self.Ndown200_quarks_pt.Fill(dquark[0].pt)
				self.Ndown200_leading_tau_pt.Fill(tau[0].pt)
				self.Ndown200_subleading_tau_pt.Fill(tau[1].pt)
				#eta
				self.Ndown200_quarks_eta.Fill(uquark[0].eta)
				self.Ndown200_quarks_eta.Fill(dquark[0].eta)
				self.Ndown200_leading_tau_eta.Fill(tau[0].eta)
				self.Ndown200_subleading_tau_eta.Fill(tau[1].eta)
			self.Nrecomass.Fill(Np4.M())
			self.WRrecomass.Fill(WRp4.M())
		
		if len(squark) !=0 and len(cquark) !=0 and len(tau) >1:
			Np4 = squark[0].p4() + cquark[0].p4() + tau[1].p4()
			WRp4 = Np4 + tau[0].p4()
			sectaup4 = tau[1].p4()
			if Np4.M() > 200:
				#mass
				secWR = squark[0].p4() + cquark[0].p4() 
				self.Nup200_secWRrecomass.Fill(secWR.M())
				#print ("taumass for N over 200 sc",tau[0].p4().M())
				#pt
				self.Nup200_quarks_pt.Fill(cquark[0].pt)
				self.Nup200_quarks_pt.Fill(squark[0].pt)
				self.Nup200_leading_tau_pt.Fill(tau[0].pt)
				self.Nup200_subleading_tau_pt.Fill(tau[1].pt)
				#eta
				self.Nup200_quarks_eta.Fill(cquark[0].eta)
				self.Nup200_quarks_eta.Fill(squark[0].eta)
				self.Nup200_leading_tau_eta.Fill(tau[0].eta)
				self.Nup200_subleading_tau_eta.Fill(tau[1].eta)
			else:
				#mass
				secWR = cquark[0].p4() + squark[0].p4()
				self.Ndown200_secWRrecomass.Fill(secWR.M())
				self.Ndown200_sectaumass.Fill(sectaup4.M())
				#print ("taumass for N below 200 sc",tau[0].p4().M())
				#pt
				self.Ndown200_quarks_pt.Fill(cquark[0].pt)
				self.Ndown200_quarks_pt.Fill(squark[0].pt)
				self.Ndown200_leading_tau_pt.Fill(tau[0].pt)
				self.Ndown200_subleading_tau_pt.Fill(tau[1].pt)
				#eta
				self.Ndown200_quarks_eta.Fill(cquark[0].eta)
				self.Ndown200_quarks_eta.Fill(squark[0].eta)
				self.Ndown200_leading_tau_eta.Fill(tau[0].eta)
				self.Ndown200_subleading_tau_eta.Fill(tau[1].eta)
			self.Nrecomass.Fill(Np4.M())
			self.WRrecomass.Fill(WRp4.M())
		
		if len(bquark) !=0 and len(tquark) !=0 and len(tau) >1:
			print ("tbquark has", len(bquark))
			Np4 = bquark[0].p4() + tquark[0].p4() + tau[1].p4()
			WRp4 = Np4 + tau[0].p4()
			sectaup4 = tau[1].p4()
			if Np4.M() > 200:
				#mass
				secWR = bquark[0].p4() + tquark[0].p4()
				self.Nup200_secWRrecomass.Fill(secWR.M())
				#print ("taumass for N over 200 bd", tau[0].p4().M())
				#pt
				self.Nup200_quarks_pt.Fill(bquark[0].pt)
				self.Nup200_quarks_pt.Fill(tquark[0].pt)
				self.Nup200_leading_tau_pt.Fill(tau[0].pt)
				self.Nup200_subleading_tau_pt.Fill(tau[1].pt)
				#eta
				self.Nup200_quarks_eta.Fill(bquark[0].eta)
				self.Nup200_quarks_eta.Fill(tquark[0].eta)
				self.Nup200_leading_tau_eta.Fill(tau[0].eta)
				self.Nup200_subleading_tau_eta.Fill(tau[1].eta)

			else:
				#mass
				secWR = bquark[0].p4() + tquark[0].p4()
				self.Ndown200_secWRrecomass.Fill(secWR.M())
				self.Ndown200_sectaumass.Fill(sectaup4.M())
				#print ("taumass for N below 200 bd", tau[0].p4().M())
				#pt
				self.Ndown200_quarks_pt.Fill(bquark[0].pt)
				self.Ndown200_quarks_pt.Fill(tquark[0].pt)
				self.Ndown200_leading_tau_pt.Fill(tau[0].pt)
				self.Ndown200_subleading_tau_pt.Fill(tau[1].pt)
				#eta
				self.Ndown200_quarks_eta.Fill(bquark[0].eta)
				self.Ndown200_quarks_eta.Fill(tquark[0].eta)
				self.Ndown200_leading_tau_eta.Fill(tau[0].eta)
				self.Ndown200_subleading_tau_eta.Fill(tau[1].eta)

			self.Nrecomass.Fill(Np4.M())
			self.WRrecomass.Fill(WRp4.M())

		

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