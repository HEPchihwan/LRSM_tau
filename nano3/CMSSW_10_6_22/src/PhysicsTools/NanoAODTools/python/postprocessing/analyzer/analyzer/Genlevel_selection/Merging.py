import glob
from ROOT import *

# 디렉토리 경로
dirW1000N100 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR1000/N100"
dirW1000N500 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR1000/N500"
dirW1000N900 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR1000/N900"
dirW2000N100 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR2000/N100"
dirW2000N1000 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR2000/N1000"
dirW2000N1900 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR2000/N1900"
dirW4000N100 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR4000/N100"
dirW4000N2000 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR4000/N2000"
dirW4000N3900 = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/Genlevel_selection/result/WR4000/N3900"


## 루트 파일 가져오기 
file_list_W1000N100 = glob.glob(f"{dirW1000N100}/*.root") 
file_list_W1000N500 = glob.glob(f"{dirW1000N500}/*.root")
file_list_W1000N900 = glob.glob(f"{dirW1000N900}/*.root")
file_list_W2000N100 = glob.glob(f"{dirW2000N100}/*.root")
file_list_W2000N1000 = glob.glob(f"{dirW2000N1000}/*.root")
file_list_W2000N1900 = glob.glob(f"{dirW2000N1900}/*.root")
file_list_W4000N100 = glob.glob(f"{dirW4000N100}/*.root")
file_list_W4000N2000 = glob.glob(f"{dirW4000N2000}/*.root")
file_list_W4000N3900 = glob.glob(f"{dirW4000N3900}/*.root")

file_lists = [file_list_W1000N100, file_list_W1000N500, file_list_W1000N900 , file_list_W2000N100, file_list_W2000N1000,file_list_W2000N1900, file_list_W4000N100, file_list_W4000N2000, file_list_W4000N3900]

# 출력 ROOT 파일 생성
output_file = TFile("results.root", "RECREATE")


# 히스토그램 병합을 위한 빈 히스토그램 생성

#################################no####cut################################
W1000N100_nocut_tau_pt = TH1F("W1000N100_nc_tau_pt","W1000N100_nc_tau_pt", 50, 0,7000)
W1000N100_nocut_tau_eta = TH1F("W1000N100_nc_tau_eta", "W1000N100_nc_tau_eta", 50, -8, 8)
W1000N100_nocut_tau_mass = TH1F("W1000N100_nc_tau_mass", "W1000N100_nc_tau_mass", 50, 0, 7000)

W1000N100_nocut_AK4_pt = TH1F("W1000N100_nc_4_pt", "W1000N100_nc_4_pt", 50, 0, 7000)
W1000N100_nocut_AK4_eta = TH1F("W1000N100_nc_4_eta", "W1000N100_nc_4_eta", 50, -8, 8)
W1000N100_nocut_AK4_mass = TH1F("W1000N100_nc_4_mass", "W1000N100_nc_4_mass", 50, 0, 7000)

W1000N100_nocut_AK4_pt_2 = TH1F("W1000N100_nc_4_pt_2", "W1000N100_nc_4_pt_2", 50, 0, 7000)
W1000N100_nocut_AK4_eta_2 = TH1F("W1000N100_nc_4_eta_2", "W1000N100_nc_4_eta_2", 50, -8, 8)
W1000N100_nocut_AK4_mass_2 = TH1F("W1000N100_nc_4_mass_2", "W1000N100_nc_4_mass_2", 50, 0, 7000)

W1000N100_nocut_AK8_pt = TH1F("W1000N100_nc_8_pt", "W1000N100_nc_8_pt", 50, 0, 7000)
W1000N100_nocut_AK8_eta = TH1F("W1000N100_nc_8_eta", "W1000N100_nc_8_eta", 50, -8, 8)
W1000N100_nocut_AK8_mass = TH1F("W1000N100_nc_8_mass", "W1000N100_nc_8_mass", 50, 0, 7000)

W1000N100_nocut_subAK8_pt = TH1F("W1000N100_nc_sub8_pt", "W1000N100_nc_sub8_pt", 50, 0, 7000)
W1000N100_nocut_subAK8_eta = TH1F("W1000N100_nc_sub8_eta", "W1000N100_nc_sub8_eta", 50,-8, 8)
W1000N100_nocut_subAK8_mass = TH1F("W1000N100_nc_sub8_mass", "W1000N100_nc_sub8_mass", 50, 0, 7000)

W1000N100_nocut_subAK8_pt_2 = TH1F("W1000N100_nc_sub8_pt_2", "W1000N100_nc_sub8_pt_2", 50, 0, 7000)
W1000N100_nocut_subAK8_eta_2 = TH1F("W1000N100_nc_sub8_eta_2", "W1000N100_nc_sub8_eta_2", 50,-8, 8)
W1000N100_nocut_subAK8_mass_2 = TH1F("W1000N100_nc_sub8_mass_2", "W1000N100_nc_sub8_mass_2", 50, 0, 7000)

#N
W1000N100_nocut_N4_el_pt = TH1F("W1000N100_nc_N4_el_pt", "W1000N100_nc_N4_el_pt", 50, 0, 7000)
W1000N100_nocut_N4_el_eta = TH1F("W1000N100_nc_N4_el_eta", "W1000N100_nc_N4_el_eta", 50, -8, 8)
W1000N100_nocut_N4_el_mass = TH1F("W1000N100_nc_N4_el_mass", "W1000N100_nc_N4_el_mass", 50, 0, 7000)

W1000N100_nocut_N4_mu_pt = TH1F("W1000N100_nc_N4_mu_pt", "W1000N100_nc_N4_mu_pt", 50, 0, 7000)
W1000N100_nocut_N4_mu_eta = TH1F("W1000N100_nc_N4_mu_eta", "W1000N100_nc_N4_mu_eta", 50, -8, 8)
W1000N100_nocut_N4_mu_mass = TH1F("W1000N100_nc_N4_mu_mass", "W1000N100_nc_N4_mu_mass", 50, 0, 7000)

W1000N100_nocut_subAK8_el_pt = TH1F("W1000N100_nc_subN8_el_pt", "W1000N100_nc_subN8_el_pt" , 50 ,0 ,7000)
W1000N100_nocut_subAK8_el_eta = TH1F("W1000N100_nc_subN8_el_eta", "W1000N100_nc_subN8_el_eta", 50, -8, 8)
W1000N100_nocut_subAK8_el_mass = TH1F("W1000N100_nc_subN8_el_mass", "W1000N100_nc_subN8_el_mass", 50,0,7000)

