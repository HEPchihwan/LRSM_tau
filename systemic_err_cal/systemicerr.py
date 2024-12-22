import uproot
import numpy as np
import logging
from ROOT import *
from ROOT import TFile


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 'up'과 'down'을 위한 서브 dtype 정의
sub_dtype = np.dtype([
    ('1', np.float64),
    ('2', np.float64),
    ('3', np.float64),
    ('4', np.float64)
])

# 메인 dtype 정의
dtype = np.dtype([
    ('up', sub_dtype),
    ('down', sub_dtype)
])

# 배열 초기화
bkg_data = np.zeros(16, dtype=dtype)
sig_data = np.zeros(16, dtype=dtype)
fake_data = np.zeros(1, dtype=dtype)
sig_exp_data = np.zeros(1, dtype=dtype)




def group_files_by_keywords(root_file_path, base_name, keywords, data_array):
    logger.info(f"Processing base_name: {base_name}")
    with uproot.open(root_file_path) as root_file:
        file_names = root_file.keys()
        for name in file_names:
            decoded_name = name.decode("utf-8") if isinstance(name, bytes) else name
            if base_name in decoded_name:
                logger.info(f"Processing file: {decoded_name}")
                if base_name in ["signal_SR_ScaleUP", "signal_SR_ScaleDown"]:
                    try:
                        obj = root_file[decoded_name] ## 루트파일안에 있는 데이터를 한번에 가져옴 ( 1, 2, 3, 4 빈 지정할 필요 없음 )
                        values = obj.to_numpy()
                        if "ScaleUP" in decoded_name:
                            data_array[-1]['up'] = values
                            logger.debug(f"Assigned up values for {base_name}")
                        elif "ScaleDown" in decoded_name:
                            data_array[-1]['down'] = values
                            logger.debug(f"Assigned down values for {base_name}")
                    except KeyError:
                        logger.warning(f"Key {decoded_name} not found in ROOT file.")
                else:
                    for i, keyword in enumerate(keywords):
                        if keyword in decoded_name:
                            try:
                                obj = root_file[decoded_name]
                                values = obj.to_numpy()
                                if "2018Up" in decoded_name:
                                    data_array[i]['up'] = values
                                    logger.debug(f"Assigned up values for {keyword}")
                                elif "2018Down" in decoded_name:
                                    data_array[i]['down'] = values
                                    logger.debug(f"Assigned down values for {keyword}")
                            except KeyError:
                                logger.warning(f"Key {decoded_name} not found in ROOT file.")
    return data_array

# 메인 실행
if __name__ == "__main__":
    root_file_path = "WR1000_N300_card_input.root"
    
    base_name_bkg = "bkg_SR"
    base_name_sig = "signal_SR"
    base_name_fake = "fake_SR"

    ## 예외 처리  ( sig 에 추가적으로 하나 더 있음. )
    keyword_exception_sig = [ "signal_SR_ScaleUP","signal_SR_ScaleDown" ]

    keywords_bkg = [
        "ElectroEn", "ElectroID", "ElectroSF", "ElectronRes", "JetEN", "JetRes",
        "MuonEN", "MuonIDSF", "MuonISOSF", "PU", "Prefire", "TauEn", "TauIDSFExt",
        "TauIDSFStat", "TauIDSFSyst", "TauTriggerSF"
    ]
    keywords_sig = keywords_bkg.copy()  # 신호에도 동일한 키워드를 사용 
    keywords_fake = ["TauFRErr"]

    # 배경 데이터 그룹화
    bkg_data = group_files_by_keywords(root_file_path, base_name_bkg, keywords_bkg, bkg_data)
    
    # sig data 

    sig_data = group_files_by_keywords(root_file_path, base_name_sig, keywords_sig, sig_data)
    
    # 페이크 데이터 그룹화
    fake_data = group_files_by_keywords(root_file_path, base_name_fake, keywords_fake, fake_data)
    
    # 예외사항  (Scale Up 및 Scale Down)
    sig_exp_data = group_files_by_keywords(root_file_path, keyword_exception_sig, [], sig_exp_data)
    
    
    # 선택 사항: 로드된 데이터 검증
    logger.info("Background Data:")
    logger.info(bkg_data)
    logger.info("Signal Data:")
    logger.info(sig_data)
    logger.info("Fake Data:")
    logger.info(fake_data)



    orginal = TFile("WR1000_N300_card_input.root")
    bkg_original = [orginal.Get("bkg_SR")[1],orginal.Get("bkg_SR")[2],orginal.Get("bkg_SR")[3] ,orginal.Get("bkg_SR")[4]]

    sig_original = [ orginal.Get("signal_SR")[1],orginal.Get("signal_SR")[2],orginal.Get("signal_SR")[3],orginal.Get("signal_SR")[4]    ]

    fake_original = [ orginal.Get("fake_SR")[1], orginal.Get("fake_SR")[2],orginal.Get("fake_SR")[3] , orginal.Get("fake_SR")[4]]


    ## 나누기 실행 코드 

    ## 나눈 값 저장소 
    bkg_data_up = np.zeros(16, dtype=dtype)
    bkg_data_down = np.zeros(16, dtype=dtype)

    sig_data_up = np.zeros(17, dtype=dtype)
    sig_data_down = np.zeros(17, dtype=dtype)

    fake_data_up = np.zeros(1, dtype=dtype)
    fake_data_down = np.zeros(1, dtype=dtype)

    sig_exp_data_up = np.zeros(1, dtype=dtype)
    sig_exp_data_down = np.zeros(1, dtype=dtype)


    ## 값 나누기 
    for i in range(15):
        for j in range(1,4):
            bkg_data_up[i] = bkg_data['up'][i][j] / bkg_original[i]
            bkg_data_down[i] = bkg_data['down'][i][j] / bkg_original[i]

            sig_data_up[i] = sig_data['up'][i][j] / sig_original[i]
            sig_data_down[i] = sig_data['down'][i][j] / sig_original[i]

    for j in range(1,4):
        fake_data_up[0] = fake_data['up'][0][j] / fake_original[i]
        fake_data_down[0] = fake_data['down'][0][j] / fake_original[i]

        sig_exp_data_up[0] = sig_exp_data['up'][0][j] / sig_original[i]
        sig_exp_data_down[0] = sig_exp_data['down'][0][j] / sig_original[i]

    print ("ok")
    
    





    

