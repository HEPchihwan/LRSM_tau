import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# CSV 파일 읽기 (파일 경로를 실제 파일 위치에 맞게 수정)
df = pd.read_csv('../result/calculated_ordered_kfactor.csv')

# 정규표현식을 사용해 WR mass와 N mass 추출 함수
def extract_WR_N(filename):
    m = re.search(r'WR(\d+)_N(\d+)', filename)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None, None

# 각 행의 LO_Filename에서 WR mass와 N mass 추출
df['WR mass'], df['N mass'] = zip(*df['LO_Filename'].apply(extract_WR_N))

# 원하는 열만 선택하고 마지막 열의 이름을 K factor로 변경
new_df = df[['WR mass', 'N mass', 'Row_NLO/LO_Ratio']].rename(columns={'Row_NLO/LO_Ratio': 'K factor'})

# 결과 확인
print(new_df.head())

# 필요시 결과를 새로운 CSV 파일로 저장
new_df.to_csv('../result/extracted_matrix.csv', index=False)

# 피벗 테이블 생성: x축은 WR mass, y축은 N mass, 값은 K factor
heatmap_data = new_df.pivot(index='N mass', columns='WR mass', values='K factor')

# 히트맵 그리기
plt.figure(figsize=(10, 8))
ax = sns.heatmap(heatmap_data, cmap="viridis")
plt.xlabel("WR mass")
plt.ylabel("N mass")
plt.title("K factor")
plt.tight_layout()
plt.gca().invert_yaxis()

# 원하는 y축 라벨과 tick 위치 재설정
desired_y = np.arange(0, 6501, 500)  # 0, 500, 1000, ..., 6500
tick_positions = np.linspace(0, 64, len(desired_y))
plt.yticks(ticks=tick_positions, labels=desired_y)

plt.savefig('../result/heatmap.png')
print("현재 y축 범위:", plt.ylim())


plt.savefig('../result/heatmap.png')
print("현재 x축 범위:", plt.xlim())