W1000N100_nocut_subAK8_mu_pt = TH1F("W1000N100_nc_subN8_mu_pt", "W1000N100_nc_subN8_mu_pt", 50, 0, 7000)
W1000N100_nocut_subAK8_mu_eta = TH1F("W1000N100_nc_subN8_mu_eta", "W1000N100_nc_subN8_mu_eta", 50, -8, 8)
W1000N100_nocut_subAK8_mu_mass = TH1F("W1000N100_nc_subN8_mu_mass", "W1000N100_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W1000N100_nocut_WR4_el_pt = TH1F("W1000N100_nc_WR4_el_pt", "W1000N100_nc_WR4_el_pt", 50, 0, 7000)
W1000N100_nocut_WR4_el_eta = TH1F("W1000N100_nc_WR4_el_eta", "W1000N100_nc_WR4_el_eta", 50, -8, 8)
W1000N100_nocut_WR4_el_mass = TH1F("W1000N100_nc_WR4_el_mass", "W1000N100_nc_WR4_el_mass", 50, 0, 7000)

W1000N100_nocut_WR4_mu_pt = TH1F("W1000N100_nc_WR4_mu_pt", "W1000N100_nc_WR4_mu_pt", 50, 0, 7000)
W1000N100_nocut_WR4_mu_eta = TH1F("W1000N100_nc_WR4_mu_eta", "W1000N100_nc_WR4_mu_eta", 50, -8, 8)
W1000N100_nocut_WR4_mu_mass = TH1F("W1000N100_nc_WR4_mu_mass", "W1000N100_nc_WR4_mu_mass", 50, 0, 7000)

W1000N100_nocut_WR8_pt = TH1F("W1000N100_nc_WR8_pt", "W1000N100_nc_WR8_pt",50,0,7000)
W1000N100_nocut_WR8_eta = TH1F("W1000N100_nc_WR8_eta","W1000N100_nc_WR8_eta",50,-8,8)
W1000N100_nocut_WR8_mass = TH1F("W1000N100_nc_WR8_mass","W1000N100_nc_WR8_mass",50,0,7000)

W1000N100_nocut_subWR8_el_pt = TH1F("W1000N100_nc_subWR8_el_pt","W1000N100_nc_subWR8_el_pt",50,0,7000)
W1000N100_nocut_subWR8_el_eta = TH1F("W1000N100_nc_subWR8_el_eta","W1000N100_nc_subWR8_el_eta",50,-8,8)
W1000N100_nocut_subWR8_el_mass = TH1F("W1000N100_nc_subWR8_el_mass","W1000N100_nc_subWR8_el_mass",50,0,7000)

W1000N100_nocut_subWR8_mu_pt = TH1F("W1000N100_nc_subWR8_mu_pt","W1000N100_nc_subWR8_mu_pt",50,0,7000)
W1000N100_nocut_subWR8_mu_eta = TH1F("W1000N100_nc_subWR8_mu_eta","W1000N100_nc_subWR8_mu_eta",50,-8,8)
W1000N100_nocut_subWR8_mu_mass = TH1F("W1000N100_nc_subWR8_mu_mass","W1000N100_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W1000N100_cut_tau_pt = TH1F("W1000N100_c_tau_pt","W1000N100_c_tau_pt", 50, 0,7000)
W1000N100_cut_tau_eta = TH1F("W1000N100_c_tau_eta", "W1000N100_c_tau_eta", 50, -8, 8)
W1000N100_cut_tau_mass = TH1F("W1000N100_c_tau_mass", "W1000N100_c_tau_mass", 50, 0, 7000)

W1000N100_cut_AK4_pt = TH1F("W1000N100_c_4_pt", "W1000N100_c_4_pt", 50, 0, 7000)
W1000N100_cut_AK4_eta = TH1F("W1000N100_c_4_eta", "W1000N100_c_4_eta", 50, -8, 8)
W1000N100_cut_AK4_mass = TH1F("W1000N100_c_4_mass", "W1000N100_c_4_mass", 50, 0, 7000)

W1000N100_cut_AK4_pt_2 = TH1F("W1000N100_c_4_pt_2", "W1000N100_c_4_pt_2", 50, 0, 7000)
W1000N100_cut_AK4_eta_2 = TH1F("W1000N100_c_4_eta_2", "W1000N100_c_4_eta_2", 50, -8, 8)
W1000N100_cut_AK4_mass_2 = TH1F("W1000N100_c_4_mass_2", "W1000N100_c_4_mass_2", 50, 0, 7000)

W1000N100_cut_AK8_pt = TH1F("W1000N100_c_8_pt", "W1000N100_c_8_pt", 50, 0, 7000)
W1000N100_cut_AK8_eta = TH1F("W1000N100_c_8_eta", "W1000N100_c_8_eta", 50, -8, 8)
W1000N100_cut_AK8_mass = TH1F("W1000N100_c_8_mass", "W1000N100_c_8_mass", 50, 0, 7000)

W1000N100_cut_subAK8_pt = TH1F("W1000N100_c_sub8_pt", "W1000N100_c_sub8_pt", 50, 0, 7000)
W1000N100_cut_subAK8_eta = TH1F("W1000N100_c_sub8_eta", "W1000N100_c_sub8_eta", 50,-8, 8)
W1000N100_cut_subAK8_mass = TH1F("W1000N100_c_sub8_mass", "W1000N100_c_sub8_mass", 50, 0, 7000)

W1000N100_cut_subAK8_pt_2 = TH1F("W1000N100_c_sub8_pt_2", "W1000N100_c_sub8_pt_2", 50, 0, 7000)
W1000N100_cut_subAK8_eta_2 = TH1F("W1000N100_c_sub8_eta_2", "W1000N100_c_sub8_eta_2", 50,-8, 8)
W1000N100_cut_subAK8_mass_2 = TH1F("W1000N100_c_sub8_mass_2", "W1000N100_c_sub8_mass_2", 50, 0, 7000)

#N
W1000N100_cut_N4_el_pt = TH1F("W1000N100_c_N4_el_pt", "W1000N100_c_N4_el_pt", 50, 0, 7000)
W1000N100_cut_N4_el_eta = TH1F("W1000N100_c_N4_el_eta", "W1000N100_c_N4_el_eta", 50, -8, 8)
W1000N100_cut_N4_el_mass = TH1F("W1000N100_c_N4_el_mass", "W1000N100_c_N4_el_mass", 50, 0, 7000)

W1000N100_cut_N4_mu_pt = TH1F("W1000N100_c_N4_mu_pt", "W1000N100_c_N4_mu_pt", 50, 0, 7000)
W1000N100_cut_N4_mu_eta = TH1F("W1000N100_c_N4_mu_eta", "W1000N100_c_N4_mu_eta", 50, -8, 8)
W1000N100_cut_N4_mu_mass = TH1F("W1000N100_c_N4_mu_mass", "W1000N100_c_N4_mu_mass", 50, 0, 7000)

W1000N100_cut_subAK8_el_pt = TH1F("W1000N100_c_subN8_el_pt", "W1000N100_c_subN8_el_pt" , 50 ,0 ,7000)
W1000N100_cut_subAK8_el_eta = TH1F("W1000N100_c_subN8_el_eta", "W1000N100_c_subN8_el_eta", 50, -8, 8)
W1000N100_cut_subAK8_el_mass = TH1F("W1000N100_c_subN8_el_mass", "W1000N100_c_subN8_el_mass", 50,0,7000)

W1000N100_cut_subAK8_mu_pt = TH1F("W1000N100_c_subN8_mu_pt", "W1000N100_c_subN8_mu_pt", 50, 0, 7000)
W1000N100_cut_subAK8_mu_eta = TH1F("W1000N100_c_subN8_mu_eta", "W1000N100_c_subN8_mu_eta", 50, -8, 8)
W1000N100_cut_subAK8_mu_mass = TH1F("W1000N100_c_subN8_mu_mass", "W1000N100_c_subN8_mu_mass", 50, 0, 7000)


# wr
W1000N100_cut_WR4_el_pt = TH1F("W1000N100_c_WR4_el_pt", "W1000N100_c_WR4_el_pt", 50, 0, 7000)
W1000N100_cut_WR4_el_eta = TH1F("W1000N100_c_WR4_el_eta", "W1000N100_c_WR4_el_eta", 50, -8, 8)
W1000N100_cut_WR4_el_mass = TH1F("W1000N100_c_WR4_el_mass", "W1000N100_c_WR4_el_mass", 50, 0, 7000)

W1000N100_cut_WR4_mu_pt = TH1F("W1000N100_c_WR4_mu_pt", "W1000N100_c_WR4_mu_pt", 50, 0, 7000)
W1000N100_cut_WR4_mu_eta = TH1F("W1000N100_c_WR4_mu_eta", "W1000N100_c_WR4_mu_eta", 50, -8, 8)
W1000N100_cut_WR4_mu_mass = TH1F("W1000N100_c_WR4_mu_mass", "W1000N100_c_WR4_mu_mass", 50, 0, 7000)

W1000N100_cut_WR8_pt = TH1F("W1000N100_c_WR8_pt", "W1000N100_c_WR8_pt",50,0,7000)
W1000N100_cut_WR8_eta = TH1F("W1000N100_c_WR8_eta","W1000N100_c_WR8_eta",50,-8,8)
W1000N100_cut_WR8_mass = TH1F("W1000N100_c_WR8_mass","W1000N100_c_WR8_mass",50,0,7000)

W1000N100_cut_subWR8_el_pt = TH1F("W1000N100_c_subWR8_el_pt","W1000N100_c_subWR8_el_pt",50,0,7000)
W1000N100_cut_subWR8_el_eta = TH1F("W1000N100_c_subWR8_el_eta","W1000N100_c_subWR8_el_eta",50,-8,8)
W1000N100_cut_subWR8_el_mass = TH1F("W1000N100_c_subWR8_el_mass","W1000N100_c_subWR8_el_mass",50,0,7000)

W1000N100_cut_subWR8_mu_pt = TH1F("W1000N100_c_subWR8_mu_pt","W1000N100_c_subWR8_mu_pt",50,0,7000)
W1000N100_cut_subWR8_mu_eta = TH1F("W1000N100_c_subWR8_mu_eta","W1000N100_c_subWR8_mu_eta",50,-8,8)
W1000N100_cut_subWR8_mu_mass = TH1F("W1000N100_c_subWR8_mu_mass","W1000N100_c_subWR8_mu_mass",50,0,7000)

#################################no####cut################################
W1000N500_nocut_tau_pt = TH1F("W1000N500_nc_tau_pt","W1000N500_nc_tau_pt", 50, 0,7000)
W1000N500_nocut_tau_eta = TH1F("W1000N500_nc_tau_eta", "W1000N500_nc_tau_eta", 50, -8, 8)
W1000N500_nocut_tau_mass = TH1F("W1000N500_nc_tau_mass", "W1000N500_nc_tau_mass", 50, 0, 7000)

W1000N500_nocut_AK4_pt = TH1F("W1000N500_nc_4_pt", "W1000N500_nc_4_pt", 50, 0, 7000)
W1000N500_nocut_AK4_eta = TH1F("W1000N500_nc_4_eta", "W1000N500_nc_4_eta", 50, -8, 8)
W1000N500_nocut_AK4_mass = TH1F("W1000N500_nc_4_mass", "W1000N500_nc_4_mass", 50, 0, 7000)

W1000N500_nocut_AK4_pt_2 = TH1F("W1000N500_nc_4_pt_2", "W1000N500_nc_4_pt_2", 50, 0, 7000)
W1000N500_nocut_AK4_eta_2 = TH1F("W1000N500_nc_4_eta_2", "W1000N500_nc_4_eta_2", 50, -8, 8)
W1000N500_nocut_AK4_mass_2 = TH1F("W1000N500_nc_4_mass_2", "W1000N500_nc_4_mass_2", 50, 0, 7000)

W1000N500_nocut_AK8_pt = TH1F("W1000N500_nc_8_pt", "W1000N500_nc_8_pt", 50, 0, 7000)
W1000N500_nocut_AK8_eta = TH1F("W1000N500_nc_8_eta", "W1000N500_nc_8_eta", 50, -8, 8)
W1000N500_nocut_AK8_mass = TH1F("W1000N500_nc_8_mass", "W1000N500_nc_8_mass", 50, 0, 7000)

W1000N500_nocut_subAK8_pt = TH1F("W1000N500_nc_sub8_pt", "W1000N500_nc_sub8_pt", 50, 0, 7000)
W1000N500_nocut_subAK8_eta = TH1F("W1000N500_nc_sub8_eta", "W1000N500_nc_sub8_eta", 50,-8, 8)
W1000N500_nocut_subAK8_mass = TH1F("W1000N500_nc_sub8_mass", "W1000N500_nc_sub8_mass", 50, 0, 7000)

W1000N500_nocut_subAK8_pt_2 = TH1F("W1000N500_nc_sub8_pt_2", "W1000N500_nc_sub8_pt_2", 50, 0, 7000)
W1000N500_nocut_subAK8_eta_2 = TH1F("W1000N500_nc_sub8_eta_2", "W1000N500_nc_sub8_eta_2", 50,-8, 8)
W1000N500_nocut_subAK8_mass_2 = TH1F("W1000N500_nc_sub8_mass_2", "W1000N500_nc_sub8_mass_2", 50, 0, 7000)

#N
W1000N500_nocut_N4_el_pt = TH1F("W1000N500_nc_N4_el_pt", "W1000N500_nc_N4_el_pt", 50, 0, 7000)
W1000N500_nocut_N4_el_eta = TH1F("W1000N500_nc_N4_el_eta", "W1000N500_nc_N4_el_eta", 50, -8, 8)
W1000N500_nocut_N4_el_mass = TH1F("W1000N500_nc_N4_el_mass", "W1000N500_nc_N4_el_mass", 50, 0, 7000)

W1000N500_nocut_N4_mu_pt = TH1F("W1000N500_nc_N4_mu_pt", "W1000N500_nc_N4_mu_pt", 50, 0, 7000)
W1000N500_nocut_N4_mu_eta = TH1F("W1000N500_nc_N4_mu_eta", "W1000N500_nc_N4_mu_eta", 50, -8, 8)
W1000N500_nocut_N4_mu_mass = TH1F("W1000N500_nc_N4_mu_mass", "W1000N500_nc_N4_mu_mass", 50, 0, 7000)

W1000N500_nocut_subAK8_el_pt = TH1F("W1000N500_nc_subN8_el_pt", "W1000N500_nc_subN8_el_pt" , 50 ,0 ,7000)
W1000N500_nocut_subAK8_el_eta = TH1F("W1000N500_nc_subN8_el_eta", "W1000N500_nc_subN8_el_eta", 50, -8, 8)
W1000N500_nocut_subAK8_el_mass = TH1F("W1000N500_nc_subN8_el_mass", "W1000N500_nc_subN8_el_mass", 50,0,7000)

W1000N500_nocut_subAK8_mu_pt = TH1F("W1000N500_nc_subN8_mu_pt", "W1000N500_nc_subN8_mu_pt", 50, 0, 7000)
W1000N500_nocut_subAK8_mu_eta = TH1F("W1000N500_nc_subN8_mu_eta", "W1000N500_nc_subN8_mu_eta", 50, -8, 8)
W1000N500_nocut_subAK8_mu_mass = TH1F("W1000N500_nc_subN8_mu_mass", "W1000N500_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W1000N500_nocut_WR4_el_pt = TH1F("W1000N500_nc_WR4_el_pt", "W1000N500_nc_WR4_el_pt", 50, 0, 7000)
W1000N500_nocut_WR4_el_eta = TH1F("W1000N500_nc_WR4_el_eta", "W1000N500_nc_WR4_el_eta", 50, -8, 8)
W1000N500_nocut_WR4_el_mass = TH1F("W1000N500_nc_WR4_el_mass", "W1000N500_nc_WR4_el_mass", 50, 0, 7000)

W1000N500_nocut_WR4_mu_pt = TH1F("W1000N500_nc_WR4_mu_pt", "W1000N500_nc_WR4_mu_pt", 50, 0, 7000)
W1000N500_nocut_WR4_mu_eta = TH1F("W1000N500_nc_WR4_mu_eta", "W1000N500_nc_WR4_mu_eta", 50, -8, 8)
W1000N500_nocut_WR4_mu_mass = TH1F("W1000N500_nc_WR4_mu_mass", "W1000N500_nc_WR4_mu_mass", 50, 0, 7000)

W1000N500_nocut_WR8_pt = TH1F("W1000N500_nc_WR8_pt", "W1000N500_nc_WR8_pt",50,0,7000)
W1000N500_nocut_WR8_eta = TH1F("W1000N500_nc_WR8_eta","W1000N500_nc_WR8_eta",50,-8,8)
W1000N500_nocut_WR8_mass = TH1F("W1000N500_nc_WR8_mass","W1000N500_nc_WR8_mass",50,0,7000)

W1000N500_nocut_subWR8_el_pt = TH1F("W1000N500_nc_subWR8_el_pt","W1000N500_nc_subWR8_el_pt",50,0,7000)
W1000N500_nocut_subWR8_el_eta = TH1F("W1000N500_nc_subWR8_el_eta","W1000N500_nc_subWR8_el_eta",50,-8,8)
W1000N500_nocut_subWR8_el_mass = TH1F("W1000N500_nc_subWR8_el_mass","W1000N500_nc_subWR8_el_mass",50,0,7000)

W1000N500_nocut_subWR8_mu_pt = TH1F("W1000N500_nc_subWR8_mu_pt","W1000N500_nc_subWR8_mu_pt",50,0,7000)
W1000N500_nocut_subWR8_mu_eta = TH1F("W1000N500_nc_subWR8_mu_eta","W1000N500_nc_subWR8_mu_eta",50,-8,8)
W1000N500_nocut_subWR8_mu_mass = TH1F("W1000N500_nc_subWR8_mu_mass","W1000N500_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W1000N500_cut_tau_pt = TH1F("W1000N500_c_tau_pt","W1000N500_c_tau_pt", 50, 0,7000)
W1000N500_cut_tau_eta = TH1F("W1000N500_c_tau_eta", "W1000N500_c_tau_eta", 50, -8, 8)
W1000N500_cut_tau_mass = TH1F("W1000N500_c_tau_mass", "W1000N500_c_tau_mass", 50, 0, 7000)

W1000N500_cut_AK4_pt = TH1F("W1000N500_c_4_pt", "W1000N500_c_4_pt", 50, 0, 7000)
W1000N500_cut_AK4_eta = TH1F("W1000N500_c_4_eta", "W1000N500_c_4_eta", 50, -8, 8)
W1000N500_cut_AK4_mass = TH1F("W1000N500_c_4_mass", "W1000N500_c_4_mass", 50, 0, 7000)

W1000N500_cut_AK4_pt_2 = TH1F("W1000N500_c_4_pt_2", "W1000N500_c_4_pt_2", 50, 0, 7000)
W1000N500_cut_AK4_eta_2 = TH1F("W1000N500_c_4_eta_2", "W1000N500_c_4_eta_2", 50, -8, 8)
W1000N500_cut_AK4_mass_2 = TH1F("W1000N500_c_4_mass_2", "W1000N500_c_4_mass_2", 50, 0, 7000)

W1000N500_cut_AK8_pt = TH1F("W1000N500_c_8_pt", "W1000N500_c_8_pt", 50, 0, 7000)
W1000N500_cut_AK8_eta = TH1F("W1000N500_c_8_eta", "W1000N500_c_8_eta", 50, -8, 8)
W1000N500_cut_AK8_mass = TH1F("W1000N500_c_8_mass", "W1000N500_c_8_mass", 50, 0, 7000)

W1000N500_cut_subAK8_pt = TH1F("W1000N500_c_sub8_pt", "W1000N500_c_sub8_pt", 50, 0, 7000)
W1000N500_cut_subAK8_eta = TH1F("W1000N500_c_sub8_eta", "W1000N500_c_sub8_eta", 50,-8, 8)
W1000N500_cut_subAK8_mass = TH1F("W1000N500_c_sub8_mass", "W1000N500_c_sub8_mass", 50, 0, 7000)

W1000N500_cut_subAK8_pt_2 = TH1F("W1000N500_c_sub8_pt_2", "W1000N500_c_sub8_pt_2", 50, 0, 7000)
W1000N500_cut_subAK8_eta_2 = TH1F("W1000N500_c_sub8_eta_2", "W1000N500_c_sub8_eta_2", 50,-8, 8)
W1000N500_cut_subAK8_mass_2 = TH1F("W1000N500_c_sub8_mass_2", "W1000N500_c_sub8_mass_2", 50, 0, 7000)

#N
W1000N500_cut_N4_el_pt = TH1F("W1000N500_c_N4_el_pt", "W1000N500_c_N4_el_pt", 50, 0, 7000)
W1000N500_cut_N4_el_eta = TH1F("W1000N500_c_N4_el_eta", "W1000N500_c_N4_el_eta", 50, -8, 8)
W1000N500_cut_N4_el_mass = TH1F("W1000N500_c_N4_el_mass", "W1000N500_c_N4_el_mass", 50, 0, 7000)

W1000N500_cut_N4_mu_pt = TH1F("W1000N500_c_N4_mu_pt", "W1000N500_c_N4_mu_pt", 50, 0, 7000)
W1000N500_cut_N4_mu_eta = TH1F("W1000N500_c_N4_mu_eta", "W1000N500_c_N4_mu_eta", 50, -8, 8)
W1000N500_cut_N4_mu_mass = TH1F("W1000N500_c_N4_mu_mass", "W1000N500_c_N4_mu_mass", 50, 0, 7000)

W1000N500_cut_subAK8_el_pt = TH1F("W1000N500_c_subN8_el_pt", "W1000N500_c_subN8_el_pt" , 50 ,0 ,7000)
W1000N500_cut_subAK8_el_eta = TH1F("W1000N500_c_subN8_el_eta", "W1000N500_c_subN8_el_eta", 50, -8, 8)
W1000N500_cut_subAK8_el_mass = TH1F("W1000N500_c_subN8_el_mass", "W1000N500_c_subN8_el_mass", 50,0,7000)

W1000N500_cut_subAK8_mu_pt = TH1F("W1000N500_c_subN8_mu_pt", "W1000N500_c_subN8_mu_pt", 50, 0, 7000)
W1000N500_cut_subAK8_mu_eta = TH1F("W1000N500_c_subN8_mu_eta", "W1000N500_c_subN8_mu_eta", 50, -8, 8)
W1000N500_cut_subAK8_mu_mass = TH1F("W1000N500_c_subN8_mu_mass", "W1000N500_c_subN8_mu_mass", 50, 0, 7000)


# wr
W1000N500_cut_WR4_el_pt = TH1F("W1000N500_c_WR4_el_pt", "W1000N500_c_WR4_el_pt", 50, 0, 7000)
W1000N500_cut_WR4_el_eta = TH1F("W1000N500_c_WR4_el_eta", "W1000N500_c_WR4_el_eta", 50, -8, 8)
W1000N500_cut_WR4_el_mass = TH1F("W1000N500_c_WR4_el_mass", "W1000N500_c_WR4_el_mass", 50, 0, 7000)

W1000N500_cut_WR4_mu_pt = TH1F("W1000N500_c_WR4_mu_pt", "W1000N500_c_WR4_mu_pt", 50, 0, 7000)
W1000N500_cut_WR4_mu_eta = TH1F("W1000N500_c_WR4_mu_eta", "W1000N500_c_WR4_mu_eta", 50, -8, 8)
W1000N500_cut_WR4_mu_mass = TH1F("W1000N500_c_WR4_mu_mass", "W1000N500_c_WR4_mu_mass", 50, 0, 7000)

W1000N500_cut_WR8_pt = TH1F("W1000N500_c_WR8_pt", "W1000N500_c_WR8_pt",50,0,7000)
W1000N500_cut_WR8_eta = TH1F("W1000N500_c_WR8_eta","W1000N500_c_WR8_eta",50,-8,8)
W1000N500_cut_WR8_mass = TH1F("W1000N500_c_WR8_mass","W1000N500_c_WR8_mass",50,0,7000)

W1000N500_cut_subWR8_el_pt = TH1F("W1000N500_c_subWR8_el_pt","W1000N500_c_subWR8_el_pt",50,0,7000)
W1000N500_cut_subWR8_el_eta = TH1F("W1000N500_c_subWR8_el_eta","W1000N500_c_subWR8_el_eta",50,-8,8)
W1000N500_cut_subWR8_el_mass = TH1F("W1000N500_c_subWR8_el_mass","W1000N500_c_subWR8_el_mass",50,0,7000)

W1000N500_cut_subWR8_mu_pt = TH1F("W1000N500_c_subWR8_mu_pt","W1000N500_c_subWR8_mu_pt",50,0,7000)
W1000N500_cut_subWR8_mu_eta = TH1F("W1000N500_c_subWR8_mu_eta","W1000N500_c_subWR8_mu_eta",50,-8,8)
W1000N500_cut_subWR8_mu_mass = TH1F("W1000N500_c_subWR8_mu_mass","W1000N500_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################

#################################no####cut################################
W1000N900_nocut_tau_pt = TH1F("W1000N900_nc_tau_pt","W1000N900_nc_tau_pt", 50, 0,7000)
W1000N900_nocut_tau_eta = TH1F("W1000N900_nc_tau_eta", "W1000N900_nc_tau_eta", 50, -8, 8)
W1000N900_nocut_tau_mass = TH1F("W1000N900_nc_tau_mass", "W1000N900_nc_tau_mass", 50, 0, 7000)

W1000N900_nocut_AK4_pt = TH1F("W1000N900_nc_4_pt", "W1000N900_nc_4_pt", 50, 0, 7000)
W1000N900_nocut_AK4_eta = TH1F("W1000N900_nc_4_eta", "W1000N900_nc_4_eta", 50, -8, 8)
W1000N900_nocut_AK4_mass = TH1F("W1000N900_nc_4_mass", "W1000N900_nc_4_mass", 50, 0, 7000)

W1000N900_nocut_AK4_pt_2 = TH1F("W1000N900_nc_4_pt_2", "W1000N900_nc_4_pt_2", 50, 0, 7000)
W1000N900_nocut_AK4_eta_2 = TH1F("W1000N900_nc_4_eta_2", "W1000N900_nc_4_eta_2", 50, -8, 8)
W1000N900_nocut_AK4_mass_2 = TH1F("W1000N900_nc_4_mass_2", "W1000N900_nc_4_mass_2", 50, 0, 7000)

W1000N900_nocut_AK8_pt = TH1F("W1000N900_nc_8_pt", "W1000N900_nc_8_pt", 50, 0, 7000)
W1000N900_nocut_AK8_eta = TH1F("W1000N900_nc_8_eta", "W1000N900_nc_8_eta", 50, -8, 8)
W1000N900_nocut_AK8_mass = TH1F("W1000N900_nc_8_mass", "W1000N900_nc_8_mass", 50, 0, 7000)

W1000N900_nocut_subAK8_pt = TH1F("W1000N900_nc_sub8_pt", "W1000N900_nc_sub8_pt", 50, 0, 7000)
W1000N900_nocut_subAK8_eta = TH1F("W1000N900_nc_sub8_eta", "W1000N900_nc_sub8_eta", 50,-8, 8)
W1000N900_nocut_subAK8_mass = TH1F("W1000N900_nc_sub8_mass", "W1000N900_nc_sub8_mass", 50, 0, 7000)

W1000N900_nocut_subAK8_pt_2 = TH1F("W1000N900_nc_sub8_pt_2", "W1000N900_nc_sub8_pt_2", 50, 0, 7000)
W1000N900_nocut_subAK8_eta_2 = TH1F("W1000N900_nc_sub8_eta_2", "W1000N900_nc_sub8_eta_2", 50,-8, 8)
W1000N900_nocut_subAK8_mass_2 = TH1F("W1000N900_nc_sub8_mass_2", "W1000N900_nc_sub8_mass_2", 50, 0, 7000)

#N
W1000N900_nocut_N4_el_pt = TH1F("W1000N900_nc_N4_el_pt", "W1000N900_nc_N4_el_pt", 50, 0, 7000)
W1000N900_nocut_N4_el_eta = TH1F("W1000N900_nc_N4_el_eta", "W1000N900_nc_N4_el_eta", 50, -8, 8)
W1000N900_nocut_N4_el_mass = TH1F("W1000N900_nc_N4_el_mass", "W1000N900_nc_N4_el_mass", 50, 0, 7000)

W1000N900_nocut_N4_mu_pt = TH1F("W1000N900_nc_N4_mu_pt", "W1000N900_nc_N4_mu_pt", 50, 0, 7000)
W1000N900_nocut_N4_mu_eta = TH1F("W1000N900_nc_N4_mu_eta", "W1000N900_nc_N4_mu_eta", 50, -8, 8)
W1000N900_nocut_N4_mu_mass = TH1F("W1000N900_nc_N4_mu_mass", "W1000N900_nc_N4_mu_mass", 50, 0, 7000)

W1000N900_nocut_subAK8_el_pt = TH1F("W1000N900_nc_subN8_el_pt", "W1000N900_nc_subN8_el_pt" , 50 ,0 ,7000)
W1000N900_nocut_subAK8_el_eta = TH1F("W1000N900_nc_subN8_el_eta", "W1000N900_nc_subN8_el_eta", 50, -8, 8)
W1000N900_nocut_subAK8_el_mass = TH1F("W1000N900_nc_subN8_el_mass", "W1000N900_nc_subN8_el_mass", 50,0,7000)

W1000N900_nocut_subAK8_mu_pt = TH1F("W1000N900_nc_subN8_mu_pt", "W1000N900_nc_subN8_mu_pt", 50, 0, 7000)
W1000N900_nocut_subAK8_mu_eta = TH1F("W1000N900_nc_subN8_mu_eta", "W1000N900_nc_subN8_mu_eta", 50, -8, 8)
W1000N900_nocut_subAK8_mu_mass = TH1F("W1000N900_nc_subN8_mu_mass", "W1000N900_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W1000N900_nocut_WR4_el_pt = TH1F("W1000N900_nc_WR4_el_pt", "W1000N900_nc_WR4_el_pt", 50, 0, 7000)
W1000N900_nocut_WR4_el_eta = TH1F("W1000N900_nc_WR4_el_eta", "W1000N900_nc_WR4_el_eta", 50, -8, 8)
W1000N900_nocut_WR4_el_mass = TH1F("W1000N900_nc_WR4_el_mass", "W1000N900_nc_WR4_el_mass", 50, 0, 7000)

W1000N900_nocut_WR4_mu_pt = TH1F("W1000N900_nc_WR4_mu_pt", "W1000N900_nc_WR4_mu_pt", 50, 0, 7000)
W1000N900_nocut_WR4_mu_eta = TH1F("W1000N900_nc_WR4_mu_eta", "W1000N900_nc_WR4_mu_eta", 50, -8, 8)
W1000N900_nocut_WR4_mu_mass = TH1F("W1000N900_nc_WR4_mu_mass", "W1000N900_nc_WR4_mu_mass", 50, 0, 7000)

W1000N900_nocut_WR8_pt = TH1F("W1000N900_nc_WR8_pt", "W1000N900_nc_WR8_pt",50,0,7000)
W1000N900_nocut_WR8_eta = TH1F("W1000N900_nc_WR8_eta","W1000N900_nc_WR8_eta",50,-8,8)
W1000N900_nocut_WR8_mass = TH1F("W1000N900_nc_WR8_mass","W1000N900_nc_WR8_mass",50,0,7000)

W1000N900_nocut_subWR8_el_pt = TH1F("W1000N900_nc_subWR8_el_pt","W1000N900_nc_subWR8_el_pt",50,0,7000)
W1000N900_nocut_subWR8_el_eta = TH1F("W1000N900_nc_subWR8_el_eta","W1000N900_nc_subWR8_el_eta",50,-8,8)
W1000N900_nocut_subWR8_el_mass = TH1F("W1000N900_nc_subWR8_el_mass","W1000N900_nc_subWR8_el_mass",50,0,7000)

W1000N900_nocut_subWR8_mu_pt = TH1F("W1000N900_nc_subWR8_mu_pt","W1000N900_nc_subWR8_mu_pt",50,0,7000)
W1000N900_nocut_subWR8_mu_eta = TH1F("W1000N900_nc_subWR8_mu_eta","W1000N900_nc_subWR8_mu_eta",50,-8,8)
W1000N900_nocut_subWR8_mu_mass = TH1F("W1000N900_nc_subWR8_mu_mass","W1000N900_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W1000N900_cut_tau_pt = TH1F("W1000N900_c_tau_pt","W1000N900_c_tau_pt", 50, 0,7000)
W1000N900_cut_tau_eta = TH1F("W1000N900_c_tau_eta", "W1000N900_c_tau_eta", 50, -8, 8)
W1000N900_cut_tau_mass = TH1F("W1000N900_c_tau_mass", "W1000N900_c_tau_mass", 50, 0, 7000)

W1000N900_cut_AK4_pt = TH1F("W1000N900_c_4_pt", "W1000N900_c_4_pt", 50, 0, 7000)
W1000N900_cut_AK4_eta = TH1F("W1000N900_c_4_eta", "W1000N900_c_4_eta", 50, -8, 8)
W1000N900_cut_AK4_mass = TH1F("W1000N900_c_4_mass", "W1000N900_c_4_mass", 50, 0, 7000)

W1000N900_cut_AK4_pt_2 = TH1F("W1000N900_c_4_pt_2", "W1000N900_c_4_pt_2", 50, 0, 7000)
W1000N900_cut_AK4_eta_2 = TH1F("W1000N900_c_4_eta_2", "W1000N900_c_4_eta_2", 50, -8, 8)
W1000N900_cut_AK4_mass_2 = TH1F("W1000N900_c_4_mass_2", "W1000N900_c_4_mass_2", 50, 0, 7000)

W1000N900_cut_AK8_pt = TH1F("W1000N900_c_8_pt", "W1000N900_c_8_pt", 50, 0, 7000)
W1000N900_cut_AK8_eta = TH1F("W1000N900_c_8_eta", "W1000N900_c_8_eta", 50, -8, 8)
W1000N900_cut_AK8_mass = TH1F("W1000N900_c_8_mass", "W1000N900_c_8_mass", 50, 0, 7000)

W1000N900_cut_subAK8_pt = TH1F("W1000N900_c_sub8_pt", "W1000N900_c_sub8_pt", 50, 0, 7000)
W1000N900_cut_subAK8_eta = TH1F("W1000N900_c_sub8_eta", "W1000N900_c_sub8_eta", 50,-8, 8)
W1000N900_cut_subAK8_mass = TH1F("W1000N900_c_sub8_mass", "W1000N900_c_sub8_mass", 50, 0, 7000)

W1000N900_cut_subAK8_pt_2 = TH1F("W1000N900_c_sub8_pt_2", "W1000N900_c_sub8_pt_2", 50, 0, 7000)
W1000N900_cut_subAK8_eta_2 = TH1F("W1000N900_c_sub8_eta_2", "W1000N900_c_sub8_eta_2", 50,-8, 8)
W1000N900_cut_subAK8_mass_2 = TH1F("W1000N900_c_sub8_mass_2", "W1000N900_c_sub8_mass_2", 50, 0, 7000)

#N
W1000N900_cut_N4_el_pt = TH1F("W1000N900_c_N4_el_pt", "W1000N900_c_N4_el_pt", 50, 0, 7000)
W1000N900_cut_N4_el_eta = TH1F("W1000N900_c_N4_el_eta", "W1000N900_c_N4_el_eta", 50, -8, 8)
W1000N900_cut_N4_el_mass = TH1F("W1000N900_c_N4_el_mass", "W1000N900_c_N4_el_mass", 50, 0, 7000)

W1000N900_cut_N4_mu_pt = TH1F("W1000N900_c_N4_mu_pt", "W1000N900_c_N4_mu_pt", 50, 0, 7000)
W1000N900_cut_N4_mu_eta = TH1F("W1000N900_c_N4_mu_eta", "W1000N900_c_N4_mu_eta", 50, -8, 8)
W1000N900_cut_N4_mu_mass = TH1F("W1000N900_c_N4_mu_mass", "W1000N900_c_N4_mu_mass", 50, 0, 7000)

W1000N900_cut_subAK8_el_pt = TH1F("W1000N900_c_subN8_el_pt", "W1000N900_c_subN8_el_pt" , 50 ,0 ,7000)
W1000N900_cut_subAK8_el_eta = TH1F("W1000N900_c_subN8_el_eta", "W1000N900_c_subN8_el_eta", 50, -8, 8)
W1000N900_cut_subAK8_el_mass = TH1F("W1000N900_c_subN8_el_mass", "W1000N900_c_subN8_el_mass", 50,0,7000)

W1000N900_cut_subAK8_mu_pt = TH1F("W1000N900_c_subN8_mu_pt", "W1000N900_c_subN8_mu_pt", 50, 0, 7000)
W1000N900_cut_subAK8_mu_eta = TH1F("W1000N900_c_subN8_mu_eta", "W1000N900_c_subN8_mu_eta", 50, -8, 8)
W1000N900_cut_subAK8_mu_mass = TH1F("W1000N900_c_subN8_mu_mass", "W1000N900_c_subN8_mu_mass", 50, 0, 7000)


# wr
W1000N900_cut_WR4_el_pt = TH1F("W1000N900_c_WR4_el_pt", "W1000N900_c_WR4_el_pt", 50, 0, 7000)
W1000N900_cut_WR4_el_eta = TH1F("W1000N900_c_WR4_el_eta", "W1000N900_c_WR4_el_eta", 50, -8, 8)
W1000N900_cut_WR4_el_mass = TH1F("W1000N900_c_WR4_el_mass", "W1000N900_c_WR4_el_mass", 50, 0, 7000)

W1000N900_cut_WR4_mu_pt = TH1F("W1000N900_c_WR4_mu_pt", "W1000N900_c_WR4_mu_pt", 50, 0, 7000)
W1000N900_cut_WR4_mu_eta = TH1F("W1000N900_c_WR4_mu_eta", "W1000N900_c_WR4_mu_eta", 50, -8, 8)
W1000N900_cut_WR4_mu_mass = TH1F("W1000N900_c_WR4_mu_mass", "W1000N900_c_WR4_mu_mass", 50, 0, 7000)

W1000N900_cut_WR8_pt = TH1F("W1000N900_c_WR8_pt", "W1000N900_c_WR8_pt",50,0,7000)
W1000N900_cut_WR8_eta = TH1F("W1000N900_c_WR8_eta","W1000N900_c_WR8_eta",50,-8,8)
W1000N900_cut_WR8_mass = TH1F("W1000N900_c_WR8_mass","W1000N900_c_WR8_mass",50,0,7000)

W1000N900_cut_subWR8_el_pt = TH1F("W1000N900_c_subWR8_el_pt","W1000N900_c_subWR8_el_pt",50,0,7000)
W1000N900_cut_subWR8_el_eta = TH1F("W1000N900_c_subWR8_el_eta","W1000N900_c_subWR8_el_eta",50,-8,8)
W1000N900_cut_subWR8_el_mass = TH1F("W1000N900_c_subWR8_el_mass","W1000N900_c_subWR8_el_mass",50,0,7000)

W1000N900_cut_subWR8_mu_pt = TH1F("W1000N900_c_subWR8_mu_pt","W1000N900_c_subWR8_mu_pt",50,0,7000)
W1000N900_cut_subWR8_mu_eta = TH1F("W1000N900_c_subWR8_mu_eta","W1000N900_c_subWR8_mu_eta",50,-8,8)
W1000N900_cut_subWR8_mu_mass = TH1F("W1000N900_c_subWR8_mu_mass","W1000N900_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################
#################################no####cut################################
W2000N100_nocut_tau_pt = TH1F("W2000N100_nc_tau_pt","W2000N100_nc_tau_pt", 50, 0,7000)
W2000N100_nocut_tau_eta = TH1F("W2000N100_nc_tau_eta", "W2000N100_nc_tau_eta", 50, -8, 8)
W2000N100_nocut_tau_mass = TH1F("W2000N100_nc_tau_mass", "W2000N100_nc_tau_mass", 50, 0, 7000)

W2000N100_nocut_AK4_pt = TH1F("W2000N100_nc_4_pt", "W2000N100_nc_4_pt", 50, 0, 7000)
W2000N100_nocut_AK4_eta = TH1F("W2000N100_nc_4_eta", "W2000N100_nc_4_eta", 50, -8, 8)
W2000N100_nocut_AK4_mass = TH1F("W2000N100_nc_4_mass", "W2000N100_nc_4_mass", 50, 0, 7000)

W2000N100_nocut_AK4_pt_2 = TH1F("W2000N100_nc_4_pt_2", "W2000N100_nc_4_pt_2", 50, 0, 7000)
W2000N100_nocut_AK4_eta_2 = TH1F("W2000N100_nc_4_eta_2", "W2000N100_nc_4_eta_2", 50, -8, 8)
W2000N100_nocut_AK4_mass_2 = TH1F("W2000N100_nc_4_mass_2", "W2000N100_nc_4_mass_2", 50, 0, 7000)

W2000N100_nocut_AK8_pt = TH1F("W2000N100_nc_8_pt", "W2000N100_nc_8_pt", 50, 0, 7000)
W2000N100_nocut_AK8_eta = TH1F("W2000N100_nc_8_eta", "W2000N100_nc_8_eta", 50, -8, 8)
W2000N100_nocut_AK8_mass = TH1F("W2000N100_nc_8_mass", "W2000N100_nc_8_mass", 50, 0, 7000)

W2000N100_nocut_subAK8_pt = TH1F("W2000N100_nc_sub8_pt", "W2000N100_nc_sub8_pt", 50, 0, 7000)
W2000N100_nocut_subAK8_eta = TH1F("W2000N100_nc_sub8_eta", "W2000N100_nc_sub8_eta", 50,-8, 8)
W2000N100_nocut_subAK8_mass = TH1F("W2000N100_nc_sub8_mass", "W2000N100_nc_sub8_mass", 50, 0, 7000)

W2000N100_nocut_subAK8_pt_2 = TH1F("W2000N100_nc_sub8_pt_2", "W2000N100_nc_sub8_pt_2", 50, 0, 7000)
W2000N100_nocut_subAK8_eta_2 = TH1F("W2000N100_nc_sub8_eta_2", "W2000N100_nc_sub8_eta_2", 50,-8, 8)
W2000N100_nocut_subAK8_mass_2 = TH1F("W2000N100_nc_sub8_mass_2", "W2000N100_nc_sub8_mass_2", 50, 0, 7000)

#N
W2000N100_nocut_N4_el_pt = TH1F("W2000N100_nc_N4_el_pt", "W2000N100_nc_N4_el_pt", 50, 0, 7000)
W2000N100_nocut_N4_el_eta = TH1F("W2000N100_nc_N4_el_eta", "W2000N100_nc_N4_el_eta", 50, -8, 8)
W2000N100_nocut_N4_el_mass = TH1F("W2000N100_nc_N4_el_mass", "W2000N100_nc_N4_el_mass", 50, 0, 7000)

W2000N100_nocut_N4_mu_pt = TH1F("W2000N100_nc_N4_mu_pt", "W2000N100_nc_N4_mu_pt", 50, 0, 7000)
W2000N100_nocut_N4_mu_eta = TH1F("W2000N100_nc_N4_mu_eta", "W2000N100_nc_N4_mu_eta", 50, -8, 8)
W2000N100_nocut_N4_mu_mass = TH1F("W2000N100_nc_N4_mu_mass", "W2000N100_nc_N4_mu_mass", 50, 0, 7000)

W2000N100_nocut_subAK8_el_pt = TH1F("W2000N100_nc_subN8_el_pt", "W2000N100_nc_subN8_el_pt" , 50 ,0 ,7000)
W2000N100_nocut_subAK8_el_eta = TH1F("W2000N100_nc_subN8_el_eta", "W2000N100_nc_subN8_el_eta", 50, -8, 8)
W2000N100_nocut_subAK8_el_mass = TH1F("W2000N100_nc_subN8_el_mass", "W2000N100_nc_subN8_el_mass", 50,0,7000)

W2000N100_nocut_subAK8_mu_pt = TH1F("W2000N100_nc_subN8_mu_pt", "W2000N100_nc_subN8_mu_pt", 50, 0, 7000)
W2000N100_nocut_subAK8_mu_eta = TH1F("W2000N100_nc_subN8_mu_eta", "W2000N100_nc_subN8_mu_eta", 50, -8, 8)
W2000N100_nocut_subAK8_mu_mass = TH1F("W2000N100_nc_subN8_mu_mass", "W2000N100_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W2000N100_nocut_WR4_el_pt = TH1F("W2000N100_nc_WR4_el_pt", "W2000N100_nc_WR4_el_pt", 50, 0, 7000)
W2000N100_nocut_WR4_el_eta = TH1F("W2000N100_nc_WR4_el_eta", "W2000N100_nc_WR4_el_eta", 50, -8, 8)
W2000N100_nocut_WR4_el_mass = TH1F("W2000N100_nc_WR4_el_mass", "W2000N100_nc_WR4_el_mass", 50, 0, 7000)

W2000N100_nocut_WR4_mu_pt = TH1F("W2000N100_nc_WR4_mu_pt", "W2000N100_nc_WR4_mu_pt", 50, 0, 7000)
W2000N100_nocut_WR4_mu_eta = TH1F("W2000N100_nc_WR4_mu_eta", "W2000N100_nc_WR4_mu_eta", 50, -8, 8)
W2000N100_nocut_WR4_mu_mass = TH1F("W2000N100_nc_WR4_mu_mass", "W2000N100_nc_WR4_mu_mass", 50, 0, 7000)

W2000N100_nocut_WR8_pt = TH1F("W2000N100_nc_WR8_pt", "W2000N100_nc_WR8_pt",50,0,7000)
W2000N100_nocut_WR8_eta = TH1F("W2000N100_nc_WR8_eta","W2000N100_nc_WR8_eta",50,-8,8)
W2000N100_nocut_WR8_mass = TH1F("W2000N100_nc_WR8_mass","W2000N100_nc_WR8_mass",50,0,7000)

W2000N100_nocut_subWR8_el_pt = TH1F("W2000N100_nc_subWR8_el_pt","W2000N100_nc_subWR8_el_pt",50,0,7000)
W2000N100_nocut_subWR8_el_eta = TH1F("W2000N100_nc_subWR8_el_eta","W2000N100_nc_subWR8_el_eta",50,-8,8)
W2000N100_nocut_subWR8_el_mass = TH1F("W2000N100_nc_subWR8_el_mass","W2000N100_nc_subWR8_el_mass",50,0,7000)

W2000N100_nocut_subWR8_mu_pt = TH1F("W2000N100_nc_subWR8_mu_pt","W2000N100_nc_subWR8_mu_pt",50,0,7000)
W2000N100_nocut_subWR8_mu_eta = TH1F("W2000N100_nc_subWR8_mu_eta","W2000N100_nc_subWR8_mu_eta",50,-8,8)
W2000N100_nocut_subWR8_mu_mass = TH1F("W2000N100_nc_subWR8_mu_mass","W2000N100_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W2000N100_cut_tau_pt = TH1F("W2000N100_c_tau_pt","W2000N100_c_tau_pt", 50, 0,7000)
W2000N100_cut_tau_eta = TH1F("W2000N100_c_tau_eta", "W2000N100_c_tau_eta", 50, -8, 8)
W2000N100_cut_tau_mass = TH1F("W2000N100_c_tau_mass", "W2000N100_c_tau_mass", 50, 0, 7000)

W2000N100_cut_AK4_pt = TH1F("W2000N100_c_4_pt", "W2000N100_c_4_pt", 50, 0, 7000)
W2000N100_cut_AK4_eta = TH1F("W2000N100_c_4_eta", "W2000N100_c_4_eta", 50, -8, 8)
W2000N100_cut_AK4_mass = TH1F("W2000N100_c_4_mass", "W2000N100_c_4_mass", 50, 0, 7000)

W2000N100_cut_AK4_pt_2 = TH1F("W2000N100_c_4_pt_2", "W2000N100_c_4_pt_2", 50, 0, 7000)
W2000N100_cut_AK4_eta_2 = TH1F("W2000N100_c_4_eta_2", "W2000N100_c_4_eta_2", 50, -8, 8)
W2000N100_cut_AK4_mass_2 = TH1F("W2000N100_c_4_mass_2", "W2000N100_c_4_mass_2", 50, 0, 7000)

W2000N100_cut_AK8_pt = TH1F("W2000N100_c_8_pt", "W2000N100_c_8_pt", 50, 0, 7000)
W2000N100_cut_AK8_eta = TH1F("W2000N100_c_8_eta", "W2000N100_c_8_eta", 50, -8, 8)
W2000N100_cut_AK8_mass = TH1F("W2000N100_c_8_mass", "W2000N100_c_8_mass", 50, 0, 7000)

W2000N100_cut_subAK8_pt = TH1F("W2000N100_c_sub8_pt", "W2000N100_c_sub8_pt", 50, 0, 7000)
W2000N100_cut_subAK8_eta = TH1F("W2000N100_c_sub8_eta", "W2000N100_c_sub8_eta", 50,-8, 8)
W2000N100_cut_subAK8_mass = TH1F("W2000N100_c_sub8_mass", "W2000N100_c_sub8_mass", 50, 0, 7000)

W2000N100_cut_subAK8_pt_2 = TH1F("W2000N100_c_sub8_pt_2", "W2000N100_c_sub8_pt_2", 50, 0, 7000)
W2000N100_cut_subAK8_eta_2 = TH1F("W2000N100_c_sub8_eta_2", "W2000N100_c_sub8_eta_2", 50,-8, 8)
W2000N100_cut_subAK8_mass_2 = TH1F("W2000N100_c_sub8_mass_2", "W2000N100_c_sub8_mass_2", 50, 0, 7000)

#N
W2000N100_cut_N4_el_pt = TH1F("W2000N100_c_N4_el_pt", "W2000N100_c_N4_el_pt", 50, 0, 7000)
W2000N100_cut_N4_el_eta = TH1F("W2000N100_c_N4_el_eta", "W2000N100_c_N4_el_eta", 50, -8, 8)
W2000N100_cut_N4_el_mass = TH1F("W2000N100_c_N4_el_mass", "W2000N100_c_N4_el_mass", 50, 0, 7000)

W2000N100_cut_N4_mu_pt = TH1F("W2000N100_c_N4_mu_pt", "W2000N100_c_N4_mu_pt", 50, 0, 7000)
W2000N100_cut_N4_mu_eta = TH1F("W2000N100_c_N4_mu_eta", "W2000N100_c_N4_mu_eta", 50, -8, 8)
W2000N100_cut_N4_mu_mass = TH1F("W2000N100_c_N4_mu_mass", "W2000N100_c_N4_mu_mass", 50, 0, 7000)

W2000N100_cut_subAK8_el_pt = TH1F("W2000N100_c_subN8_el_pt", "W2000N100_c_subN8_el_pt" , 50 ,0 ,7000)
W2000N100_cut_subAK8_el_eta = TH1F("W2000N100_c_subN8_el_eta", "W2000N100_c_subN8_el_eta", 50, -8, 8)
W2000N100_cut_subAK8_el_mass = TH1F("W2000N100_c_subN8_el_mass", "W2000N100_c_subN8_el_mass", 50,0,7000)

W2000N100_cut_subAK8_mu_pt = TH1F("W2000N100_c_subN8_mu_pt", "W2000N100_c_subN8_mu_pt", 50, 0, 7000)
W2000N100_cut_subAK8_mu_eta = TH1F("W2000N100_c_subN8_mu_eta", "W2000N100_c_subN8_mu_eta", 50, -8, 8)
W2000N100_cut_subAK8_mu_mass = TH1F("W2000N100_c_subN8_mu_mass", "W2000N100_c_subN8_mu_mass", 50, 0, 7000)


# wr
W2000N100_cut_WR4_el_pt = TH1F("W2000N100_c_WR4_el_pt", "W2000N100_c_WR4_el_pt", 50, 0, 7000)
W2000N100_cut_WR4_el_eta = TH1F("W2000N100_c_WR4_el_eta", "W2000N100_c_WR4_el_eta", 50, -8, 8)
W2000N100_cut_WR4_el_mass = TH1F("W2000N100_c_WR4_el_mass", "W2000N100_c_WR4_el_mass", 50, 0, 7000)

W2000N100_cut_WR4_mu_pt = TH1F("W2000N100_c_WR4_mu_pt", "W2000N100_c_WR4_mu_pt", 50, 0, 7000)
W2000N100_cut_WR4_mu_eta = TH1F("W2000N100_c_WR4_mu_eta", "W2000N100_c_WR4_mu_eta", 50, -8, 8)
W2000N100_cut_WR4_mu_mass = TH1F("W2000N100_c_WR4_mu_mass", "W2000N100_c_WR4_mu_mass", 50, 0, 7000)

W2000N100_cut_WR8_pt = TH1F("W2000N100_c_WR8_pt", "W2000N100_c_WR8_pt",50,0,7000)
W2000N100_cut_WR8_eta = TH1F("W2000N100_c_WR8_eta","W2000N100_c_WR8_eta",50,-8,8)
W2000N100_cut_WR8_mass = TH1F("W2000N100_c_WR8_mass","W2000N100_c_WR8_mass",50,0,7000)

W2000N100_cut_subWR8_el_pt = TH1F("W2000N100_c_subWR8_el_pt","W2000N100_c_subWR8_el_pt",50,0,7000)
W2000N100_cut_subWR8_el_eta = TH1F("W2000N100_c_subWR8_el_eta","W2000N100_c_subWR8_el_eta",50,-8,8)
W2000N100_cut_subWR8_el_mass = TH1F("W2000N100_c_subWR8_el_mass","W2000N100_c_subWR8_el_mass",50,0,7000)

W2000N100_cut_subWR8_mu_pt = TH1F("W2000N100_c_subWR8_mu_pt","W2000N100_c_subWR8_mu_pt",50,0,7000)
W2000N100_cut_subWR8_mu_eta = TH1F("W2000N100_c_subWR8_mu_eta","W2000N100_c_subWR8_mu_eta",50,-8,8)
W2000N100_cut_subWR8_mu_mass = TH1F("W2000N100_c_subWR8_mu_mass","W2000N100_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################
#################################no####cut################################
W2000N1000_nocut_tau_pt = TH1F("W2000N1000_nc_tau_pt","W2000N1000_nc_tau_pt", 50, 0,7000)
W2000N1000_nocut_tau_eta = TH1F("W2000N1000_nc_tau_eta", "W2000N1000_nc_tau_eta", 50, -8, 8)
W2000N1000_nocut_tau_mass = TH1F("W2000N1000_nc_tau_mass", "W2000N1000_nc_tau_mass", 50, 0, 7000)

W2000N1000_nocut_AK4_pt = TH1F("W2000N1000_nc_4_pt", "W2000N1000_nc_4_pt", 50, 0, 7000)
W2000N1000_nocut_AK4_eta = TH1F("W2000N1000_nc_4_eta", "W2000N1000_nc_4_eta", 50, -8, 8)
W2000N1000_nocut_AK4_mass = TH1F("W2000N1000_nc_4_mass", "W2000N1000_nc_4_mass", 50, 0, 7000)

W2000N1000_nocut_AK4_pt_2 = TH1F("W2000N1000_nc_4_pt_2", "W2000N1000_nc_4_pt_2", 50, 0, 7000)
W2000N1000_nocut_AK4_eta_2 = TH1F("W2000N1000_nc_4_eta_2", "W2000N1000_nc_4_eta_2", 50, -8, 8)
W2000N1000_nocut_AK4_mass_2 = TH1F("W2000N1000_nc_4_mass_2", "W2000N1000_nc_4_mass_2", 50, 0, 7000)

W2000N1000_nocut_AK8_pt = TH1F("W2000N1000_nc_8_pt", "W2000N1000_nc_8_pt", 50, 0, 7000)
W2000N1000_nocut_AK8_eta = TH1F("W2000N1000_nc_8_eta", "W2000N1000_nc_8_eta", 50, -8, 8)
W2000N1000_nocut_AK8_mass = TH1F("W2000N1000_nc_8_mass", "W2000N1000_nc_8_mass", 50, 0, 7000)

W2000N1000_nocut_subAK8_pt = TH1F("W2000N1000_nc_sub8_pt", "W2000N1000_nc_sub8_pt", 50, 0, 7000)
W2000N1000_nocut_subAK8_eta = TH1F("W2000N1000_nc_sub8_eta", "W2000N1000_nc_sub8_eta", 50,-8, 8)
W2000N1000_nocut_subAK8_mass = TH1F("W2000N1000_nc_sub8_mass", "W2000N1000_nc_sub8_mass", 50, 0, 7000)

W2000N1000_nocut_subAK8_pt_2 = TH1F("W2000N1000_nc_sub8_pt_2", "W2000N1000_nc_sub8_pt_2", 50, 0, 7000)
W2000N1000_nocut_subAK8_eta_2 = TH1F("W2000N1000_nc_sub8_eta_2", "W2000N1000_nc_sub8_eta_2", 50,-8, 8)
W2000N1000_nocut_subAK8_mass_2 = TH1F("W2000N1000_nc_sub8_mass_2", "W2000N1000_nc_sub8_mass_2", 50, 0, 7000)

#N
W2000N1000_nocut_N4_el_pt = TH1F("W2000N1000_nc_N4_el_pt", "W2000N1000_nc_N4_el_pt", 50, 0, 7000)
W2000N1000_nocut_N4_el_eta = TH1F("W2000N1000_nc_N4_el_eta", "W2000N1000_nc_N4_el_eta", 50, -8, 8)
W2000N1000_nocut_N4_el_mass = TH1F("W2000N1000_nc_N4_el_mass", "W2000N1000_nc_N4_el_mass", 50, 0, 7000)

W2000N1000_nocut_N4_mu_pt = TH1F("W2000N1000_nc_N4_mu_pt", "W2000N1000_nc_N4_mu_pt", 50, 0, 7000)
W2000N1000_nocut_N4_mu_eta = TH1F("W2000N1000_nc_N4_mu_eta", "W2000N1000_nc_N4_mu_eta", 50, -8, 8)
W2000N1000_nocut_N4_mu_mass = TH1F("W2000N1000_nc_N4_mu_mass", "W2000N1000_nc_N4_mu_mass", 50, 0, 7000)

W2000N1000_nocut_subAK8_el_pt = TH1F("W2000N1000_nc_subN8_el_pt", "W2000N1000_nc_subN8_el_pt" , 50 ,0 ,7000)
W2000N1000_nocut_subAK8_el_eta = TH1F("W2000N1000_nc_subN8_el_eta", "W2000N1000_nc_subN8_el_eta", 50, -8, 8)
W2000N1000_nocut_subAK8_el_mass = TH1F("W2000N1000_nc_subN8_el_mass", "W2000N1000_nc_subN8_el_mass", 50,0,7000)

W2000N1000_nocut_subAK8_mu_pt = TH1F("W2000N1000_nc_subN8_mu_pt", "W2000N1000_nc_subN8_mu_pt", 50, 0, 7000)
W2000N1000_nocut_subAK8_mu_eta = TH1F("W2000N1000_nc_subN8_mu_eta", "W2000N1000_nc_subN8_mu_eta", 50, -8, 8)
W2000N1000_nocut_subAK8_mu_mass = TH1F("W2000N1000_nc_subN8_mu_mass", "W2000N1000_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W2000N1000_nocut_WR4_el_pt = TH1F("W2000N1000_nc_WR4_el_pt", "W2000N1000_nc_WR4_el_pt", 50, 0, 7000)
W2000N1000_nocut_WR4_el_eta = TH1F("W2000N1000_nc_WR4_el_eta", "W2000N1000_nc_WR4_el_eta", 50, -8, 8)
W2000N1000_nocut_WR4_el_mass = TH1F("W2000N1000_nc_WR4_el_mass", "W2000N1000_nc_WR4_el_mass", 50, 0, 7000)

W2000N1000_nocut_WR4_mu_pt = TH1F("W2000N1000_nc_WR4_mu_pt", "W2000N1000_nc_WR4_mu_pt", 50, 0, 7000)
W2000N1000_nocut_WR4_mu_eta = TH1F("W2000N1000_nc_WR4_mu_eta", "W2000N1000_nc_WR4_mu_eta", 50, -8, 8)
W2000N1000_nocut_WR4_mu_mass = TH1F("W2000N1000_nc_WR4_mu_mass", "W2000N1000_nc_WR4_mu_mass", 50, 0, 7000)

W2000N1000_nocut_WR8_pt = TH1F("W2000N1000_nc_WR8_pt", "W2000N1000_nc_WR8_pt",50,0,7000)
W2000N1000_nocut_WR8_eta = TH1F("W2000N1000_nc_WR8_eta","W2000N1000_nc_WR8_eta",50,-8,8)
W2000N1000_nocut_WR8_mass = TH1F("W2000N1000_nc_WR8_mass","W2000N1000_nc_WR8_mass",50,0,7000)

W2000N1000_nocut_subWR8_el_pt = TH1F("W2000N1000_nc_subWR8_el_pt","W2000N1000_nc_subWR8_el_pt",50,0,7000)
W2000N1000_nocut_subWR8_el_eta = TH1F("W2000N1000_nc_subWR8_el_eta","W2000N1000_nc_subWR8_el_eta",50,-8,8)
W2000N1000_nocut_subWR8_el_mass = TH1F("W2000N1000_nc_subWR8_el_mass","W2000N1000_nc_subWR8_el_mass",50,0,7000)

W2000N1000_nocut_subWR8_mu_pt = TH1F("W2000N1000_nc_subWR8_mu_pt","W2000N1000_nc_subWR8_mu_pt",50,0,7000)
W2000N1000_nocut_subWR8_mu_eta = TH1F("W2000N1000_nc_subWR8_mu_eta","W2000N1000_nc_subWR8_mu_eta",50,-8,8)
W2000N1000_nocut_subWR8_mu_mass = TH1F("W2000N1000_nc_subWR8_mu_mass","W2000N1000_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W2000N1000_cut_tau_pt = TH1F("W2000N1000_c_tau_pt","W2000N1000_c_tau_pt", 50, 0,7000)
W2000N1000_cut_tau_eta = TH1F("W2000N1000_c_tau_eta", "W2000N1000_c_tau_eta", 50, -8, 8)
W2000N1000_cut_tau_mass = TH1F("W2000N1000_c_tau_mass", "W2000N1000_c_tau_mass", 50, 0, 7000)

W2000N1000_cut_AK4_pt = TH1F("W2000N1000_c_4_pt", "W2000N1000_c_4_pt", 50, 0, 7000)
W2000N1000_cut_AK4_eta = TH1F("W2000N1000_c_4_eta", "W2000N1000_c_4_eta", 50, -8, 8)
W2000N1000_cut_AK4_mass = TH1F("W2000N1000_c_4_mass", "W2000N1000_c_4_mass", 50, 0, 7000)

W2000N1000_cut_AK4_pt_2 = TH1F("W2000N1000_c_4_pt_2", "W2000N1000_c_4_pt_2", 50, 0, 7000)
W2000N1000_cut_AK4_eta_2 = TH1F("W2000N1000_c_4_eta_2", "W2000N1000_c_4_eta_2", 50, -8, 8)
W2000N1000_cut_AK4_mass_2 = TH1F("W2000N1000_c_4_mass_2", "W2000N1000_c_4_mass_2", 50, 0, 7000)

W2000N1000_cut_AK8_pt = TH1F("W2000N1000_c_8_pt", "W2000N1000_c_8_pt", 50, 0, 7000)
W2000N1000_cut_AK8_eta = TH1F("W2000N1000_c_8_eta", "W2000N1000_c_8_eta", 50, -8, 8)
W2000N1000_cut_AK8_mass = TH1F("W2000N1000_c_8_mass", "W2000N1000_c_8_mass", 50, 0, 7000)

W2000N1000_cut_subAK8_pt = TH1F("W2000N1000_c_sub8_pt", "W2000N1000_c_sub8_pt", 50, 0, 7000)
W2000N1000_cut_subAK8_eta = TH1F("W2000N1000_c_sub8_eta", "W2000N1000_c_sub8_eta", 50,-8, 8)
W2000N1000_cut_subAK8_mass = TH1F("W2000N1000_c_sub8_mass", "W2000N1000_c_sub8_mass", 50, 0, 7000)

W2000N1000_cut_subAK8_pt_2 = TH1F("W2000N1000_c_sub8_pt_2", "W2000N1000_c_sub8_pt_2", 50, 0, 7000)
W2000N1000_cut_subAK8_eta_2 = TH1F("W2000N1000_c_sub8_eta_2", "W2000N1000_c_sub8_eta_2", 50,-8, 8)
W2000N1000_cut_subAK8_mass_2 = TH1F("W2000N1000_c_sub8_mass_2", "W2000N1000_c_sub8_mass_2", 50, 0, 7000)

#N
W2000N1000_cut_N4_el_pt = TH1F("W2000N1000_c_N4_el_pt", "W2000N1000_c_N4_el_pt", 50, 0, 7000)
W2000N1000_cut_N4_el_eta = TH1F("W2000N1000_c_N4_el_eta", "W2000N1000_c_N4_el_eta", 50, -8, 8)
W2000N1000_cut_N4_el_mass = TH1F("W2000N1000_c_N4_el_mass", "W2000N1000_c_N4_el_mass", 50, 0, 7000)

W2000N1000_cut_N4_mu_pt = TH1F("W2000N1000_c_N4_mu_pt", "W2000N1000_c_N4_mu_pt", 50, 0, 7000)
W2000N1000_cut_N4_mu_eta = TH1F("W2000N1000_c_N4_mu_eta", "W2000N1000_c_N4_mu_eta", 50, -8, 8)
W2000N1000_cut_N4_mu_mass = TH1F("W2000N1000_c_N4_mu_mass", "W2000N1000_c_N4_mu_mass", 50, 0, 7000)

W2000N1000_cut_subAK8_el_pt = TH1F("W2000N1000_c_subN8_el_pt", "W2000N1000_c_subN8_el_pt" , 50 ,0 ,7000)
W2000N1000_cut_subAK8_el_eta = TH1F("W2000N1000_c_subN8_el_eta", "W2000N1000_c_subN8_el_eta", 50, -8, 8)
W2000N1000_cut_subAK8_el_mass = TH1F("W2000N1000_c_subN8_el_mass", "W2000N1000_c_subN8_el_mass", 50,0,7000)

W2000N1000_cut_subAK8_mu_pt = TH1F("W2000N1000_c_subN8_mu_pt", "W2000N1000_c_subN8_mu_pt", 50, 0, 7000)
W2000N1000_cut_subAK8_mu_eta = TH1F("W2000N1000_c_subN8_mu_eta", "W2000N1000_c_subN8_mu_eta", 50, -8, 8)
W2000N1000_cut_subAK8_mu_mass = TH1F("W2000N1000_c_subN8_mu_mass", "W2000N1000_c_subN8_mu_mass", 50, 0, 7000)


# wr
W2000N1000_cut_WR4_el_pt = TH1F("W2000N1000_c_WR4_el_pt", "W2000N1000_c_WR4_el_pt", 50, 0, 7000)
W2000N1000_cut_WR4_el_eta = TH1F("W2000N1000_c_WR4_el_eta", "W2000N1000_c_WR4_el_eta", 50, -8, 8)
W2000N1000_cut_WR4_el_mass = TH1F("W2000N1000_c_WR4_el_mass", "W2000N1000_c_WR4_el_mass", 50, 0, 7000)

W2000N1000_cut_WR4_mu_pt = TH1F("W2000N1000_c_WR4_mu_pt", "W2000N1000_c_WR4_mu_pt", 50, 0, 7000)
W2000N1000_cut_WR4_mu_eta = TH1F("W2000N1000_c_WR4_mu_eta", "W2000N1000_c_WR4_mu_eta", 50, -8, 8)
W2000N1000_cut_WR4_mu_mass = TH1F("W2000N1000_c_WR4_mu_mass", "W2000N1000_c_WR4_mu_mass", 50, 0, 7000)

W2000N1000_cut_WR8_pt = TH1F("W2000N1000_c_WR8_pt", "W2000N1000_c_WR8_pt",50,0,7000)
W2000N1000_cut_WR8_eta = TH1F("W2000N1000_c_WR8_eta","W2000N1000_c_WR8_eta",50,-8,8)
W2000N1000_cut_WR8_mass = TH1F("W2000N1000_c_WR8_mass","W2000N1000_c_WR8_mass",50,0,7000)

W2000N1000_cut_subWR8_el_pt = TH1F("W2000N1000_c_subWR8_el_pt","W2000N1000_c_subWR8_el_pt",50,0,7000)
W2000N1000_cut_subWR8_el_eta = TH1F("W2000N1000_c_subWR8_el_eta","W2000N1000_c_subWR8_el_eta",50,-8,8)
W2000N1000_cut_subWR8_el_mass = TH1F("W2000N1000_c_subWR8_el_mass","W2000N1000_c_subWR8_el_mass",50,0,7000)

W2000N1000_cut_subWR8_mu_pt = TH1F("W2000N1000_c_subWR8_mu_pt","W2000N1000_c_subWR8_mu_pt",50,0,7000)
W2000N1000_cut_subWR8_mu_eta = TH1F("W2000N1000_c_subWR8_mu_eta","W2000N1000_c_subWR8_mu_eta",50,-8,8)
W2000N1000_cut_subWR8_mu_mass = TH1F("W2000N1000_c_subWR8_mu_mass","W2000N1000_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################
#################################no####cut################################
W2000N1900_nocut_tau_pt = TH1F("W2000N1900_nc_tau_pt","W2000N1900_nc_tau_pt", 50, 0,7000)
W2000N1900_nocut_tau_eta = TH1F("W2000N1900_nc_tau_eta", "W2000N1900_nc_tau_eta", 50, -8, 8)
W2000N1900_nocut_tau_mass = TH1F("W2000N1900_nc_tau_mass", "W2000N1900_nc_tau_mass", 50, 0, 7000)

W2000N1900_nocut_AK4_pt = TH1F("W2000N1900_nc_4_pt", "W2000N1900_nc_4_pt", 50, 0, 7000)
W2000N1900_nocut_AK4_eta = TH1F("W2000N1900_nc_4_eta", "W2000N1900_nc_4_eta", 50, -8, 8)
W2000N1900_nocut_AK4_mass = TH1F("W2000N1900_nc_4_mass", "W2000N1900_nc_4_mass", 50, 0, 7000)

W2000N1900_nocut_AK4_pt_2 = TH1F("W2000N1900_nc_4_pt_2", "W2000N1900_nc_4_pt_2", 50, 0, 7000)
W2000N1900_nocut_AK4_eta_2 = TH1F("W2000N1900_nc_4_eta_2", "W2000N1900_nc_4_eta_2", 50, -8, 8)
W2000N1900_nocut_AK4_mass_2 = TH1F("W2000N1900_nc_4_mass_2", "W2000N1900_nc_4_mass_2", 50, 0, 7000)

W2000N1900_nocut_AK8_pt = TH1F("W2000N1900_nc_8_pt", "W2000N1900_nc_8_pt", 50, 0, 7000)
W2000N1900_nocut_AK8_eta = TH1F("W2000N1900_nc_8_eta", "W2000N1900_nc_8_eta", 50, -8, 8)
W2000N1900_nocut_AK8_mass = TH1F("W2000N1900_nc_8_mass", "W2000N1900_nc_8_mass", 50, 0, 7000)

W2000N1900_nocut_subAK8_pt = TH1F("W2000N1900_nc_sub8_pt", "W2000N1900_nc_sub8_pt", 50, 0, 7000)
W2000N1900_nocut_subAK8_eta = TH1F("W2000N1900_nc_sub8_eta", "W2000N1900_nc_sub8_eta", 50,-8, 8)
W2000N1900_nocut_subAK8_mass = TH1F("W2000N1900_nc_sub8_mass", "W2000N1900_nc_sub8_mass", 50, 0, 7000)

W2000N1900_nocut_subAK8_pt_2 = TH1F("W2000N1900_nc_sub8_pt_2", "W2000N1900_nc_sub8_pt_2", 50, 0, 7000)
W2000N1900_nocut_subAK8_eta_2 = TH1F("W2000N1900_nc_sub8_eta_2", "W2000N1900_nc_sub8_eta_2", 50,-8, 8)
W2000N1900_nocut_subAK8_mass_2 = TH1F("W2000N1900_nc_sub8_mass_2", "W2000N1900_nc_sub8_mass_2", 50, 0, 7000)

#N
W2000N1900_nocut_N4_el_pt = TH1F("W2000N1900_nc_N4_el_pt", "W2000N1900_nc_N4_el_pt", 50, 0, 7000)
W2000N1900_nocut_N4_el_eta = TH1F("W2000N1900_nc_N4_el_eta", "W2000N1900_nc_N4_el_eta", 50, -8, 8)
W2000N1900_nocut_N4_el_mass = TH1F("W2000N1900_nc_N4_el_mass", "W2000N1900_nc_N4_el_mass", 50, 0, 7000)

W2000N1900_nocut_N4_mu_pt = TH1F("W2000N1900_nc_N4_mu_pt", "W2000N1900_nc_N4_mu_pt", 50, 0, 7000)
W2000N1900_nocut_N4_mu_eta = TH1F("W2000N1900_nc_N4_mu_eta", "W2000N1900_nc_N4_mu_eta", 50, -8, 8)
W2000N1900_nocut_N4_mu_mass = TH1F("W2000N1900_nc_N4_mu_mass", "W2000N1900_nc_N4_mu_mass", 50, 0, 7000)

W2000N1900_nocut_subAK8_el_pt = TH1F("W2000N1900_nc_subN8_el_pt", "W2000N1900_nc_subN8_el_pt" , 50 ,0 ,7000)
W2000N1900_nocut_subAK8_el_eta = TH1F("W2000N1900_nc_subN8_el_eta", "W2000N1900_nc_subN8_el_eta", 50, -8, 8)
W2000N1900_nocut_subAK8_el_mass = TH1F("W2000N1900_nc_subN8_el_mass", "W2000N1900_nc_subN8_el_mass", 50,0,7000)

W2000N1900_nocut_subAK8_mu_pt = TH1F("W2000N1900_nc_subN8_mu_pt", "W2000N1900_nc_subN8_mu_pt", 50, 0, 7000)
W2000N1900_nocut_subAK8_mu_eta = TH1F("W2000N1900_nc_subN8_mu_eta", "W2000N1900_nc_subN8_mu_eta", 50, -8, 8)
W2000N1900_nocut_subAK8_mu_mass = TH1F("W2000N1900_nc_subN8_mu_mass", "W2000N1900_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W2000N1900_nocut_WR4_el_pt = TH1F("W2000N1900_nc_WR4_el_pt", "W2000N1900_nc_WR4_el_pt", 50, 0, 7000)
W2000N1900_nocut_WR4_el_eta = TH1F("W2000N1900_nc_WR4_el_eta", "W2000N1900_nc_WR4_el_eta", 50, -8, 8)
W2000N1900_nocut_WR4_el_mass = TH1F("W2000N1900_nc_WR4_el_mass", "W2000N1900_nc_WR4_el_mass", 50, 0, 7000)

W2000N1900_nocut_WR4_mu_pt = TH1F("W2000N1900_nc_WR4_mu_pt", "W2000N1900_nc_WR4_mu_pt", 50, 0, 7000)
W2000N1900_nocut_WR4_mu_eta = TH1F("W2000N1900_nc_WR4_mu_eta", "W2000N1900_nc_WR4_mu_eta", 50, -8, 8)
W2000N1900_nocut_WR4_mu_mass = TH1F("W2000N1900_nc_WR4_mu_mass", "W2000N1900_nc_WR4_mu_mass", 50, 0, 7000)

W2000N1900_nocut_WR8_pt = TH1F("W2000N1900_nc_WR8_pt", "W2000N1900_nc_WR8_pt",50,0,7000)
W2000N1900_nocut_WR8_eta = TH1F("W2000N1900_nc_WR8_eta","W2000N1900_nc_WR8_eta",50,-8,8)
W2000N1900_nocut_WR8_mass = TH1F("W2000N1900_nc_WR8_mass","W2000N1900_nc_WR8_mass",50,0,7000)

W2000N1900_nocut_subWR8_el_pt = TH1F("W2000N1900_nc_subWR8_el_pt","W2000N1900_nc_subWR8_el_pt",50,0,7000)
W2000N1900_nocut_subWR8_el_eta = TH1F("W2000N1900_nc_subWR8_el_eta","W2000N1900_nc_subWR8_el_eta",50,-8,8)
W2000N1900_nocut_subWR8_el_mass = TH1F("W2000N1900_nc_subWR8_el_mass","W2000N1900_nc_subWR8_el_mass",50,0,7000)

W2000N1900_nocut_subWR8_mu_pt = TH1F("W2000N1900_nc_subWR8_mu_pt","W2000N1900_nc_subWR8_mu_pt",50,0,7000)
W2000N1900_nocut_subWR8_mu_eta = TH1F("W2000N1900_nc_subWR8_mu_eta","W2000N1900_nc_subWR8_mu_eta",50,-8,8)
W2000N1900_nocut_subWR8_mu_mass = TH1F("W2000N1900_nc_subWR8_mu_mass","W2000N1900_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W2000N1900_cut_tau_pt = TH1F("W2000N1900_c_tau_pt","W2000N1900_c_tau_pt", 50, 0,7000)
W2000N1900_cut_tau_eta = TH1F("W2000N1900_c_tau_eta", "W2000N1900_c_tau_eta", 50, -8, 8)
W2000N1900_cut_tau_mass = TH1F("W2000N1900_c_tau_mass", "W2000N1900_c_tau_mass", 50, 0, 7000)

W2000N1900_cut_AK4_pt = TH1F("W2000N1900_c_4_pt", "W2000N1900_c_4_pt", 50, 0, 7000)
W2000N1900_cut_AK4_eta = TH1F("W2000N1900_c_4_eta", "W2000N1900_c_4_eta", 50, -8, 8)
W2000N1900_cut_AK4_mass = TH1F("W2000N1900_c_4_mass", "W2000N1900_c_4_mass", 50, 0, 7000)

W2000N1900_cut_AK4_pt_2 = TH1F("W2000N1900_c_4_pt_2", "W2000N1900_c_4_pt_2", 50, 0, 7000)
W2000N1900_cut_AK4_eta_2 = TH1F("W2000N1900_c_4_eta_2", "W2000N1900_c_4_eta_2", 50, -8, 8)
W2000N1900_cut_AK4_mass_2 = TH1F("W2000N1900_c_4_mass_2", "W2000N1900_c_4_mass_2", 50, 0, 7000)

W2000N1900_cut_AK8_pt = TH1F("W2000N1900_c_8_pt", "W2000N1900_c_8_pt", 50, 0, 7000)
W2000N1900_cut_AK8_eta = TH1F("W2000N1900_c_8_eta", "W2000N1900_c_8_eta", 50, -8, 8)
W2000N1900_cut_AK8_mass = TH1F("W2000N1900_c_8_mass", "W2000N1900_c_8_mass", 50, 0, 7000)

W2000N1900_cut_subAK8_pt = TH1F("W2000N1900_c_sub8_pt", "W2000N1900_c_sub8_pt", 50, 0, 7000)
W2000N1900_cut_subAK8_eta = TH1F("W2000N1900_c_sub8_eta", "W2000N1900_c_sub8_eta", 50,-8, 8)
W2000N1900_cut_subAK8_mass = TH1F("W2000N1900_c_sub8_mass", "W2000N1900_c_sub8_mass", 50, 0, 7000)

W2000N1900_cut_subAK8_pt_2 = TH1F("W2000N1900_c_sub8_pt_2", "W2000N1900_c_sub8_pt_2", 50, 0, 7000)
W2000N1900_cut_subAK8_eta_2 = TH1F("W2000N1900_c_sub8_eta_2", "W2000N1900_c_sub8_eta_2", 50,-8, 8)
W2000N1900_cut_subAK8_mass_2 = TH1F("W2000N1900_c_sub8_mass_2", "W2000N1900_c_sub8_mass_2", 50, 0, 7000)

#N
W2000N1900_cut_N4_el_pt = TH1F("W2000N1900_c_N4_el_pt", "W2000N1900_c_N4_el_pt", 50, 0, 7000)
W2000N1900_cut_N4_el_eta = TH1F("W2000N1900_c_N4_el_eta", "W2000N1900_c_N4_el_eta", 50, -8, 8)
W2000N1900_cut_N4_el_mass = TH1F("W2000N1900_c_N4_el_mass", "W2000N1900_c_N4_el_mass", 50, 0, 7000)

W2000N1900_cut_N4_mu_pt = TH1F("W2000N1900_c_N4_mu_pt", "W2000N1900_c_N4_mu_pt", 50, 0, 7000)
W2000N1900_cut_N4_mu_eta = TH1F("W2000N1900_c_N4_mu_eta", "W2000N1900_c_N4_mu_eta", 50, -8, 8)
W2000N1900_cut_N4_mu_mass = TH1F("W2000N1900_c_N4_mu_mass", "W2000N1900_c_N4_mu_mass", 50, 0, 7000)

W2000N1900_cut_subAK8_el_pt = TH1F("W2000N1900_c_subN8_el_pt", "W2000N1900_c_subN8_el_pt" , 50 ,0 ,7000)
W2000N1900_cut_subAK8_el_eta = TH1F("W2000N1900_c_subN8_el_eta", "W2000N1900_c_subN8_el_eta", 50, -8, 8)
W2000N1900_cut_subAK8_el_mass = TH1F("W2000N1900_c_subN8_el_mass", "W2000N1900_c_subN8_el_mass", 50,0,7000)

W2000N1900_cut_subAK8_mu_pt = TH1F("W2000N1900_c_subN8_mu_pt", "W2000N1900_c_subN8_mu_pt", 50, 0, 7000)
W2000N1900_cut_subAK8_mu_eta = TH1F("W2000N1900_c_subN8_mu_eta", "W2000N1900_c_subN8_mu_eta", 50, -8, 8)
W2000N1900_cut_subAK8_mu_mass = TH1F("W2000N1900_c_subN8_mu_mass", "W2000N1900_c_subN8_mu_mass", 50, 0, 7000)


# wr
W2000N1900_cut_WR4_el_pt = TH1F("W2000N1900_c_WR4_el_pt", "W2000N1900_c_WR4_el_pt", 50, 0, 7000)
W2000N1900_cut_WR4_el_eta = TH1F("W2000N1900_c_WR4_el_eta", "W2000N1900_c_WR4_el_eta", 50, -8, 8)
W2000N1900_cut_WR4_el_mass = TH1F("W2000N1900_c_WR4_el_mass", "W2000N1900_c_WR4_el_mass", 50, 0, 7000)

W2000N1900_cut_WR4_mu_pt = TH1F("W2000N1900_c_WR4_mu_pt", "W2000N1900_c_WR4_mu_pt", 50, 0, 7000)
W2000N1900_cut_WR4_mu_eta = TH1F("W2000N1900_c_WR4_mu_eta", "W2000N1900_c_WR4_mu_eta", 50, -8, 8)
W2000N1900_cut_WR4_mu_mass = TH1F("W2000N1900_c_WR4_mu_mass", "W2000N1900_c_WR4_mu_mass", 50, 0, 7000)

W2000N1900_cut_WR8_pt = TH1F("W2000N1900_c_WR8_pt", "W2000N1900_c_WR8_pt",50,0,7000)
W2000N1900_cut_WR8_eta = TH1F("W2000N1900_c_WR8_eta","W2000N1900_c_WR8_eta",50,-8,8)
W2000N1900_cut_WR8_mass = TH1F("W2000N1900_c_WR8_mass","W2000N1900_c_WR8_mass",50,0,7000)

W2000N1900_cut_subWR8_el_pt = TH1F("W2000N1900_c_subWR8_el_pt","W2000N1900_c_subWR8_el_pt",50,0,7000)
W2000N1900_cut_subWR8_el_eta = TH1F("W2000N1900_c_subWR8_el_eta","W2000N1900_c_subWR8_el_eta",50,-8,8)
W2000N1900_cut_subWR8_el_mass = TH1F("W2000N1900_c_subWR8_el_mass","W2000N1900_c_subWR8_el_mass",50,0,7000)

W2000N1900_cut_subWR8_mu_pt = TH1F("W2000N1900_c_subWR8_mu_pt","W2000N1900_c_subWR8_mu_pt",50,0,7000)
W2000N1900_cut_subWR8_mu_eta = TH1F("W2000N1900_c_subWR8_mu_eta","W2000N1900_c_subWR8_mu_eta",50,-8,8)
W2000N1900_cut_subWR8_mu_mass = TH1F("W2000N1900_c_subWR8_mu_mass","W2000N1900_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################
#################################no####cut################################
W4000N100_nocut_tau_pt = TH1F("W4000N100_nc_tau_pt","W4000N100_nc_tau_pt", 50, 0,7000)
W4000N100_nocut_tau_eta = TH1F("W4000N100_nc_tau_eta", "W4000N100_nc_tau_eta", 50, -8, 8)
W4000N100_nocut_tau_mass = TH1F("W4000N100_nc_tau_mass", "W4000N100_nc_tau_mass", 50, 0, 7000)

W4000N100_nocut_AK4_pt = TH1F("W4000N100_nc_4_pt", "W4000N100_nc_4_pt", 50, 0, 7000)
W4000N100_nocut_AK4_eta = TH1F("W4000N100_nc_4_eta", "W4000N100_nc_4_eta", 50, -8, 8)
W4000N100_nocut_AK4_mass = TH1F("W4000N100_nc_4_mass", "W4000N100_nc_4_mass", 50, 0, 7000)

W4000N100_nocut_AK4_pt_2 = TH1F("W4000N100_nc_4_pt_2", "W4000N100_nc_4_pt_2", 50, 0, 7000)
W4000N100_nocut_AK4_eta_2 = TH1F("W4000N100_nc_4_eta_2", "W4000N100_nc_4_eta_2", 50, -8, 8)
W4000N100_nocut_AK4_mass_2 = TH1F("W4000N100_nc_4_mass_2", "W4000N100_nc_4_mass_2", 50, 0, 7000)

W4000N100_nocut_AK8_pt = TH1F("W4000N100_nc_8_pt", "W4000N100_nc_8_pt", 50, 0, 7000)
W4000N100_nocut_AK8_eta = TH1F("W4000N100_nc_8_eta", "W4000N100_nc_8_eta", 50, -8, 8)
W4000N100_nocut_AK8_mass = TH1F("W4000N100_nc_8_mass", "W4000N100_nc_8_mass", 50, 0, 7000)

W4000N100_nocut_subAK8_pt = TH1F("W4000N100_nc_sub8_pt", "W4000N100_nc_sub8_pt", 50, 0, 7000)
W4000N100_nocut_subAK8_eta = TH1F("W4000N100_nc_sub8_eta", "W4000N100_nc_sub8_eta", 50,-8, 8)
W4000N100_nocut_subAK8_mass = TH1F("W4000N100_nc_sub8_mass", "W4000N100_nc_sub8_mass", 50, 0, 7000)

W4000N100_nocut_subAK8_pt_2 = TH1F("W4000N100_nc_sub8_pt_2", "W4000N100_nc_sub8_pt_2", 50, 0, 7000)
W4000N100_nocut_subAK8_eta_2 = TH1F("W4000N100_nc_sub8_eta_2", "W4000N100_nc_sub8_eta_2", 50,-8, 8)
W4000N100_nocut_subAK8_mass_2 = TH1F("W4000N100_nc_sub8_mass_2", "W4000N100_nc_sub8_mass_2", 50, 0, 7000)

#N
W4000N100_nocut_N4_el_pt = TH1F("W4000N100_nc_N4_el_pt", "W4000N100_nc_N4_el_pt", 50, 0, 7000)
W4000N100_nocut_N4_el_eta = TH1F("W4000N100_nc_N4_el_eta", "W4000N100_nc_N4_el_eta", 50, -8, 8)
W4000N100_nocut_N4_el_mass = TH1F("W4000N100_nc_N4_el_mass", "W4000N100_nc_N4_el_mass", 50, 0, 7000)

W4000N100_nocut_N4_mu_pt = TH1F("W4000N100_nc_N4_mu_pt", "W4000N100_nc_N4_mu_pt", 50, 0, 7000)
W4000N100_nocut_N4_mu_eta = TH1F("W4000N100_nc_N4_mu_eta", "W4000N100_nc_N4_mu_eta", 50, -8, 8)
W4000N100_nocut_N4_mu_mass = TH1F("W4000N100_nc_N4_mu_mass", "W4000N100_nc_N4_mu_mass", 50, 0, 7000)

W4000N100_nocut_subAK8_el_pt = TH1F("W4000N100_nc_subN8_el_pt", "W4000N100_nc_subN8_el_pt" , 50 ,0 ,7000)
W4000N100_nocut_subAK8_el_eta = TH1F("W4000N100_nc_subN8_el_eta", "W4000N100_nc_subN8_el_eta", 50, -8, 8)
W4000N100_nocut_subAK8_el_mass = TH1F("W4000N100_nc_subN8_el_mass", "W4000N100_nc_subN8_el_mass", 50,0,7000)

W4000N100_nocut_subAK8_mu_pt = TH1F("W4000N100_nc_subN8_mu_pt", "W4000N100_nc_subN8_mu_pt", 50, 0, 7000)
W4000N100_nocut_subAK8_mu_eta = TH1F("W4000N100_nc_subN8_mu_eta", "W4000N100_nc_subN8_mu_eta", 50, -8, 8)
W4000N100_nocut_subAK8_mu_mass = TH1F("W4000N100_nc_subN8_mu_mass", "W4000N100_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W4000N100_nocut_WR4_el_pt = TH1F("W4000N100_nc_WR4_el_pt", "W4000N100_nc_WR4_el_pt", 50, 0, 7000)
W4000N100_nocut_WR4_el_eta = TH1F("W4000N100_nc_WR4_el_eta", "W4000N100_nc_WR4_el_eta", 50, -8, 8)
W4000N100_nocut_WR4_el_mass = TH1F("W4000N100_nc_WR4_el_mass", "W4000N100_nc_WR4_el_mass", 50, 0, 7000)

W4000N100_nocut_WR4_mu_pt = TH1F("W4000N100_nc_WR4_mu_pt", "W4000N100_nc_WR4_mu_pt", 50, 0, 7000)
W4000N100_nocut_WR4_mu_eta = TH1F("W4000N100_nc_WR4_mu_eta", "W4000N100_nc_WR4_mu_eta", 50, -8, 8)
W4000N100_nocut_WR4_mu_mass = TH1F("W4000N100_nc_WR4_mu_mass", "W4000N100_nc_WR4_mu_mass", 50, 0, 7000)

W4000N100_nocut_WR8_pt = TH1F("W4000N100_nc_WR8_pt", "W4000N100_nc_WR8_pt",50,0,7000)
W4000N100_nocut_WR8_eta = TH1F("W4000N100_nc_WR8_eta","W4000N100_nc_WR8_eta",50,-8,8)
W4000N100_nocut_WR8_mass = TH1F("W4000N100_nc_WR8_mass","W4000N100_nc_WR8_mass",50,0,7000)

W4000N100_nocut_subWR8_el_pt = TH1F("W4000N100_nc_subWR8_el_pt","W4000N100_nc_subWR8_el_pt",50,0,7000)
W4000N100_nocut_subWR8_el_eta = TH1F("W4000N100_nc_subWR8_el_eta","W4000N100_nc_subWR8_el_eta",50,-8,8)
W4000N100_nocut_subWR8_el_mass = TH1F("W4000N100_nc_subWR8_el_mass","W4000N100_nc_subWR8_el_mass",50,0,7000)

W4000N100_nocut_subWR8_mu_pt = TH1F("W4000N100_nc_subWR8_mu_pt","W4000N100_nc_subWR8_mu_pt",50,0,7000)
W4000N100_nocut_subWR8_mu_eta = TH1F("W4000N100_nc_subWR8_mu_eta","W4000N100_nc_subWR8_mu_eta",50,-8,8)
W4000N100_nocut_subWR8_mu_mass = TH1F("W4000N100_nc_subWR8_mu_mass","W4000N100_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W4000N100_cut_tau_pt = TH1F("W4000N100_c_tau_pt","W4000N100_c_tau_pt", 50, 0,7000)
W4000N100_cut_tau_eta = TH1F("W4000N100_c_tau_eta", "W4000N100_c_tau_eta", 50, -8, 8)
W4000N100_cut_tau_mass = TH1F("W4000N100_c_tau_mass", "W4000N100_c_tau_mass", 50, 0, 7000)

W4000N100_cut_AK4_pt = TH1F("W4000N100_c_4_pt", "W4000N100_c_4_pt", 50, 0, 7000)
W4000N100_cut_AK4_eta = TH1F("W4000N100_c_4_eta", "W4000N100_c_4_eta", 50, -8, 8)
W4000N100_cut_AK4_mass = TH1F("W4000N100_c_4_mass", "W4000N100_c_4_mass", 50, 0, 7000)

W4000N100_cut_AK4_pt_2 = TH1F("W4000N100_c_4_pt_2", "W4000N100_c_4_pt_2", 50, 0, 7000)
W4000N100_cut_AK4_eta_2 = TH1F("W4000N100_c_4_eta_2", "W4000N100_c_4_eta_2", 50, -8, 8)
W4000N100_cut_AK4_mass_2 = TH1F("W4000N100_c_4_mass_2", "W4000N100_c_4_mass_2", 50, 0, 7000)

W4000N100_cut_AK8_pt = TH1F("W4000N100_c_8_pt", "W4000N100_c_8_pt", 50, 0, 7000)
W4000N100_cut_AK8_eta = TH1F("W4000N100_c_8_eta", "W4000N100_c_8_eta", 50, -8, 8)
W4000N100_cut_AK8_mass = TH1F("W4000N100_c_8_mass", "W4000N100_c_8_mass", 50, 0, 7000)

W4000N100_cut_subAK8_pt = TH1F("W4000N100_c_sub8_pt", "W4000N100_c_sub8_pt", 50, 0, 7000)
W4000N100_cut_subAK8_eta = TH1F("W4000N100_c_sub8_eta", "W4000N100_c_sub8_eta", 50,-8, 8)
W4000N100_cut_subAK8_mass = TH1F("W4000N100_c_sub8_mass", "W4000N100_c_sub8_mass", 50, 0, 7000)

W4000N100_cut_subAK8_pt_2 = TH1F("W4000N100_c_sub8_pt_2", "W4000N100_c_sub8_pt_2", 50, 0, 7000)
W4000N100_cut_subAK8_eta_2 = TH1F("W4000N100_c_sub8_eta_2", "W4000N100_c_sub8_eta_2", 50,-8, 8)
W4000N100_cut_subAK8_mass_2 = TH1F("W4000N100_c_sub8_mass_2", "W4000N100_c_sub8_mass_2", 50, 0, 7000)

#N
W4000N100_cut_N4_el_pt = TH1F("W4000N100_c_N4_el_pt", "W4000N100_c_N4_el_pt", 50, 0, 7000)
W4000N100_cut_N4_el_eta = TH1F("W4000N100_c_N4_el_eta", "W4000N100_c_N4_el_eta", 50, -8, 8)
W4000N100_cut_N4_el_mass = TH1F("W4000N100_c_N4_el_mass", "W4000N100_c_N4_el_mass", 50, 0, 7000)

W4000N100_cut_N4_mu_pt = TH1F("W4000N100_c_N4_mu_pt", "W4000N100_c_N4_mu_pt", 50, 0, 7000)
W4000N100_cut_N4_mu_eta = TH1F("W4000N100_c_N4_mu_eta", "W4000N100_c_N4_mu_eta", 50, -8, 8)
W4000N100_cut_N4_mu_mass = TH1F("W4000N100_c_N4_mu_mass", "W4000N100_c_N4_mu_mass", 50, 0, 7000)

W4000N100_cut_subAK8_el_pt = TH1F("W4000N100_c_subN8_el_pt", "W4000N100_c_subN8_el_pt" , 50 ,0 ,7000)
W4000N100_cut_subAK8_el_eta = TH1F("W4000N100_c_subN8_el_eta", "W4000N100_c_subN8_el_eta", 50, -8, 8)
W4000N100_cut_subAK8_el_mass = TH1F("W4000N100_c_subN8_el_mass", "W4000N100_c_subN8_el_mass", 50,0,7000)

W4000N100_cut_subAK8_mu_pt = TH1F("W4000N100_c_subN8_mu_pt", "W4000N100_c_subN8_mu_pt", 50, 0, 7000)
W4000N100_cut_subAK8_mu_eta = TH1F("W4000N100_c_subN8_mu_eta", "W4000N100_c_subN8_mu_eta", 50, -8, 8)
W4000N100_cut_subAK8_mu_mass = TH1F("W4000N100_c_subN8_mu_mass", "W4000N100_c_subN8_mu_mass", 50, 0, 7000)


# wr
W4000N100_cut_WR4_el_pt = TH1F("W4000N100_c_WR4_el_pt", "W4000N100_c_WR4_el_pt", 50, 0, 7000)
W4000N100_cut_WR4_el_eta = TH1F("W4000N100_c_WR4_el_eta", "W4000N100_c_WR4_el_eta", 50, -8, 8)
W4000N100_cut_WR4_el_mass = TH1F("W4000N100_c_WR4_el_mass", "W4000N100_c_WR4_el_mass", 50, 0, 7000)

W4000N100_cut_WR4_mu_pt = TH1F("W4000N100_c_WR4_mu_pt", "W4000N100_c_WR4_mu_pt", 50, 0, 7000)
W4000N100_cut_WR4_mu_eta = TH1F("W4000N100_c_WR4_mu_eta", "W4000N100_c_WR4_mu_eta", 50, -8, 8)
W4000N100_cut_WR4_mu_mass = TH1F("W4000N100_c_WR4_mu_mass", "W4000N100_c_WR4_mu_mass", 50, 0, 7000)

W4000N100_cut_WR8_pt = TH1F("W4000N100_c_WR8_pt", "W4000N100_c_WR8_pt",50,0,7000)
W4000N100_cut_WR8_eta = TH1F("W4000N100_c_WR8_eta","W4000N100_c_WR8_eta",50,-8,8)
W4000N100_cut_WR8_mass = TH1F("W4000N100_c_WR8_mass","W4000N100_c_WR8_mass",50,0,7000)

W4000N100_cut_subWR8_el_pt = TH1F("W4000N100_c_subWR8_el_pt","W4000N100_c_subWR8_el_pt",50,0,7000)
W4000N100_cut_subWR8_el_eta = TH1F("W4000N100_c_subWR8_el_eta","W4000N100_c_subWR8_el_eta",50,-8,8)
W4000N100_cut_subWR8_el_mass = TH1F("W4000N100_c_subWR8_el_mass","W4000N100_c_subWR8_el_mass",50,0,7000)

W4000N100_cut_subWR8_mu_pt = TH1F("W4000N100_c_subWR8_mu_pt","W4000N100_c_subWR8_mu_pt",50,0,7000)
W4000N100_cut_subWR8_mu_eta = TH1F("W4000N100_c_subWR8_mu_eta","W4000N100_c_subWR8_mu_eta",50,-8,8)
W4000N100_cut_subWR8_mu_mass = TH1F("W4000N100_c_subWR8_mu_mass","W4000N100_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################
#################################no####cut################################
W4000N2000_nocut_tau_pt = TH1F("W4000N2000_nc_tau_pt","W4000N2000_nc_tau_pt", 50, 0,7000)
W4000N2000_nocut_tau_eta = TH1F("W4000N2000_nc_tau_eta", "W4000N2000_nc_tau_eta", 50, -8, 8)
W4000N2000_nocut_tau_mass = TH1F("W4000N2000_nc_tau_mass", "W4000N2000_nc_tau_mass", 50, 0, 7000)

W4000N2000_nocut_AK4_pt = TH1F("W4000N2000_nc_4_pt", "W4000N2000_nc_4_pt", 50, 0, 7000)
W4000N2000_nocut_AK4_eta = TH1F("W4000N2000_nc_4_eta", "W4000N2000_nc_4_eta", 50, -8, 8)
W4000N2000_nocut_AK4_mass = TH1F("W4000N2000_nc_4_mass", "W4000N2000_nc_4_mass", 50, 0, 7000)

W4000N2000_nocut_AK4_pt_2 = TH1F("W4000N2000_nc_4_pt_2", "W4000N2000_nc_4_pt_2", 50, 0, 7000)
W4000N2000_nocut_AK4_eta_2 = TH1F("W4000N2000_nc_4_eta_2", "W4000N2000_nc_4_eta_2", 50, -8, 8)
W4000N2000_nocut_AK4_mass_2 = TH1F("W4000N2000_nc_4_mass_2", "W4000N2000_nc_4_mass_2", 50, 0, 7000)

W4000N2000_nocut_AK8_pt = TH1F("W4000N2000_nc_8_pt", "W4000N2000_nc_8_pt", 50, 0, 7000)
W4000N2000_nocut_AK8_eta = TH1F("W4000N2000_nc_8_eta", "W4000N2000_nc_8_eta", 50, -8, 8)
W4000N2000_nocut_AK8_mass = TH1F("W4000N2000_nc_8_mass", "W4000N2000_nc_8_mass", 50, 0, 7000)

W4000N2000_nocut_subAK8_pt = TH1F("W4000N2000_nc_sub8_pt", "W4000N2000_nc_sub8_pt", 50, 0, 7000)
W4000N2000_nocut_subAK8_eta = TH1F("W4000N2000_nc_sub8_eta", "W4000N2000_nc_sub8_eta", 50,-8, 8)
W4000N2000_nocut_subAK8_mass = TH1F("W4000N2000_nc_sub8_mass", "W4000N2000_nc_sub8_mass", 50, 0, 7000)

W4000N2000_nocut_subAK8_pt_2 = TH1F("W4000N2000_nc_sub8_pt_2", "W4000N2000_nc_sub8_pt_2", 50, 0, 7000)
W4000N2000_nocut_subAK8_eta_2 = TH1F("W4000N2000_nc_sub8_eta_2", "W4000N2000_nc_sub8_eta_2", 50,-8, 8)
W4000N2000_nocut_subAK8_mass_2 = TH1F("W4000N2000_nc_sub8_mass_2", "W4000N2000_nc_sub8_mass_2", 50, 0, 7000)

#N
W4000N2000_nocut_N4_el_pt = TH1F("W4000N2000_nc_N4_el_pt", "W4000N2000_nc_N4_el_pt", 50, 0, 7000)
W4000N2000_nocut_N4_el_eta = TH1F("W4000N2000_nc_N4_el_eta", "W4000N2000_nc_N4_el_eta", 50, -8, 8)
W4000N2000_nocut_N4_el_mass = TH1F("W4000N2000_nc_N4_el_mass", "W4000N2000_nc_N4_el_mass", 50, 0, 7000)

W4000N2000_nocut_N4_mu_pt = TH1F("W4000N2000_nc_N4_mu_pt", "W4000N2000_nc_N4_mu_pt", 50, 0, 7000)
W4000N2000_nocut_N4_mu_eta = TH1F("W4000N2000_nc_N4_mu_eta", "W4000N2000_nc_N4_mu_eta", 50, -8, 8)
W4000N2000_nocut_N4_mu_mass = TH1F("W4000N2000_nc_N4_mu_mass", "W4000N2000_nc_N4_mu_mass", 50, 0, 7000)

W4000N2000_nocut_subAK8_el_pt = TH1F("W4000N2000_nc_subN8_el_pt", "W4000N2000_nc_subN8_el_pt" , 50 ,0 ,7000)
W4000N2000_nocut_subAK8_el_eta = TH1F("W4000N2000_nc_subN8_el_eta", "W4000N2000_nc_subN8_el_eta", 50, -8, 8)
W4000N2000_nocut_subAK8_el_mass = TH1F("W4000N2000_nc_subN8_el_mass", "W4000N2000_nc_subN8_el_mass", 50,0,7000)

W4000N2000_nocut_subAK8_mu_pt = TH1F("W4000N2000_nc_subN8_mu_pt", "W4000N2000_nc_subN8_mu_pt", 50, 0, 7000)
W4000N2000_nocut_subAK8_mu_eta = TH1F("W4000N2000_nc_subN8_mu_eta", "W4000N2000_nc_subN8_mu_eta", 50, -8, 8)
W4000N2000_nocut_subAK8_mu_mass = TH1F("W4000N2000_nc_subN8_mu_mass", "W4000N2000_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W4000N2000_nocut_WR4_el_pt = TH1F("W4000N2000_nc_WR4_el_pt", "W4000N2000_nc_WR4_el_pt", 50, 0, 7000)
W4000N2000_nocut_WR4_el_eta = TH1F("W4000N2000_nc_WR4_el_eta", "W4000N2000_nc_WR4_el_eta", 50, -8, 8)
W4000N2000_nocut_WR4_el_mass = TH1F("W4000N2000_nc_WR4_el_mass", "W4000N2000_nc_WR4_el_mass", 50, 0, 7000)

W4000N2000_nocut_WR4_mu_pt = TH1F("W4000N2000_nc_WR4_mu_pt", "W4000N2000_nc_WR4_mu_pt", 50, 0, 7000)
W4000N2000_nocut_WR4_mu_eta = TH1F("W4000N2000_nc_WR4_mu_eta", "W4000N2000_nc_WR4_mu_eta", 50, -8, 8)
W4000N2000_nocut_WR4_mu_mass = TH1F("W4000N2000_nc_WR4_mu_mass", "W4000N2000_nc_WR4_mu_mass", 50, 0, 7000)

W4000N2000_nocut_WR8_pt = TH1F("W4000N2000_nc_WR8_pt", "W4000N2000_nc_WR8_pt",50,0,7000)
W4000N2000_nocut_WR8_eta = TH1F("W4000N2000_nc_WR8_eta","W4000N2000_nc_WR8_eta",50,-8,8)
W4000N2000_nocut_WR8_mass = TH1F("W4000N2000_nc_WR8_mass","W4000N2000_nc_WR8_mass",50,0,7000)

W4000N2000_nocut_subWR8_el_pt = TH1F("W4000N2000_nc_subWR8_el_pt","W4000N2000_nc_subWR8_el_pt",50,0,7000)
W4000N2000_nocut_subWR8_el_eta = TH1F("W4000N2000_nc_subWR8_el_eta","W4000N2000_nc_subWR8_el_eta",50,-8,8)
W4000N2000_nocut_subWR8_el_mass = TH1F("W4000N2000_nc_subWR8_el_mass","W4000N2000_nc_subWR8_el_mass",50,0,7000)

W4000N2000_nocut_subWR8_mu_pt = TH1F("W4000N2000_nc_subWR8_mu_pt","W4000N2000_nc_subWR8_mu_pt",50,0,7000)
W4000N2000_nocut_subWR8_mu_eta = TH1F("W4000N2000_nc_subWR8_mu_eta","W4000N2000_nc_subWR8_mu_eta",50,-8,8)
W4000N2000_nocut_subWR8_mu_mass = TH1F("W4000N2000_nc_subWR8_mu_mass","W4000N2000_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W4000N2000_cut_tau_pt = TH1F("W4000N2000_c_tau_pt","W4000N2000_c_tau_pt", 50, 0,7000)
W4000N2000_cut_tau_eta = TH1F("W4000N2000_c_tau_eta", "W4000N2000_c_tau_eta", 50, -8, 8)
W4000N2000_cut_tau_mass = TH1F("W4000N2000_c_tau_mass", "W4000N2000_c_tau_mass", 50, 0, 7000)

W4000N2000_cut_AK4_pt = TH1F("W4000N2000_c_4_pt", "W4000N2000_c_4_pt", 50, 0, 7000)
W4000N2000_cut_AK4_eta = TH1F("W4000N2000_c_4_eta", "W4000N2000_c_4_eta", 50, -8, 8)
W4000N2000_cut_AK4_mass = TH1F("W4000N2000_c_4_mass", "W4000N2000_c_4_mass", 50, 0, 7000)

W4000N2000_cut_AK4_pt_2 = TH1F("W4000N2000_c_4_pt_2", "W4000N2000_c_4_pt_2", 50, 0, 7000)
W4000N2000_cut_AK4_eta_2 = TH1F("W4000N2000_c_4_eta_2", "W4000N2000_c_4_eta_2", 50, -8, 8)
W4000N2000_cut_AK4_mass_2 = TH1F("W4000N2000_c_4_mass_2", "W4000N2000_c_4_mass_2", 50, 0, 7000)

W4000N2000_cut_AK8_pt = TH1F("W4000N2000_c_8_pt", "W4000N2000_c_8_pt", 50, 0, 7000)
W4000N2000_cut_AK8_eta = TH1F("W4000N2000_c_8_eta", "W4000N2000_c_8_eta", 50, -8, 8)
W4000N2000_cut_AK8_mass = TH1F("W4000N2000_c_8_mass", "W4000N2000_c_8_mass", 50, 0, 7000)

W4000N2000_cut_subAK8_pt = TH1F("W4000N2000_c_sub8_pt", "W4000N2000_c_sub8_pt", 50, 0, 7000)
W4000N2000_cut_subAK8_eta = TH1F("W4000N2000_c_sub8_eta", "W4000N2000_c_sub8_eta", 50,-8, 8)
W4000N2000_cut_subAK8_mass = TH1F("W4000N2000_c_sub8_mass", "W4000N2000_c_sub8_mass", 50, 0, 7000)

W4000N2000_cut_subAK8_pt_2 = TH1F("W4000N2000_c_sub8_pt_2", "W4000N2000_c_sub8_pt_2", 50, 0, 7000)
W4000N2000_cut_subAK8_eta_2 = TH1F("W4000N2000_c_sub8_eta_2", "W4000N2000_c_sub8_eta_2", 50,-8, 8)
W4000N2000_cut_subAK8_mass_2 = TH1F("W4000N2000_c_sub8_mass_2", "W4000N2000_c_sub8_mass_2", 50, 0, 7000)

#N
W4000N2000_cut_N4_el_pt = TH1F("W4000N2000_c_N4_el_pt", "W4000N2000_c_N4_el_pt", 50, 0, 7000)
W4000N2000_cut_N4_el_eta = TH1F("W4000N2000_c_N4_el_eta", "W4000N2000_c_N4_el_eta", 50, -8, 8)
W4000N2000_cut_N4_el_mass = TH1F("W4000N2000_c_N4_el_mass", "W4000N2000_c_N4_el_mass", 50, 0, 7000)

W4000N2000_cut_N4_mu_pt = TH1F("W4000N2000_c_N4_mu_pt", "W4000N2000_c_N4_mu_pt", 50, 0, 7000)
W4000N2000_cut_N4_mu_eta = TH1F("W4000N2000_c_N4_mu_eta", "W4000N2000_c_N4_mu_eta", 50, -8, 8)
W4000N2000_cut_N4_mu_mass = TH1F("W4000N2000_c_N4_mu_mass", "W4000N2000_c_N4_mu_mass", 50, 0, 7000)

W4000N2000_cut_subAK8_el_pt = TH1F("W4000N2000_c_subN8_el_pt", "W4000N2000_c_subN8_el_pt" , 50 ,0 ,7000)
W4000N2000_cut_subAK8_el_eta = TH1F("W4000N2000_c_subN8_el_eta", "W4000N2000_c_subN8_el_eta", 50, -8, 8)
W4000N2000_cut_subAK8_el_mass = TH1F("W4000N2000_c_subN8_el_mass", "W4000N2000_c_subN8_el_mass", 50,0,7000)

W4000N2000_cut_subAK8_mu_pt = TH1F("W4000N2000_c_subN8_mu_pt", "W4000N2000_c_subN8_mu_pt", 50, 0, 7000)
W4000N2000_cut_subAK8_mu_eta = TH1F("W4000N2000_c_subN8_mu_eta", "W4000N2000_c_subN8_mu_eta", 50, -8, 8)
W4000N2000_cut_subAK8_mu_mass = TH1F("W4000N2000_c_subN8_mu_mass", "W4000N2000_c_subN8_mu_mass", 50, 0, 7000)


# wr
W4000N2000_cut_WR4_el_pt = TH1F("W4000N2000_c_WR4_el_pt", "W4000N2000_c_WR4_el_pt", 50, 0, 7000)
W4000N2000_cut_WR4_el_eta = TH1F("W4000N2000_c_WR4_el_eta", "W4000N2000_c_WR4_el_eta", 50, -8, 8)
W4000N2000_cut_WR4_el_mass = TH1F("W4000N2000_c_WR4_el_mass", "W4000N2000_c_WR4_el_mass", 50, 0, 7000)

W4000N2000_cut_WR4_mu_pt = TH1F("W4000N2000_c_WR4_mu_pt", "W4000N2000_c_WR4_mu_pt", 50, 0, 7000)
W4000N2000_cut_WR4_mu_eta = TH1F("W4000N2000_c_WR4_mu_eta", "W4000N2000_c_WR4_mu_eta", 50, -8, 8)
W4000N2000_cut_WR4_mu_mass = TH1F("W4000N2000_c_WR4_mu_mass", "W4000N2000_c_WR4_mu_mass", 50, 0, 7000)

W4000N2000_cut_WR8_pt = TH1F("W4000N2000_c_WR8_pt", "W4000N2000_c_WR8_pt",50,0,7000)
W4000N2000_cut_WR8_eta = TH1F("W4000N2000_c_WR8_eta","W4000N2000_c_WR8_eta",50,-8,8)
W4000N2000_cut_WR8_mass = TH1F("W4000N2000_c_WR8_mass","W4000N2000_c_WR8_mass",50,0,7000)

W4000N2000_cut_subWR8_el_pt = TH1F("W4000N2000_c_subWR8_el_pt","W4000N2000_c_subWR8_el_pt",50,0,7000)
W4000N2000_cut_subWR8_el_eta = TH1F("W4000N2000_c_subWR8_el_eta","W4000N2000_c_subWR8_el_eta",50,-8,8)
W4000N2000_cut_subWR8_el_mass = TH1F("W4000N2000_c_subWR8_el_mass","W4000N2000_c_subWR8_el_mass",50,0,7000)

W4000N2000_cut_subWR8_mu_pt = TH1F("W4000N2000_c_subWR8_mu_pt","W4000N2000_c_subWR8_mu_pt",50,0,7000)
W4000N2000_cut_subWR8_mu_eta = TH1F("W4000N2000_c_subWR8_mu_eta","W4000N2000_c_subWR8_mu_eta",50,-8,8)
W4000N2000_cut_subWR8_mu_mass = TH1F("W4000N2000_c_subWR8_mu_mass","W4000N2000_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################
#################################no####cut################################
W4000N3900_nocut_tau_pt = TH1F("W4000N3900_nc_tau_pt","W4000N3900_nc_tau_pt", 50, 0,7000)
W4000N3900_nocut_tau_eta = TH1F("W4000N3900_nc_tau_eta", "W4000N3900_nc_tau_eta", 50, -8, 8)
W4000N3900_nocut_tau_mass = TH1F("W4000N3900_nc_tau_mass", "W4000N3900_nc_tau_mass", 50, 0, 7000)

W4000N3900_nocut_AK4_pt = TH1F("W4000N3900_nc_4_pt", "W4000N3900_nc_4_pt", 50, 0, 7000)
W4000N3900_nocut_AK4_eta = TH1F("W4000N3900_nc_4_eta", "W4000N3900_nc_4_eta", 50, -8, 8)
W4000N3900_nocut_AK4_mass = TH1F("W4000N3900_nc_4_mass", "W4000N3900_nc_4_mass", 50, 0, 7000)

W4000N3900_nocut_AK4_pt_2 = TH1F("W4000N3900_nc_4_pt_2", "W4000N3900_nc_4_pt_2", 50, 0, 7000)
W4000N3900_nocut_AK4_eta_2 = TH1F("W4000N3900_nc_4_eta_2", "W4000N3900_nc_4_eta_2", 50, -8, 8)
W4000N3900_nocut_AK4_mass_2 = TH1F("W4000N3900_nc_4_mass_2", "W4000N3900_nc_4_mass_2", 50, 0, 7000)

W4000N3900_nocut_AK8_pt = TH1F("W4000N3900_nc_8_pt", "W4000N3900_nc_8_pt", 50, 0, 7000)
W4000N3900_nocut_AK8_eta = TH1F("W4000N3900_nc_8_eta", "W4000N3900_nc_8_eta", 50, -8, 8)
W4000N3900_nocut_AK8_mass = TH1F("W4000N3900_nc_8_mass", "W4000N3900_nc_8_mass", 50, 0, 7000)

W4000N3900_nocut_subAK8_pt = TH1F("W4000N3900_nc_sub8_pt", "W4000N3900_nc_sub8_pt", 50, 0, 7000)
W4000N3900_nocut_subAK8_eta = TH1F("W4000N3900_nc_sub8_eta", "W4000N3900_nc_sub8_eta", 50,-8, 8)
W4000N3900_nocut_subAK8_mass = TH1F("W4000N3900_nc_sub8_mass", "W4000N3900_nc_sub8_mass", 50, 0, 7000)

W4000N3900_nocut_subAK8_pt_2 = TH1F("W4000N3900_nc_sub8_pt_2", "W4000N3900_nc_sub8_pt_2", 50, 0, 7000)
W4000N3900_nocut_subAK8_eta_2 = TH1F("W4000N3900_nc_sub8_eta_2", "W4000N3900_nc_sub8_eta_2", 50,-8, 8)
W4000N3900_nocut_subAK8_mass_2 = TH1F("W4000N3900_nc_sub8_mass_2", "W4000N3900_nc_sub8_mass_2", 50, 0, 7000)

#N
W4000N3900_nocut_N4_el_pt = TH1F("W4000N3900_nc_N4_el_pt", "W4000N3900_nc_N4_el_pt", 50, 0, 7000)
W4000N3900_nocut_N4_el_eta = TH1F("W4000N3900_nc_N4_el_eta", "W4000N3900_nc_N4_el_eta", 50, -8, 8)
W4000N3900_nocut_N4_el_mass = TH1F("W4000N3900_nc_N4_el_mass", "W4000N3900_nc_N4_el_mass", 50, 0, 7000)

W4000N3900_nocut_N4_mu_pt = TH1F("W4000N3900_nc_N4_mu_pt", "W4000N3900_nc_N4_mu_pt", 50, 0, 7000)
W4000N3900_nocut_N4_mu_eta = TH1F("W4000N3900_nc_N4_mu_eta", "W4000N3900_nc_N4_mu_eta", 50, -8, 8)
W4000N3900_nocut_N4_mu_mass = TH1F("W4000N3900_nc_N4_mu_mass", "W4000N3900_nc_N4_mu_mass", 50, 0, 7000)

W4000N3900_nocut_subAK8_el_pt = TH1F("W4000N3900_nc_subN8_el_pt", "W4000N3900_nc_subN8_el_pt" , 50 ,0 ,7000)
W4000N3900_nocut_subAK8_el_eta = TH1F("W4000N3900_nc_subN8_el_eta", "W4000N3900_nc_subN8_el_eta", 50, -8, 8)
W4000N3900_nocut_subAK8_el_mass = TH1F("W4000N3900_nc_subN8_el_mass", "W4000N3900_nc_subN8_el_mass", 50,0,7000)

W4000N3900_nocut_subAK8_mu_pt = TH1F("W4000N3900_nc_subN8_mu_pt", "W4000N3900_nc_subN8_mu_pt", 50, 0, 7000)
W4000N3900_nocut_subAK8_mu_eta = TH1F("W4000N3900_nc_subN8_mu_eta", "W4000N3900_nc_subN8_mu_eta", 50, -8, 8)
W4000N3900_nocut_subAK8_mu_mass = TH1F("W4000N3900_nc_subN8_mu_mass", "W4000N3900_nc_subN8_mu_mass", 50, 0, 7000)


# wr
W4000N3900_nocut_WR4_el_pt = TH1F("W4000N3900_nc_WR4_el_pt", "W4000N3900_nc_WR4_el_pt", 50, 0, 7000)
W4000N3900_nocut_WR4_el_eta = TH1F("W4000N3900_nc_WR4_el_eta", "W4000N3900_nc_WR4_el_eta", 50, -8, 8)
W4000N3900_nocut_WR4_el_mass = TH1F("W4000N3900_nc_WR4_el_mass", "W4000N3900_nc_WR4_el_mass", 50, 0, 7000)

W4000N3900_nocut_WR4_mu_pt = TH1F("W4000N3900_nc_WR4_mu_pt", "W4000N3900_nc_WR4_mu_pt", 50, 0, 7000)
W4000N3900_nocut_WR4_mu_eta = TH1F("W4000N3900_nc_WR4_mu_eta", "W4000N3900_nc_WR4_mu_eta", 50, -8, 8)
W4000N3900_nocut_WR4_mu_mass = TH1F("W4000N3900_nc_WR4_mu_mass", "W4000N3900_nc_WR4_mu_mass", 50, 0, 7000)

W4000N3900_nocut_WR8_pt = TH1F("W4000N3900_nc_WR8_pt", "W4000N3900_nc_WR8_pt",50,0,7000)
W4000N3900_nocut_WR8_eta = TH1F("W4000N3900_nc_WR8_eta","W4000N3900_nc_WR8_eta",50,-8,8)
W4000N3900_nocut_WR8_mass = TH1F("W4000N3900_nc_WR8_mass","W4000N3900_nc_WR8_mass",50,0,7000)

W4000N3900_nocut_subWR8_el_pt = TH1F("W4000N3900_nc_subWR8_el_pt","W4000N3900_nc_subWR8_el_pt",50,0,7000)
W4000N3900_nocut_subWR8_el_eta = TH1F("W4000N3900_nc_subWR8_el_eta","W4000N3900_nc_subWR8_el_eta",50,-8,8)
W4000N3900_nocut_subWR8_el_mass = TH1F("W4000N3900_nc_subWR8_el_mass","W4000N3900_nc_subWR8_el_mass",50,0,7000)

W4000N3900_nocut_subWR8_mu_pt = TH1F("W4000N3900_nc_subWR8_mu_pt","W4000N3900_nc_subWR8_mu_pt",50,0,7000)
W4000N3900_nocut_subWR8_mu_eta = TH1F("W4000N3900_nc_subWR8_mu_eta","W4000N3900_nc_subWR8_mu_eta",50,-8,8)
W4000N3900_nocut_subWR8_mu_mass = TH1F("W4000N3900_nc_subWR8_mu_mass","W4000N3900_nc_subWR8_mu_mass",50,0,7000)


#######################################cut#######################################
W4000N3900_cut_tau_pt = TH1F("W4000N3900_c_tau_pt","W4000N3900_c_tau_pt", 50, 0,7000)
W4000N3900_cut_tau_eta = TH1F("W4000N3900_c_tau_eta", "W4000N3900_c_tau_eta", 50, -8, 8)
W4000N3900_cut_tau_mass = TH1F("W4000N3900_c_tau_mass", "W4000N3900_c_tau_mass", 50, 0, 7000)

W4000N3900_cut_AK4_pt = TH1F("W4000N3900_c_4_pt", "W4000N3900_c_4_pt", 50, 0, 7000)
W4000N3900_cut_AK4_eta = TH1F("W4000N3900_c_4_eta", "W4000N3900_c_4_eta", 50, -8, 8)
W4000N3900_cut_AK4_mass = TH1F("W4000N3900_c_4_mass", "W4000N3900_c_4_mass", 50, 0, 7000)

W4000N3900_cut_AK4_pt_2 = TH1F("W4000N3900_c_4_pt_2", "W4000N3900_c_4_pt_2", 50, 0, 7000)
W4000N3900_cut_AK4_eta_2 = TH1F("W4000N3900_c_4_eta_2", "W4000N3900_c_4_eta_2", 50, -8, 8)
W4000N3900_cut_AK4_mass_2 = TH1F("W4000N3900_c_4_mass_2", "W4000N3900_c_4_mass_2", 50, 0, 7000)

W4000N3900_cut_AK8_pt = TH1F("W4000N3900_c_8_pt", "W4000N3900_c_8_pt", 50, 0, 7000)
W4000N3900_cut_AK8_eta = TH1F("W4000N3900_c_8_eta", "W4000N3900_c_8_eta", 50, -8, 8)
W4000N3900_cut_AK8_mass = TH1F("W4000N3900_c_8_mass", "W4000N3900_c_8_mass", 50, 0, 7000)

W4000N3900_cut_subAK8_pt = TH1F("W4000N3900_c_sub8_pt", "W4000N3900_c_sub8_pt", 50, 0, 7000)
W4000N3900_cut_subAK8_eta = TH1F("W4000N3900_c_sub8_eta", "W4000N3900_c_sub8_eta", 50,-8, 8)
W4000N3900_cut_subAK8_mass = TH1F("W4000N3900_c_sub8_mass", "W4000N3900_c_sub8_mass", 50, 0, 7000)

W4000N3900_cut_subAK8_pt_2 = TH1F("W4000N3900_c_sub8_pt_2", "W4000N3900_c_sub8_pt_2", 50, 0, 7000)
W4000N3900_cut_subAK8_eta_2 = TH1F("W4000N3900_c_sub8_eta_2", "W4000N3900_c_sub8_eta_2", 50,-8, 8)
W4000N3900_cut_subAK8_mass_2 = TH1F("W4000N3900_c_sub8_mass_2", "W4000N3900_c_sub8_mass_2", 50, 0, 7000)

#N
W4000N3900_cut_N4_el_pt = TH1F("W4000N3900_c_N4_el_pt", "W4000N3900_c_N4_el_pt", 50, 0, 7000)
W4000N3900_cut_N4_el_eta = TH1F("W4000N3900_c_N4_el_eta", "W4000N3900_c_N4_el_eta", 50, -8, 8)
W4000N3900_cut_N4_el_mass = TH1F("W4000N3900_c_N4_el_mass", "W4000N3900_c_N4_el_mass", 50, 0, 7000)

W4000N3900_cut_N4_mu_pt = TH1F("W4000N3900_c_N4_mu_pt", "W4000N3900_c_N4_mu_pt", 50, 0, 7000)
W4000N3900_cut_N4_mu_eta = TH1F("W4000N3900_c_N4_mu_eta", "W4000N3900_c_N4_mu_eta", 50, -8, 8)
W4000N3900_cut_N4_mu_mass = TH1F("W4000N3900_c_N4_mu_mass", "W4000N3900_c_N4_mu_mass", 50, 0, 7000)

W4000N3900_cut_subAK8_el_pt = TH1F("W4000N3900_c_subN8_el_pt", "W4000N3900_c_subN8_el_pt" , 50 ,0 ,7000)
W4000N3900_cut_subAK8_el_eta = TH1F("W4000N3900_c_subN8_el_eta", "W4000N3900_c_subN8_el_eta", 50, -8, 8)
W4000N3900_cut_subAK8_el_mass = TH1F("W4000N3900_c_subN8_el_mass", "W4000N3900_c_subN8_el_mass", 50,0,7000)

W4000N3900_cut_subAK8_mu_pt = TH1F("W4000N3900_c_subN8_mu_pt", "W4000N3900_c_subN8_mu_pt", 50, 0, 7000)
W4000N3900_cut_subAK8_mu_eta = TH1F("W4000N3900_c_subN8_mu_eta", "W4000N3900_c_subN8_mu_eta", 50, -8, 8)
W4000N3900_cut_subAK8_mu_mass = TH1F("W4000N3900_c_subN8_mu_mass", "W4000N3900_c_subN8_mu_mass", 50, 0, 7000)


# wr
W4000N3900_cut_WR4_el_pt = TH1F("W4000N3900_c_WR4_el_pt", "W4000N3900_c_WR4_el_pt", 50, 0, 7000)
W4000N3900_cut_WR4_el_eta = TH1F("W4000N3900_c_WR4_el_eta", "W4000N3900_c_WR4_el_eta", 50, -8, 8)
W4000N3900_cut_WR4_el_mass = TH1F("W4000N3900_c_WR4_el_mass", "W4000N3900_c_WR4_el_mass", 50, 0, 7000)

W4000N3900_cut_WR4_mu_pt = TH1F("W4000N3900_c_WR4_mu_pt", "W4000N3900_c_WR4_mu_pt", 50, 0, 7000)
W4000N3900_cut_WR4_mu_eta = TH1F("W4000N3900_c_WR4_mu_eta", "W4000N3900_c_WR4_mu_eta", 50, -8, 8)
W4000N3900_cut_WR4_mu_mass = TH1F("W4000N3900_c_WR4_mu_mass", "W4000N3900_c_WR4_mu_mass", 50, 0, 7000)

W4000N3900_cut_WR8_pt = TH1F("W4000N3900_c_WR8_pt", "W4000N3900_c_WR8_pt",50,0,7000)
W4000N3900_cut_WR8_eta = TH1F("W4000N3900_c_WR8_eta","W4000N3900_c_WR8_eta",50,-8,8)
W4000N3900_cut_WR8_mass = TH1F("W4000N3900_c_WR8_mass","W4000N3900_c_WR8_mass",50,0,7000)

W4000N3900_cut_subWR8_el_pt = TH1F("W4000N3900_c_subWR8_el_pt","W4000N3900_c_subWR8_el_pt",50,0,7000)
W4000N3900_cut_subWR8_el_eta = TH1F("W4000N3900_c_subWR8_el_eta","W4000N3900_c_subWR8_el_eta",50,-8,8)
W4000N3900_cut_subWR8_el_mass = TH1F("W4000N3900_c_subWR8_el_mass","W4000N3900_c_subWR8_el_mass",50,0,7000)

W4000N3900_cut_subWR8_mu_pt = TH1F("W4000N3900_c_subWR8_mu_pt","W4000N3900_c_subWR8_mu_pt",50,0,7000)
W4000N3900_cut_subWR8_mu_eta = TH1F("W4000N3900_c_subWR8_mu_eta","W4000N3900_c_subWR8_mu_eta",50,-8,8)
W4000N3900_cut_subWR8_mu_mass = TH1F("W4000N3900_c_subWR8_mu_mass","W4000N3900_c_subWR8_mu_mass",50,0,7000)




################################################################################################################################################################################################################################################################################



################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################



# 병합 히스토그램 생성
WR1000 = THStack("WR1000", "Combined WR1000; delta R; Events")
WR2000 = THStack("WR2000", "Combined WR2000; delta R; Events")
WR4000 = THStack("WR4000", "Combined WR4000; delta R; Events")


canvas = TCanvas("canvas", "Merged Histogram", 800, 600)
legend = TLegend(0.7, 0.7, 0.9, 0.9)  # 범례 위치 설정
gStyle.SetOptStat(0)  # 통계 박스 비활성화
# 색상 리스트 (ROOT 색상 팔레트)
colors = [1, 2, 4, 6, 8, 9, 28]  # 검정, 빨강, 파랑, 보라, 초록, 청록, 회색



# 각 파일을 읽고 히스토그램 병합

for files in file_list_W1000N100:  # 각 Wr 과 N 안에 있는  root 파일 가져옴 
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 열기
    plots_dir = file_plots.Get("plots")  # "plots" 디렉토리 가져오기
        
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W1000N100_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W1000N100_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W1000N100_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W1000N100_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W1000N100_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W1000N100_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W1000N100_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W1000N100_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W1000N100_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W1000N100_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W1000N100_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W1000N100_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W1000N100_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W1000N100_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W1000N100_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W1000N100_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W1000N100_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W1000N100_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W1000N100_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W1000N100_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W1000N100_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W1000N100_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W1000N100_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W1000N100_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W1000N100_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W1000N100_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W1000N100_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W1000N100_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W1000N100_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W1000N100_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W1000N100_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W1000N100_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W1000N100_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W1000N100_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W1000N100_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W1000N100_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W1000N100_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W1000N100_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W1000N100_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W1000N100_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W1000N100_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W1000N100_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W1000N100_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W1000N100_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W1000N100_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W1000N100_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W1000N100_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W1000N100_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W1000N100_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W1000N100_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W1000N100_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W1000N100_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W1000N100_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W1000N100_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W1000N100_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W1000N100_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W1000N100_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W1000N100_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W1000N100_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W1000N100_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W1000N100_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W1000N100_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W1000N100_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W1000N100_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W1000N100_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W1000N100_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W1000N100_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W1000N100_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W1000N100_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W1000N100_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W1000N100_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W1000N100_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W1000N100_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W1000N100_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W1000N100_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W1000N100_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W1000N100_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W1000N100_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W1000N100_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W1000N100_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))

    file_plots.Close()



    
    # 각 히스토그램 가져오기

for files in file_list_W1000N500:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 열기
    plots_dir = file_plots.Get("plots")  # "plots" 디렉토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W1000N500_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W1000N500_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W1000N500_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W1000N500_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W1000N500_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W1000N500_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W1000N500_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W1000N500_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W1000N500_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W1000N500_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W1000N500_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W1000N500_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W1000N500_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W1000N500_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W1000N500_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W1000N500_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W1000N500_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W1000N500_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W1000N500_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W1000N500_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W1000N500_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W1000N500_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W1000N500_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W1000N500_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W1000N500_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W1000N500_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W1000N500_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W1000N500_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W1000N500_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W1000N500_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W1000N500_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W1000N500_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W1000N500_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W1000N500_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W1000N500_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W1000N500_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W1000N500_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W1000N500_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W1000N500_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W1000N500_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W1000N500_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W1000N500_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W1000N500_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W1000N500_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W1000N500_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W1000N500_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W1000N500_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W1000N500_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W1000N500_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W1000N500_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W1000N500_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W1000N500_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W1000N500_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W1000N500_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W1000N500_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W1000N500_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W1000N500_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W1000N500_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W1000N500_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W1000N500_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W1000N500_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W1000N500_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W1000N500_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W1000N500_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W1000N500_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W1000N500_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W1000N500_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W1000N500_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W1000N500_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W1000N500_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W1000N500_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W1000N500_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W1000N500_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W1000N500_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W1000N500_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W1000N500_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W1000N500_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W1000N500_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W1000N500_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W1000N500_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))

    file_plots.Close()

for files in file_list_W1000N900:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 열기
    plots_dir = file_plots.Get("plots")  # "plots" 디렉토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W1000N900_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W1000N900_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W1000N900_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W1000N900_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W1000N900_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W1000N900_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W1000N900_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W1000N900_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W1000N900_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W1000N900_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W1000N900_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W1000N900_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W1000N900_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W1000N900_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W1000N900_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W1000N900_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W1000N900_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W1000N900_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W1000N900_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W1000N900_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W1000N900_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W1000N900_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W1000N900_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W1000N900_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W1000N900_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W1000N900_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W1000N900_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W1000N900_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W1000N900_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W1000N900_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W1000N900_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W1000N900_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W1000N900_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W1000N900_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W1000N900_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W1000N900_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W1000N900_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W1000N900_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W1000N900_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W1000N900_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W1000N900_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W1000N900_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W1000N900_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W1000N900_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W1000N900_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W1000N900_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W1000N900_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W1000N900_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W1000N900_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W1000N900_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W1000N900_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W1000N900_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W1000N900_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W1000N900_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W1000N900_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W1000N900_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W1000N900_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W1000N900_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W1000N900_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W1000N900_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W1000N900_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W1000N900_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W1000N900_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W1000N900_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W1000N900_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W1000N900_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W1000N900_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W1000N900_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W1000N900_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W1000N900_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W1000N900_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W1000N900_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W1000N900_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W1000N900_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W1000N900_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W1000N900_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W1000N900_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W1000N900_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W1000N900_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W1000N900_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))

    file_plots.Close()

for files in file_list_W2000N100:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 열기
    plots_dir = file_plots.Get("plots")  # "plots" 디렉토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W2000N100_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W2000N100_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W2000N100_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W2000N100_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W2000N100_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W2000N100_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W2000N100_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W2000N100_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W2000N100_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W2000N100_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W2000N100_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W2000N100_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W2000N100_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W2000N100_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W2000N100_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W2000N100_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W2000N100_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W2000N100_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W2000N100_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W2000N100_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W2000N100_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W2000N100_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W2000N100_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W2000N100_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W2000N100_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W2000N100_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W2000N100_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W2000N100_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W2000N100_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W2000N100_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W2000N100_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W2000N100_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W2000N100_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W2000N100_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W2000N100_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W2000N100_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W2000N100_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W2000N100_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W2000N100_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W2000N100_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W2000N100_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W2000N100_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W2000N100_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W2000N100_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W2000N100_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W2000N100_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W2000N100_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W2000N100_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W2000N100_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W2000N100_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W2000N100_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W2000N100_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W2000N100_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W2000N100_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W2000N100_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W2000N100_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W2000N100_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W2000N100_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W2000N100_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W2000N100_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W2000N100_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W2000N100_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W2000N100_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W2000N100_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W2000N100_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W2000N100_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W2000N100_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W2000N100_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W2000N100_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W2000N100_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W2000N100_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W2000N100_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W2000N100_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W2000N100_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W2000N100_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W2000N100_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W2000N100_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W2000N100_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W2000N100_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W2000N100_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))


    file_plots.Close()

for files in file_list_W2000N1000:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 ��기
    plots_dir = file_plots.Get("plots")  # "plots" 디��토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W2000N1000_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W2000N1000_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W2000N1000_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W2000N1000_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W2000N1000_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W2000N1000_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W2000N1000_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W2000N1000_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W2000N1000_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W2000N1000_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W2000N1000_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W2000N1000_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W2000N1000_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W2000N1000_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W2000N1000_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W2000N1000_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W2000N1000_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W2000N1000_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W2000N1000_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W2000N1000_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W2000N1000_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W2000N1000_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W2000N1000_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W2000N1000_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W2000N1000_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W2000N1000_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W2000N1000_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W2000N1000_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W2000N1000_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W2000N1000_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W2000N1000_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W2000N1000_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W2000N1000_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W2000N1000_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W2000N1000_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W2000N1000_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W2000N1000_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W2000N1000_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W2000N1000_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W2000N1000_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W2000N1000_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W2000N1000_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W2000N1000_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W2000N1000_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W2000N1000_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W2000N1000_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W2000N1000_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W2000N1000_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W2000N1000_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W2000N1000_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W2000N1000_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W2000N1000_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W2000N1000_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W2000N1000_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W2000N1000_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W2000N1000_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W2000N1000_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W2000N1000_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W2000N1000_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W2000N1000_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W2000N1000_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W2000N1000_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W2000N1000_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W2000N1000_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W2000N1000_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W2000N1000_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W2000N1000_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W2000N1000_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W2000N1000_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W2000N1000_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W2000N1000_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W2000N1000_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W2000N1000_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W2000N1000_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W2000N1000_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W2000N1000_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W2000N1000_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W2000N1000_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W2000N1000_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W2000N1000_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))


    file_plots.Close()

for files in file_list_W2000N1900:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 ��기
    plots_dir = file_plots.Get("plots")  # "plots" 디��토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W2000N1900_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W2000N1900_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W2000N1900_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W2000N1900_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W2000N1900_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W2000N1900_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W2000N1900_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W2000N1900_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W2000N1900_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W2000N1900_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W2000N1900_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W2000N1900_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W2000N1900_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W2000N1900_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W2000N1900_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W2000N1900_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W2000N1900_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W2000N1900_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W2000N1900_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W2000N1900_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W2000N1900_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W2000N1900_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W2000N1900_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W2000N1900_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W2000N1900_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W2000N1900_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W2000N1900_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W2000N1900_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W2000N1900_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W2000N1900_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W2000N1900_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W2000N1900_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W2000N1900_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W2000N1900_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W2000N1900_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W2000N1900_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W2000N1900_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W2000N1900_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W2000N1900_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W2000N1900_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W2000N1900_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W2000N1900_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W2000N1900_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W2000N1900_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W2000N1900_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W2000N1900_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W2000N1900_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W2000N1900_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W2000N1900_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W2000N1900_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W2000N1900_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W2000N1900_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W2000N1900_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W2000N1900_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W2000N1900_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W2000N1900_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W2000N1900_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W2000N1900_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W2000N1900_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W2000N1900_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W2000N1900_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W2000N1900_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W2000N1900_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W2000N1900_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W2000N1900_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W2000N1900_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W2000N1900_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W2000N1900_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W2000N1900_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W2000N1900_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W2000N1900_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W2000N1900_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W2000N1900_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W2000N1900_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W2000N1900_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W2000N1900_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W2000N1900_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W2000N1900_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W2000N1900_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W2000N1900_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))


    file_plots.Close()

for files in file_list_W4000N100:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 ��기
    plots_dir = file_plots.Get("plots")  # "plots" 디��토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W4000N100_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W4000N100_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W4000N100_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W4000N100_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W4000N100_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W4000N100_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W4000N100_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W4000N100_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W4000N100_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W4000N100_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W4000N100_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W4000N100_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W4000N100_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W4000N100_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W4000N100_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W4000N100_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W4000N100_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W4000N100_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W4000N100_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W4000N100_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W4000N100_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W4000N100_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W4000N100_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W4000N100_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W4000N100_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W4000N100_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W4000N100_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W4000N100_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W4000N100_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W4000N100_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W4000N100_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W4000N100_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W4000N100_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W4000N100_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W4000N100_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W4000N100_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W4000N100_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W4000N100_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W4000N100_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W4000N100_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W4000N100_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W4000N100_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W4000N100_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W4000N100_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W4000N100_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W4000N100_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W4000N100_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W4000N100_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W4000N100_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W4000N100_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W4000N100_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W4000N100_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W4000N100_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W4000N100_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W4000N100_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W4000N100_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W4000N100_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W4000N100_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W4000N100_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W4000N100_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W4000N100_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W4000N100_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W4000N100_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W4000N100_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W4000N100_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W4000N100_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W4000N100_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W4000N100_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W4000N100_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W4000N100_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W4000N100_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W4000N100_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W4000N100_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W4000N100_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W4000N100_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W4000N100_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W4000N100_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W4000N100_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W4000N100_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W4000N100_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))

    file_plots.Close()

for files in file_list_W4000N2000:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 ��기
    plots_dir = file_plots.Get("plots")  # "plots" 디��토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W4000N2000_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W4000N2000_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W4000N2000_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W4000N2000_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W4000N2000_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W4000N2000_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W4000N2000_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W4000N2000_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W4000N2000_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W4000N2000_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W4000N2000_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W4000N2000_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W4000N2000_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W4000N2000_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W4000N2000_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W4000N2000_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W4000N2000_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W4000N2000_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W4000N2000_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W4000N2000_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W4000N2000_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W4000N2000_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W4000N2000_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W4000N2000_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W4000N2000_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W4000N2000_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W4000N2000_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W4000N2000_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W4000N2000_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W4000N2000_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W4000N2000_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W4000N2000_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W4000N2000_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W4000N2000_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W4000N2000_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W4000N2000_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W4000N2000_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W4000N2000_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W4000N2000_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W4000N2000_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W4000N2000_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W4000N2000_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W4000N2000_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W4000N2000_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W4000N2000_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W4000N2000_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W4000N2000_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W4000N2000_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W4000N2000_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W4000N2000_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W4000N2000_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W4000N2000_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W4000N2000_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W4000N2000_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W4000N2000_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W4000N2000_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W4000N2000_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W4000N2000_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W4000N2000_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W4000N2000_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W4000N2000_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W4000N2000_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W4000N2000_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W4000N2000_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W4000N2000_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W4000N2000_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W4000N2000_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W4000N2000_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W4000N2000_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W4000N2000_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W4000N2000_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W4000N2000_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W4000N2000_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W4000N2000_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W4000N2000_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W4000N2000_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W4000N2000_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W4000N2000_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W4000N2000_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W4000N2000_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))


    file_plots.Close()

for files in file_list_W4000N3900:
    print(f"Processing file: {files}")
    file_plots = TFile.Open(files)  # ROOT 파일 ��기
    plots_dir = file_plots.Get("plots")  # "plots" 디��토리 가져오기
        ## tau AK4 AK8 subAK8 disttribution

        #pt
    W4000N3900_nocut_tau_pt.Add(plots_dir.Get("tau_no_cut_pt_leading"))
    W4000N3900_nocut_tau_eta.Add(plots_dir.Get("tau_no_cut_eta_leading"))

    W4000N3900_nocut_AK4_pt.Add(plots_dir.Get("jetAK4_no_cut_pt_leading")) 
    W4000N3900_nocut_AK4_eta.Add(plots_dir.Get("jetAK4_no_cut_eta_leading"))

    W4000N3900_nocut_AK4_pt_2.Add(plots_dir.Get("jetAK4_no_cut_pt_subleading"))
    W4000N3900_nocut_AK4_eta_2.Add(plots_dir.Get("jetAK4_no_cut_eta_subleading"))     

    W4000N3900_nocut_subAK8_pt.Add(plots_dir.Get("subjetAK8_no_cut_pt_leading"))
    W4000N3900_nocut_subAK8_eta.Add(plots_dir.Get("subjetAK8_no_cut_eta_leading"))

    W4000N3900_nocut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_no_cut_pt_subleading"))
    W4000N3900_nocut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_no_cut_eta_subleading")) 

    #N
    W4000N3900_nocut_N4_el_pt.Add(plots_dir.Get("N4_no_cut_pt_el"))
    W4000N3900_nocut_N4_el_eta.Add(plots_dir.Get("N4_no_cut_eta_el"))
    W4000N3900_nocut_N4_el_mass.Add(plots_dir.Get("no_cut_mass_AK4_el")) 

    W4000N3900_nocut_N4_mu_pt.Add(plots_dir.Get("N4_no_cut_pt_mu"))
    W4000N3900_nocut_N4_mu_eta.Add(plots_dir.Get("N4_no_cut_pt_mu")) 
    W4000N3900_nocut_N4_mu_mass.Add(plots_dir.Get("no_cut_mass_AK4_mu")) 

    W4000N3900_nocut_AK8_pt.Add(plots_dir.Get("jetAK8_no_cut_pt_leading"))
    W4000N3900_nocut_AK8_eta.Add(plots_dir.Get("jetAK8_no_cut_eta_leading"))
    W4000N3900_nocut_AK8_mass.Add(plots_dir.Get("no_cut_mass_AK8"))

    W4000N3900_nocut_subAK8_el_pt.Add(plots_dir.Get("subN8_no_cut_pt_el"))
    W4000N3900_nocut_subAK8_el_eta.Add(plots_dir.Get("subN8_no_cut_eta_el"))
    W4000N3900_nocut_subAK8_el_mass.Add(plots_dir.Get("no_cut_mass_subAK8_el")) 

    W4000N3900_nocut_subAK8_mu_pt.Add(plots_dir.Get("subN8_no_cut_pt_mu"))
    W4000N3900_nocut_subAK8_mu_eta.Add(plots_dir.Get("subN8_no_cut_eta_mu"))
    W4000N3900_nocut_subAK8_mu_mass.Add(plots_dir.Get("no_cut_mass_subAK8_mu")) 

    # wr
    W4000N3900_nocut_WR4_el_pt.Add(plots_dir.Get("WR4_no_cut_pt_el"))
    W4000N3900_nocut_WR4_el_eta.Add(plots_dir.Get("WR4_no_cut_eta_el"))
    W4000N3900_nocut_WR4_el_mass.Add(plots_dir.Get("WR4_no_cut_mass_el")) 

    W4000N3900_nocut_WR4_mu_pt.Add(plots_dir.Get("WR4_no_cut_pt_mu"))
    W4000N3900_nocut_WR4_mu_eta.Add(plots_dir.Get("WR4_no_cut_eta_mu"))
    W4000N3900_nocut_WR4_mu_mass.Add(plots_dir.Get("WR4_no_cut_mass_mu")) 


    W4000N3900_nocut_WR8_pt.Add(plots_dir.Get("WR8_no_cut_pt"))
    W4000N3900_nocut_WR8_eta.Add(plots_dir.Get("WR8_no_cut_eta"))
    W4000N3900_nocut_WR8_mass.Add(plots_dir.Get("tau_no_cut_mass_AK8_tau"))

    W4000N3900_nocut_subWR8_el_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W4000N3900_nocut_subWR8_el_eta.Add(plots_dir.Get("subWR8_no_cut_eta_el"))
    W4000N3900_nocut_subWR8_el_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_el"))

    W4000N3900_nocut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_no_cut_pt_el"))
    W4000N3900_nocut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_no_cut_pt_mu"))
    W4000N3900_nocut_subWR8_mu_mass.Add(plots_dir.Get("tau_no_cut_mass_subAK8_mu"))

    

    #######################################cut#######################################
            #pt
    W4000N3900_cut_tau_pt.Add(plots_dir.Get("tau_cut_pt_leading"))
    W4000N3900_cut_tau_eta.Add(plots_dir.Get("tau_cut_eta_leading"))

    W4000N3900_cut_AK4_pt.Add(plots_dir.Get("jetAK4_cut_pt_leading")) 
    W4000N3900_cut_AK4_eta.Add(plots_dir.Get("jetAK4_cut_eta_leading"))

    W4000N3900_cut_AK4_pt_2.Add(plots_dir.Get("jetAK4_cut_pt_subleading"))
    W4000N3900_cut_AK4_eta_2.Add(plots_dir.Get("jetAK4_cut_eta_subleading"))     

    W4000N3900_cut_subAK8_pt.Add(plots_dir.Get("subjetAK8_cut_pt_leading"))
    W4000N3900_cut_subAK8_eta.Add(plots_dir.Get("subjetAK8_cut_eta_leading"))

    W4000N3900_cut_subAK8_pt_2.Add(plots_dir.Get("subjetAK8_cut_pt_subleading"))
    W4000N3900_cut_subAK8_eta_2.Add(plots_dir.Get("subjetAK8_cut_eta_subleading")) 

    #N
    W4000N3900_cut_N4_el_pt.Add(plots_dir.Get("N4_cut_pt_el"))
    W4000N3900_cut_N4_el_eta.Add(plots_dir.Get("N4_cut_eta_el"))
    W4000N3900_cut_N4_el_mass.Add(plots_dir.Get("cut_mass_AK4_el")) 

    W4000N3900_cut_N4_mu_pt.Add(plots_dir.Get("N4_cut_pt_mu"))
    W4000N3900_cut_N4_mu_eta.Add(plots_dir.Get("N4_cut_pt_mu")) 
    W4000N3900_cut_N4_mu_mass.Add(plots_dir.Get("cut_mass_AK4_mu")) 

    W4000N3900_cut_AK8_pt.Add(plots_dir.Get("jetAK8_cut_pt_leading"))
    W4000N3900_cut_AK8_eta.Add(plots_dir.Get("jetAK8_cut_eta_leading"))
    W4000N3900_cut_AK8_mass.Add(plots_dir.Get("cut_mass_AK8"))

    W4000N3900_cut_subAK8_el_pt.Add(plots_dir.Get("subN8_cut_pt_el"))
    W4000N3900_cut_subAK8_el_eta.Add(plots_dir.Get("subN8_cut_eta_el"))
    W4000N3900_cut_subAK8_el_mass.Add(plots_dir.Get("cut_mass_subAK8_el")) 

    W4000N3900_cut_subAK8_mu_pt.Add(plots_dir.Get("subN8_cut_pt_mu"))
    W4000N3900_cut_subAK8_mu_eta.Add(plots_dir.Get("subN8_cut_eta_mu"))
    W4000N3900_cut_subAK8_mu_mass.Add(plots_dir.Get("cut_mass_subAK8_mu")) 

    # wr
    W4000N3900_cut_WR4_el_pt.Add(plots_dir.Get("WR4_cut_pt_el"))
    W4000N3900_cut_WR4_el_eta.Add(plots_dir.Get("WR4_cut_eta_el"))
    W4000N3900_cut_WR4_el_mass.Add(plots_dir.Get("WR4_cut_mass_el")) 

    W4000N3900_cut_WR4_mu_pt.Add(plots_dir.Get("WR4_cut_pt_mu"))
    W4000N3900_cut_WR4_mu_eta.Add(plots_dir.Get("WR4_cut_eta_mu"))
    W4000N3900_cut_WR4_mu_mass.Add(plots_dir.Get("WR4_cut_mass_mu")) 


    W4000N3900_cut_WR8_pt.Add(plots_dir.Get("WR8_cut_pt"))
    W4000N3900_cut_WR8_eta.Add(plots_dir.Get("WR8_cut_eta"))
    W4000N3900_cut_WR8_mass.Add(plots_dir.Get("tau_cut_mass_AK8_tau"))

    W4000N3900_cut_subWR8_el_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W4000N3900_cut_subWR8_el_eta.Add(plots_dir.Get("subWR8_cut_eta_el"))
    W4000N3900_cut_subWR8_el_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_el"))

    W4000N3900_cut_subWR8_mu_pt.Add(plots_dir.Get("subWR8_cut_pt_el"))
    W4000N3900_cut_subWR8_mu_eta.Add(plots_dir.Get("subWR8_cut_pt_mu"))
    W4000N3900_cut_subWR8_mu_mass.Add(plots_dir.Get("tau_cut_mass_subAK8_mu"))

    file_plots.Close()


# TCanvas 생성
canvas_WR1000 = TCanvas("canvas_WR1000", "WR1000 Comparison", 800, 600)
canvas_WR2000 = TCanvas("canvas_WR2000", "WR2000 Comparison", 800, 600)
canvas_WR4000 = TCanvas("canvas_WR4000", "WR4000 Comparison", 800, 600)








# 히스토그램 겹쳐 그리기 설정
def draw_histograms(canvas, hists, title):
    """
    canvas   : TCanvas 객체
    hists    : 그릴 히스토그램 리스트 (예: [hist1, hist2, hist3])
    title    : 첫 번째 히스토그램에 표시할 Title
    """
    # 1) 캔버스 설정
    canvas.cd()
    canvas.SetGrid(1, 1)  # (X축, Y축) 격자
    # 필요 시 canvas.Clear() 등으로 초기화 가능

    # 2) 레전드 생성
    # 위치를 넓게 잡아서 히스토그램이 레전드를 가리지 않도록 함
    legend = TLegend(0.55, 0.65, 0.88, 0.88)
    legend.SetTextSize(0.03)
    legend.SetBorderSize(1)    # 테두리 있음 (0이면 테두리 없음)
    legend.SetFillStyle(1001)  # 레전드 박스 채우기 (0으로 하면 투명)
    legend.SetFillColor(kWhite)  # 하얀 배경
    legend.SetTextColor(kBlack)  # 검정색 글자

    # 3) 히스토그램 Draw 및 레전드 등록
    first_hist = True
    for i, hist in enumerate(hists):
        # (3-1) 히스토그램 그리기
        if first_hist:
            hist.SetTitle(title)     # 캔버스 윗부분에 표시될 제목; "X축; Y축" 형식
            hist.Draw("HIST")        # 첫 히스토그램
            first_hist = False
        else:
            hist.Draw("HIST SAME")   # 겹쳐 그리기

        

    print("Number of legend entries:", legend.GetNRows())
## 각 샘플 갯수 다르므로 noramlization

# X축 범위 제한
W1000N100.GetXaxis().SetRangeUser(0.1, 5)
W1000N500.GetXaxis().SetRangeUser(0.1, 5)
W1000N900.GetXaxis().SetRangeUser(0.1, 5)

W2000N100.GetXaxis().SetRangeUser(0.1, 5)
W2000N1000.GetXaxis().SetRangeUser(0.1, 5)
W2000N1900.GetXaxis().SetRangeUser(0.1, 5)

W4000N100.GetXaxis().SetRangeUser(0.1, 5)
W4000N2000.GetXaxis().SetRangeUser(0.1, 5)
W4000N3900.GetXaxis().SetRangeUser(0.1, 5)

# WR1000 그룹 히스토그램 그리기
W1000N100.Scale(1/W1000N100.Integral())
W1000N500.Scale(1/W1000N500.Integral())
W1000N900.Scale(1/W1000N900.Integral())
draw_histograms(
    canvas_WR1000, 
    [W1000N100, W1000N500, W1000N900], 
    "WR1000 Comparison; DeltaR(q,q); A.U."
)





output_file.cd()
W1000N100.Write()
W1000N500.Write()
W1000N900.Write()

W2000N100.Write()
W2000N1000.Write()
W2000N1900.Write()

W4000N100.Write()
W4000N2000.Write()
W4000N3900.Write()

canvas_WR1000.Write("canvas_WR1000")
canvas_WR2000.Write("canvas_WR2000")
canvas_WR4000.Write("canvas_WR4000")

canvas_WR1000.SaveAs("canvas_WR1000.png")
canvas_WR2000.SaveAs("canvas_WR2000.png")
canvas_WR4000.SaveAs("canvas_WR4000.png")

output_file.Close()



print("Histograms are saved and comparison plots are generated.")
