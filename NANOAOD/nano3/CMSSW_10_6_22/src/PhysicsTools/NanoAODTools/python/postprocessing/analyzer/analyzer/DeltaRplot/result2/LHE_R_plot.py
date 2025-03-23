#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PhysicsTools.NanoAODTools.postprocessing.tools import *
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
#from PhysicsTools.NanoAODTools.postprocessing.analyzer.ID.GenStatus import *
#from PhysicsTools.NanoAODTools.postprocessing.analyzer.AnalyserHelper.AnalyserHelper import *
from importlib import import_module
import os
import sys
import ROOT
import argparse
import linecache
ROOT.PyConfig.IgnoreCommandLineOptions = True



# PDG ID와 입자 이름 매핑
def FlagIsOn(status,flag_n) :
    if status & (1 << (flag_n -1)) : return True
    else : return False

def isHardProcess(gen) : return FlagIsOn(gen.statusFlags,8)

def beginJob(self, histFile=None, histDirName=None):
        Module.beginJob(self, histFile, histDirName)

def build_tree(gen_parts):
    """트리 형태로 계보를 구축.gen_parts: 리스트 - 각 항목은 {'pdgId': int, 'genPartIdxMother': int} 형태의 사전"""
    tree = {}
    index_to_node = {}
    # 노드 초기화
    for idx, part in enumerate(gen_parts):
        node = {"pdgId": part["pdgId"], "parents": [], "children": [], "eta": part["eta"], "phi": part["phi"]}
        index_to_node[idx] = node
        tree[idx] = node

    # 부모-자식 관계 설정
    for idx, part in enumerate(gen_parts):
        if isHardProcess(part):
            mother_indices = part["genPartIdxMother"] if isinstance(part["genPartIdxMother"], list) else [part["genPartIdxMother"]]
            ## mother가 여러개면 리스트 타입으로 나오고 , 단일이면 정수로 나옴 .
            for mother_idx in mother_indices:
                if mother_idx >= 0:  # 유효한 부모인 경우
                    index_to_node[mother_idx]["children"].append(tree[idx])
                    tree[idx]["parents"].append(index_to_node[mother_idx])

    # 루트 노드 반환 (부모가 없고 자식이 있는 노드)
    roots = [node for idx, node in tree.items() if len(node["parents"]) == 0 and len(node["children"]) > 0]
    return roots



class ExampleAnalysis(Module):
    def __init__(self):
        self.writeHistFile = True
        

    def beginJob(self, histFile=None, histDirName=None):
        Module.beginJob(self, histFile, histDirName)
        # Delta R 히스토그램 생성
        self.addObject(ROOT.TH1F("deltaR_dist", "DeltaR Distribution between Two Quarks", 50, 0, 5))

    def analyze(self, event):
        gen_parts = Collection(event, "LHEPart")
        
        for idx, part in enumerate(gen_parts):
            # Heavy_neutrino 찾기
            if part.pdgId == 9900016 and isHardProcess(part):  # Hard Process + PDG ID
                children_indices = [i for i, p in enumerate(gen_parts) if p.genPartIdxMother == idx]
                
                # 자식이 두 개의 쿼크인지 확인
                quark_indices = [i for i in children_indices if abs(gen_parts[i].pdgId) in [1, 2, 3, 4, 5, 6]]  # u, d, s, c, b, t
                
                if len(quark_indices) >= 2:
                    # 두 쿼크의 Delta R 계산
                    idx_a, idx_b = quark_indices[0], quark_indices[1]
                    quark_a, quark_b = gen_parts[idx_a], gen_parts[idx_b]
                    delta_r=deltaR(quark_a, quark_b)
                    self.deltaR_dist.Fill(delta_r)

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
