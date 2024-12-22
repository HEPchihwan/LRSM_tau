// multi_file_cutflow.C
#include <TFile.h>
#include <TH1F.h>
#include <TCanvas.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <TStyle.h> // gStyle 사용을 위해 추가

void macro() {
    gStyle->SetOptStat(0); // 통계박스 비활성화
    // 1. 파일 이름 목록 정의
    std::vector<std::string> fileNames1000 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N900.root"};
        std::vector<std::string> fileNames1500 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1400.root"};
        std::vector<std::string> fileNames2000 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1900.root"};
        std::vector<std::string> fileNames2500 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2400.root"};
        std::vector<std::string> fileNames3000 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2900.root"};
        std::vector<std::string> fileNames3500 = {  
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3400.root"
        };
        std::vector<std::string> fileNames4000 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3900.root"
        };
        std::vector<std::string> fileNames4500 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N3900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4400.root"
        };
        std::vector<std::string> fileNames5000 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N3900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4900.root"};
        std::vector<std::string> fileNames5500 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N3900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N4900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5400.root"
        };
        std::vector<std::string> fileNames6000 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N3900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N4900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5900.root"};
        std::vector<std::string> fileNames6500 = {
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N3900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N4900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N5900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6400.root"
    };



    

    
    
    
    std::vector<std::string> *fileNamesArray[] = {&fileNames1000, &fileNames1500, &fileNames2000 , &fileNames2500, &fileNames3000, &fileNames3500, &fileNames4000, &fileNames4500, &fileNames5000, &fileNames5500, &fileNames6000, &fileNames6500};

    // 각 파일 이름 목록에 대해 반복 처리
    for (int i = 0; i < sizeof(fileNamesArray)/sizeof(fileNamesArray[0]); ++i) {
        auto fileNames = fileNamesArray[i];
        int numFiles = fileNames->size(); // 루트파일 개수 계산
        int mass = 1000 + i * 500; // mass = 1000, 1500, 2000, ..., 6500
        int k = mass; // k를 mass로 설정
        // MET cut 과  tigger 통과한 양 비교 
        TH1F *hist_frame1 = new TH1F("hist_frame1", "Ratio of taucut to MET filter", numFiles + 10, 0, numFiles + 10);
        hist_frame1->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame1->GetYaxis()->SetTitle("taucut / MET filter");

        TH1F *hist_frame2 = new TH1F("hist_frame2", "Ratio of mutaucut to METfilter", numFiles + 10, 0, numFiles + 10);
        hist_frame2->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame2->GetYaxis()->SetTitle("mutaucut / MET filter");

        // MET 통과 + tigger통과 + ID 통과
        TH1F *hist_frame3 = new TH1F("hist_frame3", "Ratio of taucut + IDcut to MET filter", numFiles + 10, 0, numFiles + 10);
        hist_frame3->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame3->GetYaxis()->SetTitle("taucut + IDcut / MET filter ");

        TH1F *hist_frame4 = new TH1F("hist_frame4", "Ratio of mutaucut + IDcut to MET filter", numFiles + 10, 0, numFiles + 10);
        hist_frame4->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame4->GetYaxis()->SetTitle("mutaucut + IDcut / MET filter");

        // MET 통과 + tigger통과 + ID 통과 + Pt cut 통과 

        TH1F *hist_frame5 = new TH1F("hist_frame5", "Ratio of taucut + IDcut + Ptcut to MET filter", numFiles + 10, 0, numFiles + 10);
        hist_frame5->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame5->GetYaxis()->SetTitle("taucut + IDcut + Ptcut / MET filter");

        TH1F *hist_frame6 = new TH1F("hist_frame6", "Ratio of mutaucut + IDcut + Ptcut to MET filter", numFiles + 10, 0, numFiles + 10);
        hist_frame6->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame6->GetYaxis()->SetTitle("mutaucut + IDcut + Ptcut / MET filter");

        TH1F *hist_frame7 = new TH1F("hist_frame7", "Ratio trigger of taucut + IDcut + Ptcut to MET filter", numFiles + 10, 0, numFiles + 10);
        hist_frame7->GetXaxis()->SetTitle(Form("~N%d (GeV)", k));
        hist_frame7->GetYaxis()->SetTitle("trigger of taucut + IDcut + Ptcut / MET filter");


        double scale_factor = 3.0; // 최댓값을 20% 정도 더 크게 설정

        hist_frame1->SetMaximum(hist_frame1->GetMaximum() * scale_factor);
        hist_frame2->SetMaximum(hist_frame2->GetMaximum() * scale_factor);
        hist_frame3->SetMaximum(hist_frame3->GetMaximum() * scale_factor);
        hist_frame4->SetMaximum(hist_frame4->GetMaximum() * scale_factor);
        hist_frame5->SetMaximum(hist_frame5->GetMaximum() * scale_factor);
        hist_frame6->SetMaximum(hist_frame6->GetMaximum() * scale_factor);
        


        // X축 레이블 설정
        for (int bin = 1; bin <= numFiles + 10; ++bin) {
            int labelValue = bin * 100; // 레이블 값을 100의 배수로 설정

            if (k == 1000) { // k가 1000일 때
                if (bin % 2 == 0) {
                    hist_frame1->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame2->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame3->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame4->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame5->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame6->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame7->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                }
            } else if (k >= 1000 && k < 2000) {
                if (bin % 2 == 0) {
                    hist_frame1->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame2->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame3->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame4->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame5->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame6->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame7->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));

                }
            } else if (k >= 2000 && k < 4000) {
                if (bin % 5 == 0) {
                    hist_frame1->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame2->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame3->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame4->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame5->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame6->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame7->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));

                }
            } else if (k >= 4000 && k <= 6500) {
                if (bin % 10 == 0) {
                    hist_frame1->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame2->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame3->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame4->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame5->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame6->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));
                    hist_frame7->GetXaxis()->SetBinLabel(bin, Form("%d", labelValue));

                }
            }
        }

        // 기존 레이블 간격을 유지하면서 100배로 설정
        
        //int mass = (i + 1) * 500 + 500; // 1000, 1500, 2000, ..., 6500
        int binIndex = 1; // 히스토그램의 현재 빈 인덱스
        // 3. 파일 목록 반복 처리
        for (const auto &fileName : *fileNames) {
            TFile *file = TFile::Open(fileName.c_str());
            if (!file || file->IsZombie()) {
                std::cerr << "Failed to open file: " << fileName << std::endl;
                continue;
            }
            
            
            // 4. cutflow 히스토그램 가져오기
            TH1 *cutflowHist = (TH1*)file->Get("Not triggered");
            if (!cutflowHist) {
                std::cerr << "Failed to find cutflow in file: " << fileName << std::endl;
                file->Close();
                continue;
            }
            
            // 5. mutau히스토그램 가져오기
            TH1 *mutautriggerHist = (TH1*)file->Get("mu_tau");
            if (!mutautriggerHist) {
                std::cerr << "Failed to find Not mu_tau in file: " << fileName << std::endl;
                file->Close();
                continue;
            }

            // 5. tau히스토그램 가져오기
            TH1 *tautriggerHist = (TH1*)file->Get("tau");
            if (!tautriggerHist) {
                std::cerr << "Failed to find Not tau in file: " << fileName << std::endl;
                file->Close();
                continue;
            }

            // 6. 각 파일의 taucut 및 NotTriggeredCutflow 값 추출
            double METcut =  cutflowHist->GetBinContent(1);
            
            double tautriggercut = tautriggerHist->GetBinContent(1);
            double tautIDcut = tautriggerHist->GetBinContent(2);
            double tauPTcut = tautriggerHist->GetBinContent(3);

            double mutautriggercut = mutautriggerHist->GetBinContent(1);
            double mutauIDcut = mutautriggerHist->GetBinContent(2);
            double mutauPTcut = mutautriggerHist->GetBinContent(3);


            
            // 7. taucut / notTriggeredCutflow 비율 계산 및 히스토그램에 채우기
            if (METcut != 0) {
                double tautriggercutratio = tautriggercut / METcut;
                double mutautriggercutratio = mutautriggercut / METcut;

                double tauIDcutratio = tautIDcut / METcut;
                double mutauIDcutratio = mutauIDcut / METcut;

                double tauPTcutratio = tauPTcut / METcut;
                double mutauPTcutratio = mutauPTcut / METcut;

                double final_trigger_ratio = (mutauPTcut - tauPTcut)/METcut ;

                hist_frame1->SetBinContent(binIndex , tautriggercutratio);
                hist_frame2->SetBinContent(binIndex , mutautriggercutratio);

                hist_frame3->SetBinContent(binIndex, tauIDcutratio);
                hist_frame4->SetBinContent(binIndex, mutauIDcutratio);

                hist_frame5->SetBinContent(binIndex, tauPTcutratio);
                hist_frame6->SetBinContent(binIndex, mutauPTcutratio);

                hist_frame7->SetBinContent(binIndex, final_trigger_ratio);

            } else {
                std::cerr << "Warning: NotTriggeredCutflow is zero in file: " << fileName << std::endl;
            }

            binIndex++; // 다음 빈으로 이동
            file->Close(); // 파일 기
        }
            
            TCanvas *canvas = new TCanvas(Form("canvas_WR%d", mass), "tigger Ratio", 800, 600);
            hist_frame1->SetLineColor(kRed);
            hist_frame2->SetLineColor(kBlue);
            hist_frame1->SetMaximum(1.5); // 최댓값 고정
            hist_frame2->SetMaximum(1.5); // 최댓값 고정
            hist_frame1->Draw();
            hist_frame2->Draw("same");

            TLegend *legend2 = new TLegend(0.7, 0.7, 0.9, 0.9); // 범례 위치 설정
            legend2->AddEntry(hist_frame1, "taucut ratio", "l");
            legend2->AddEntry(hist_frame2, "mutaucut ratio", "l");
            legend2->Draw();

            canvas->SaveAs(Form("output/trigger_ratio_WR%d.png", mass)); // 결과 저장
            
            std::cout << "First frame histogram saved as 'trigger_ratio_WR" << mass << ".png'." << std::endl;

            //  9. 두 번째 액자를 캔버스에 그리기
            TCanvas *canvas2 = new TCanvas(Form("canvas2_WR%d", mass), "IDcut Ratio", 800, 600);
            hist_frame3->SetLineColor(kRed);
            hist_frame3->Draw();
            hist_frame4->SetLineColor(kBlue);
            hist_frame4->Draw("same");

            TLegend *legend1 = new TLegend(0.7, 0.7, 0.9, 0.9); // 범례 위치 설정
            legend1->AddEntry(hist_frame3, "taucut ratio", "l");
            legend1->AddEntry(hist_frame4, "mutaucut ratio", "l");
            legend1->Draw();

            canvas2->SaveAs(Form("output/IDcut_ratio_WR%d.png", mass)); // 결과 저장

            std::cout << "Second frame histogram saved as 'IDcut_ratio_WR" << mass << ".png'." << std::endl;

            // 10. 세 번째 액자에 두 히스토그램을 함께 그리기
            TCanvas *canvas3 = new TCanvas(Form("canvas3_WR%d", mass), "Ptcut ratio", 800, 600);
            hist_frame5->SetLineColor(kRed);  // 첫 번째 히스토그램의 색상 설정
            hist_frame6->SetLineColor(kBlue); // 두 번째 히스토그램의 색상 설정
            hist_frame5->Draw();              // 첫 번째 히스토그램 먼저 그리기
            hist_frame6->Draw("same");        // 두 번째 히스토그램을 동일 캔버스에 겹쳐서 그리기

            // 범례 추가
            TLegend *legend = new TLegend(0.7, 0.7, 0.9, 0.9); // 범례 위치 설정
            legend->AddEntry(hist_frame5, "taucut ratio", "l");
            legend->AddEntry(hist_frame6, "mutaucut ratio", "l");
            legend->Draw();

            canvas3->SaveAs(Form("output/ptcut_WR%d.png", mass)); // 결과 저장


            TCanvas *canvas4 = new TCanvas(Form("canvas4_WR%d", mass), "compare with each ratio", 1600, 1200);

        // 첫 번째 쌍: hist_frame1, hist_frame2 (파란색 계열)
            hist_frame1->SetLineColor(kBlue + 2); // 진한 파랑
            hist_frame1->SetLineStyle(1);         // solid line
            hist_frame2->SetLineColor(kBlue - 4); // 밝은 파랑
            hist_frame2->SetLineStyle(2);         // dashed line

