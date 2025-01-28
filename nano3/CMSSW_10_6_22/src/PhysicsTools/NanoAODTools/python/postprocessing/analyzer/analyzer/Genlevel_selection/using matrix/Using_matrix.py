#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from PhysicsTools.NanoAODTools.postprocessing.tools import *
#from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
#from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
#from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
#from PhysicsTools.NanoAODTools.postprocessing.analyser.ID.GenStatus import *
#from PhysicsTools.NanoAODTools.postprocessing.analyser.AnalyserHelper.AnalyserHelper import *
from importlib import import_module
import os
import sys
import ROOT
import argparse
import linecache
import uproot
import vector
import math
import numpy as np
import matplotlib.pyplot as plt
import awkward as ak
ROOT.PyConfig.IgnoreCommandLineOptions = True


## x 방향이 이벤트 y 방향이 각 입자의 정보 z 방향이 입자들 각각이라 생각하면 될듯?


sample = "/gv0/Users/youngwan_public/WRTauNano/WRtoNTautoTauTauJJ_WR1000_N100_TuneCP5_13TeV_madgraph-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2530000/205533A0-7DCC-B343-9A7D-969B87888C4C.root"
file = uproot.open(sample)
events = file["Events"]
print(len(events))
keys = events.keys()
#print(ak.to_list(file))

## Gen particle information 

GenPart_pdgId = events["GenPart_pdgId"].array()
GenPart_pt = events["GenPart_pt"].array()
GenPart_eta = events["GenPart_eta"].array()
GenPart_mass = events["GenPart_mass"].array()
GenPart_mother_idx  = events["GenPart_genPartIdxMother"].array()
#print(ak.to_list(GenPart_pdgId))
#print(ak.to_list(GenPart_mother_idx))
mask_electrons_muons = ( GenPart_pdgId == abs(11) ) | (GenPart_pdgId == abs(13) )
lepton_pt = GenPart_pt[mask_electrons_muons]
lepton_eta = GenPart_eta[mask_electrons_muons]
lepton_pts = ak.flatten(lepton_pt)
lepton_etas = ak.flatten(lepton_eta)
plt.hist2d(lepton_etas,lepton_pts ,bins=(50, 50), range=[[-3, 3], [190, 1000]], cmap='Blues')
plt.ylabel('lepton_pt')
plt.xlabel('lepton_eta')
plt.title('Histogram of lepton')
plt.savefig('lepton histogram.png')
plt.close()



mask_N = GenPart_pdgId == abs(9900016)
mask_tau_mom_N = (GenPart_pdgId == abs(15)) & ( mask_N[GenPart_mother_idx] == True )
tau_pt = GenPart_pt[mask_tau_mom_N]
tau_eta = GenPart_eta[mask_tau_mom_N]
## 엄마의 인덱스를 N목록중에 있나 보고 있으면 엄마가 N 인 tau

Gen_tau_pt = ak.flatten(tau_pt)  # 재그드 배열을 평탄화
Gen_tau_eta = ak.flatten(tau_eta)  # 재그드 배열을 평탄화




## Genvistau information
GenVisTau_pt = events["GenVisTau_pt"].array()
GenVisTau_eta = events["GenVisTau_eta"].array()

mask_GenVisTau = GenVisTau_pt > 190
GenVisTau_pt = GenVisTau_pt[mask_GenVisTau]
GenVisTau_eta = GenVisTau_eta[mask_GenVisTau]
print(ak.to_list(GenVisTau_pt))

GenVisTau_pt = ak.flatten(GenVisTau_pt)  # 재그드 배열을 평탄화
GenVisTau_eta = ak.flatten(GenVisTau_eta)  # 재그드 배열을 평탄화
hist, bins = np.histogram(GenVisTau_pt, bins=100, range=(0, 1000))

# 히스토그램 생성 및 저장
plt.hist2d(GenVisTau_eta, GenVisTau_pt, bins=(50, 50), range=[[-3, 3], [190, 1000]], cmap='Blues')
plt.ylabel('GenVisTau_pt')
plt.xlabel('GenVisTau_eta')
plt.title('Histogram of GenVisTau')
plt.savefig('GenVis histogram.png')
plt.close()











