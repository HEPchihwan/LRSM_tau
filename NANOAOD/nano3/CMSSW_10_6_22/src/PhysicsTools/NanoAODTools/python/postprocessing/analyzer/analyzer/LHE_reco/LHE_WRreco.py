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
		self.addObject(ROOT.TH1F('WRrecomass','WRrecomass',750,0.,10000.)) #N4
		self.addObject(ROOT.TH1F('Nrecomass','Nrecomass',750,0.,8000.)) #N4


	


	def analyze(self, event):
		
		isNoCut = False

		rawLHEParts = Collection(event,"LHEPart")
		
		
		squark = []; cquark = []; uquark = []; dquark = [];
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
				print("okt")
			# quarks
			
			if abs(rawParts.pdgId) == 1:
				dquark.append(rawParts)
			if abs(rawParts.pdgId) == 2:
				uquark.append(rawParts)
			if abs(rawParts.pdgId) == 3:
				squark.append(rawParts)
			if abs(rawParts.pdgId) == 4:
				cquark.append(rawParts)
				



		## pt sorting
		tau.sort(key=lambda x : x.pt, reverse=True)
		

		uquark.sort(key=lambda x : x.pt, reverse=True)
		dquark.sort(key=lambda x : x.pt, reverse=True)
		squark.sort(key=lambda x : x.pt, reverse=True)
		cquark.sort(key=lambda x : x.pt, reverse=True)
		## N reco 
		
		if len(uquark) !=0 and len(dquark) !=0 and len(tau) >1:
			print ("ok1")
			Np4 = uquark[0].p4() + dquark[0].p4() + tau[1].p4()
			WRp4 = Np4 + tau[0].p4()
			self.Nrecomass.Fill(Np4.M())
			self.WRrecomass.Fill(WRp4.M())
		
		if len(squark) !=0 and len(cquark) !=0 and len(tau) >1:
			print ("ok2")
			Np4 = squark[0].p4() + cquark[0].p4() + tau[1].p4()
			WRp4 = Np4 + tau[0].p4()
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