// 두 번째 쌍: hist_frame3, hist_frame4 (초록색 계열)
            hist_frame3->SetLineColor(kGreen + 2); // 진한 초록
            hist_frame3->SetLineStyle(1);          // solid line
            hist_frame4->SetLineColor(kGreen - 4); // 밝은 초록
            hist_frame4->SetLineStyle(2);          // dashed line

// 세 번째 쌍: hist_frame5, hist_frame6 (주황색 계열)
            hist_frame5->SetLineColor(kOrange + 1); // 진한 주황
            hist_frame5->SetLineStyle(1);           // solid line
            hist_frame6->SetLineColor(kOrange - 3); // 밝은 주황
            hist_frame6->SetLineStyle(2);           // dashed line
            
            
            hist_frame3->SetMaximum(1.5); // 최댓값 고정
            hist_frame4->SetMaximum(1.5); // 최댓값 고정
            hist_frame5->SetMaximum(1.5); // 최댓값 고정   
            hist_frame6->SetMaximum(1.5); // 최댓값 고정
            hist_frame7->SetMaximum(1.5); // 최댓값 고정
// 히스토그램을 겹쳐서 그림
            hist_frame1->Draw();
            hist_frame2->Draw("same");
            hist_frame3->Draw("same");
            hist_frame4->Draw("same");
            hist_frame5->Draw("same");
            hist_frame6->Draw("same");

