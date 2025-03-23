import os
import numpy as np
import matplotlib.pyplot as plt
import uproot
from concurrent.futures import ProcessPoolExecutor, as_completed

def process_file(file_name):
    try:
        with uproot.open(file_name) as file:
            # "Cutflow" 및 "Not triggered/Cutflow" 히스토그램 가져오기
            MET_hist = file["Not triggered"]
            mutau_hist = file["mu_tau"]
            tau_hist = file["tau"]

            # taucut 및 mutaucut 값 추출 (히스토그램의 bin 인덱스 확인 필요)
            MET_hist_value = MET_hist.values()[1]
            
            mutauPTcutvalue = mutau_hist.values()[3]

            tauPTcutvalue = tau_hist.values()[3]

            # 비율 계산
            if MET_hist_value != 0:
                taucutratio = tauPTcutvalue / MET_hist_value
                mutaucutratio = mutauPTcutvalue / MET_hist_value
                compareratio = (mutauPTcutvalue - tauPTcutvalue)/ tauPTcutvalue 
            else:
                taucutratio= 0
                mutaucutratio = 0
                compareratio = 0

            # WR과 N 값 추출 (파일명에서 WR과 N 값을 파싱)
            parts = file_name.split('_')
            WR_part = parts[3]  # 예: "WR1000"
            N_part = parts[4]   # 예: "N100.root"

            WR = int(WR_part.replace('WR', ''))
            N = int(N_part.replace('N', '').replace('.root', ''))

            return (WR, N, taucutratio, mutaucutratio, compareratio)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_name}")
    except KeyError as e:
        print(f"히스토그램을 찾을 수 없습니다: {file_name}, {e}")
    except Exception as e:
        print(f"파일 처리 중 오류 발생: {file_name}, {e}")
    return None

def plot_heatmaps():
    # 파일 이름 목록 정의
        

    fileNames1000 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1000_N900.root",
        
    ]
    fileNames1500 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR1500_N900.root"
    ]
    fileNames2000 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N1900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2000_N900.root"
    ]
    fileNames2500 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR2500_N900.root"
    ]
    fileNames3000 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N2900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3000_N900.root"
    ]
    fileNames3500 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR3500_N900.root"
    ]
    fileNames4000 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N3900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4000_N900.root"
    ]
    fileNames4500 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N300.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N4400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR4500_N900.root"
    ]
    fileNames5000 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N300.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N4900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5000_N900.root"
    ]
    fileNames5500 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N300.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N400.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N5400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR5500_N900.root"
    ]
    fileNames6000 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N300.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N400.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5500.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N5900.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6000_N900.root"
    ]
    fileNames6500 = [
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N100.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N200.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N300.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N400.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N500.root",
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
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N600.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6000.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6100.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6200.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6300.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N6400.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N700.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N800.root",
        "Wtau_test_WRtoNTautoTauTauJJ_WR6500_N900.root"
    ]

    # 모든 파일 리스트를 하나로 결합
    all_file_names = (
        fileNames1000 + fileNames1500 + fileNames2000 +
        fileNames2500 + fileNames3000 + fileNames3500 +
        fileNames4000 + fileNames4500 + fileNames5000 +
        fileNames5500 + fileNames6000 + fileNames6500
    )

    # 출력 디렉토리 생성
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 히스토그램 데이터를 저장할 리스트
    results = []

    # 병렬 처리 설정
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(process_file, file_name): file_name for file_name in all_file_names}
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    if not results:
        print("유효한 데이터가 없습니다. 스크립트를 종료합니다.")
        exit()

    # WR과 N 값에 따라 데이터 정렬 및 2D 배열 생성
    WR_values = sorted(list(set([res[0] for res in results])))
    N_values = sorted(list(set([res[1] for res in results])))

    # 인덱스 매핑
    WR_to_index = {WR: idx for idx, WR in enumerate(WR_values)}
    N_to_index = {N: idx for idx, N in enumerate(N_values)}

    # 2D 배열 초기화
    taucut_ratios_matrix = np.zeros((len(WR_values), len(N_values)))
    mutaucut_ratios_matrix = np.zeros((len(WR_values), len(N_values)))
    ratio_matrix = np.zeros((len(WR_values), len(N_values)))

    for res in results:
        WR, N, taucutratio, mutaucutratio , compareratio = res
        i = WR_to_index[WR]
        j = N_to_index[N]
        taucut_ratios_matrix[i, j] = taucutratio
        mutaucut_ratios_matrix[i, j] = mutaucutratio
        ratio_matrix[i, j] = compareratio
    # 히트맵 그리기 함수
    def draw_heatmap(data, title, filename, cmap='viridis'):
        plt.figure(figsize=(15, 10))
        plt.imshow(data, aspect='auto', cmap=cmap, origin='lower',
                   extent=[N_values[0]-50, N_values[-1]+50, WR_values[0]-250, WR_values[-1]+250])

        plt.colorbar(label='Ratio')
        plt.xticks(ticks=N_values, labels=[f"N{N}" for N in N_values], rotation=90)
        plt.yticks(ticks=WR_values, labels=[f"WR{WR}" for WR in WR_values])
        plt.title(title)
        plt.xlabel('N Value')
        plt.ylabel('WR Energy (GeV)')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, filename))
        plt.show()

    # 첫 번째 히트맵: taucut_ratios
    draw_heatmap(
        taucut_ratios_matrix,
        'Heatmap of taucut Ratios',
        'heatmap_taucut_ratios.png',
        cmap='viridis'
    )

    # 두 번째 히트맵: mutaucut_ratios
    draw_heatmap(
        mutaucut_ratios_matrix,
        'Heatmap of mutaucut Ratios',
        'heatmap_mutaucut_ratios.png',
        cmap='plasma'
    )

    # 세 번째 히트맵: mutaucut_ratios / taucut_ratios
    draw_heatmap(
        ratio_matrix,
        'Heatmap of taucutratio & mu or taucut Ratios',
        'heatmap_ratio.png',
        cmap='coolwarm'
    )

if __name__ == "__main__":
    plot_heatmaps()