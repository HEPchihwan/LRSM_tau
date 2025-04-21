import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. CSV 파일 읽기 및 열 이름 재지정
df = pd.read_csv("../result/calculated_ordered_kfactor.csv")
df.columns = ['LO_Filename', 'LO_CrossSection', 'LO_Error',
              'NLO_Filename', 'NLO_CrossSection', 'NLO_Error', 'Ratio']

# 2. LO와 NLO Cross Section 값을 숫자형으로 변환
df['LO_CrossSection'] = pd.to_numeric(df['LO_CrossSection'], errors='coerce')
df['NLO_CrossSection'] = pd.to_numeric(df['NLO_CrossSection'], errors='coerce')

# 3. LO_Filename에서 WR와 N 값 추출 함수 정의
def extract_wr_n(filename):
    # 예: "condorfiles/LO/result_WR1000_N100/WRtoNLtoLLJJ_WR1000_N100.log"
    m = re.search(r"WR(\d+)_N(\d+)", filename)
    if m:
        return int(m.group(1)), int(m.group(2))
    else:
        return None, None

# 4. WR와 N 컬럼 추가
df[['WR', 'N']] = df['LO_Filename'].apply(lambda x: pd.Series(extract_wr_n(x)))

# 5. WR, N 값이 없는 행 제거 및 타입 정리
df = df.dropna(subset=['WR', 'N'])
df['WR'] = df['WR'].astype(int)
df['N'] = df['N'].astype(int)

# 6. 그룹 지정 함수 (원하는 세 그룹: N100, WR/2, WR-100)
def assign_group(row):
    wr = row['WR']
    n = row['N']
    if n == 100:
        return "N100"
    elif n == wr / 2:
        return "WR/2"
    elif n == wr - 100:
        return "WR-100"
    else:
        return "Other"

# 7. 각 행에 그룹 부여 후, 원하는 그룹만 필터링 (만약 WR/2 그룹이 없는 경우는 건너뜀)
df['Group'] = df.apply(assign_group, axis=1)
df_plot = df[df['Group'].isin(["N100", "WR/2", "WR-100"])].copy()

# 8. 동일한 WR와 그룹 조합에 대해 여러 값이 있다면 평균으로 집계
grouped_plot = df_plot.groupby(['WR', 'Group']).agg(
    LO_CrossSection=('LO_CrossSection', 'mean'),
    NLO_CrossSection=('NLO_CrossSection', 'mean')
).reset_index()

# 9. LO Cross Section 플로팅
plt.figure(figsize=(8, 6))
for grp in ["N100", "WR/2", "WR-100"]:
    data = grouped_plot[grouped_plot['Group'] == grp].sort_values('WR')
    if data.empty:
        continue  # 해당 그룹 데이터가 없으면 건너뜀
    # 각 WR마다 한 점씩 찍음 (예: WR1000에서 N100, WR/2, WR-100에 해당하는 점)
    plt.plot(data['WR'], data['LO_CrossSection'], marker='$L$', label=grp+"_LO")
    plt.plot(data['WR'], data['NLO_CrossSection'], marker='$N$',label=grp+"_NLO")
plt.xlabel("WR [GeV]")
plt.ylabel("Cross Section [pb]")
plt.title("Cross Section ")
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.savefig("../result/LOxec.png")
"""""
# 10. NLO Cross Section 플로팅
plt.figure(figsize=(8, 6))
for grp in ["N100", "WR/2", "WR-100"]:
    data = grouped_plot[grouped_plot['Group'] == grp].sort_values('WR')
    if data.empty:
        continue
    plt.plot(data['WR'], data['NLO_CrossSection'], marker='o', label=grp)
plt.xlabel("WR")
plt.ylabel("NLO Cross Section")
plt.title("NLO Cross Section ")
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.savefig("../result/NLOxec.png")
"""