// 범례 추가
            TLegend *legend4 = new TLegend(0.7, 0.7, 0.9, 0.9);
            legend4->AddEntry(hist_frame1, "taucut / NotTriggeredCutflow (solid dark blue)", "l");
            legend4->AddEntry(hist_frame2, "mutaucut / NotTriggeredCutflow (dashed light blue)", "l");
            legend4->AddEntry(hist_frame3, "taucut + IDcut (solid dark green)", "l");
            legend4->AddEntry(hist_frame4, "mutaucut + IDcut (dashed light green)", "l");
            legend4->AddEntry(hist_frame5, "taucut + IDcut + Ptcut (solid dark orange)", "l");
            legend4->AddEntry(hist_frame6, "mutaucut + IDcut + Ptcut (dashed light orange)", "l");
            legend4->Draw();

            
            canvas4->SaveAs(Form("output/compare %d.png", mass)); // 결과 저장
            std::cout << "Third frame comparison histogram saved as 'ptcut_ratio_WR" << mass << ".png'." << std::endl;

            TCanvas *canvas5 = new TCanvas(Form("canvas5_WR%d", mass), "compare with each ratio", 1600, 1200);
            hist_frame7->SetLineColor(kOrange + 7); // 진한 주황
            double fixed_max_value = 0.025; // 원하는 최댓값으로 설정
            hist_frame7->SetMaximum(fixed_max_value); // 최댓값 고정
            hist_frame7->Draw();


            TLegend *legend7 = new TLegend(0.7, 0.7, 0.9, 0.9); // 범례 위치 설정
            legend7->AddEntry(hist_frame7, "(mutaucut - taucut)/taucut ", "l");
            legend7->Draw();

            canvas5->SaveAs(Form("output/twotriggercompare%d.png", mass)); // 결과 저장

            std::cout << "Third frame comparison histogram saved as '(mutaucut - taucut)/taucutoutput/_WR" << mass << ".png'." << std::endl;      
            
        }
    }
    

    
