import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV 파일 읽기
df = pd.read_csv("../result/grouped_ratio.csv")  # ['WR', 'Group', 'Avg_Ratio'] 등의 열이 있다고 가정

# 2. 그룹 라벨 매핑 (원하는 레이블로 교체)
group_label_map = {
    "N100": "100",
    "WR/2": r"$m(W_R)/2$",
    "WR-100": r"$m(W_R)-100$"
}

# 3. 그룹별 색상 지정
group_color_map = {
    "N100": "red",
    "WR/2": "green",
    "WR-100": "blue"
}

# 4. 그래프 초기 설정
plt.figure(figsize=(8, 6))
desired_order = ["N100", "WR/2", "WR-100"]

for group_name in desired_order:
    group_data = df[df["Group"] == group_name].sort_values("WR")
    
    label_str = group_label_map.get(group_name, group_name)
    color_str = group_color_map.get(group_name, "black")
    
    plt.plot(
        group_data["WR"],
        group_data["Avg_Ratio"],
        color=color_str,
        linewidth=2,
        label=label_str
    )


# 6. 축 레이블, 제목, 범위 설정
plt.xlabel(r"$m(W_R)\ \mathrm{[GeV]}$", fontsize=14)
plt.ylabel(r"$\frac{\sigma_{\mathrm{NLO}}}{\sigma_{\mathrm{LO}}}$", fontsize=14)

# WR와 비율 값의 범위를 자동 혹은 약간 확장하여 설정
wr_min, wr_max = df["WR"].min(), df["WR"].max()
ratio_min, ratio_max = df["Avg_Ratio"].min(), df["Avg_Ratio"].max()
plt.xlim(wr_min * 0.9, wr_max * 1.1)
plt.ylim(1.15, 1.5)

# 7. 범례 (오른쪽 아래)
plt.legend(loc="lower right", fontsize=12)

# 8. 격자, 레이아웃, 저장
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.savefig("../result/kfactor_plot.png", dpi=300)
plt.show()