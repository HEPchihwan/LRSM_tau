import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import seaborn as sns
from matplotlib.ticker import LogLocator

# Load CSV (replace this path with your actual one)
csv_path = "../result/20000event/20000_cross_section_summary.csv"  
df = pd.read_csv(csv_path)

# Parse scale and pdf variation into numeric up/down values
def parse_variation(var_str):
    if pd.isna(var_str):
        return (0.0, 0.0)
    try:
        up, down = var_str.replace('%', '').split('/')
        return (float(up.replace('+', '').strip()), float(down.replace('-', '').strip()))
    except:
        return (0.0, 0.0)

# Add columns for scale and pdf errors
for mode in ['LO', 'NLO']:
    df[f'{mode}_scale_up'], df[f'{mode}_scale_down'] = zip(*df[f'{mode}_scale'].map(parse_variation))
    df[f'{mode}_pdf_up'], df[f'{mode}_pdf_down'] = zip(*df[f'{mode}_pdf'].map(parse_variation))

# Define target N values
def get_targets(wr):
    return [100, wr // 2, wr - 100]

# Prepare plot data
kfactor_lines = {100: [], 'WR/2': [], 'WR -100': []}
x_vals = {100: [], 'WR/2': [], 'WR -100': []}
lo_lines = {100: [], 'WR/2': [], 'WR -100': []}
nlo_lines = {100: [], 'WR/2': [], 'WR -100': []}
lo_errors = {100: [], 'WR/2': [], 'WR -100': []}
nlo_errors = {100: [], 'WR/2': [], 'WR -100': []}
pdf_errors_lo = {100: [], 'WR/2': [], 'WR -100': []}
pdf_errors_nlo = {100: [], 'WR/2': [], 'WR -100': []}
kfactor_with_error = {'WR': [], 'N': [], 'kfactor': [], 'pdf_err_low': [], 'pdf_err_high': []}


for wr in sorted(df['WR'].unique()):
    for n_type, n_val in zip([100, 'WR/2', 'WR -100'], get_targets(wr)):
        row = df[(df['WR'] == wr) & (df['N'] == n_val)]
        if not row.empty:
            row = row.iloc[0]
            lo = row['LO_crosssection']
            nlo = row['NLO_crosssection']
            if lo and nlo and lo != 0:
                x_vals[n_type].append(wr)
                kfactor_lines[n_type].append(nlo / lo)

            if lo:
                lo_lines[n_type].append(lo)
                lo_errors[n_type].append([
                    lo * row['LO_scale_down'] / 100,
                    lo * row['LO_scale_up'] / 100
                ])
                pdf_errors_lo[n_type].append([
                    lo * row['LO_pdf_down'] / 100,
                    lo * row['LO_pdf_up'] / 100
                ])
            else:
                lo_lines[n_type].append(None)
                lo_errors[n_type].append([0, 0])
                pdf_errors_lo[n_type].append([0, 0])

            if nlo:
                nlo_lines[n_type].append(nlo)
                nlo_errors[n_type].append([
                    nlo * row['NLO_scale_down'] / 100,
                    nlo * row['NLO_scale_up'] / 100
                ])
                pdf_errors_nlo[n_type].append([
                    nlo * row['NLO_pdf_down'] / 100,
                    nlo * row['NLO_pdf_up'] / 100
                ])
            else:
                nlo_lines[n_type].append(None)
                nlo_errors[n_type].append([0, 0])
                pdf_errors_nlo[n_type].append([0, 0])
    for n in [100, wr // 2, wr - 100]:
        row = df[(df['WR'] == wr) & (df['N'] == n)]
        if not row.empty:
            row = row.iloc[0]
            lo = row['LO_crosssection']
            nlo = row['NLO_crosssection']
            if lo and nlo and lo != 0:
                k = nlo / lo
                lo_up = row['LO_pdf_up']
                lo_down = row['LO_pdf_down']
                nlo_up = row['NLO_pdf_up']
                nlo_down = row['NLO_pdf_down']

                # Propagate PDF uncertainty for k = nlo / lo
                k_up = k * np.sqrt((nlo_up / 100)**2 + (lo_down / 100)**2)
                k_down = k * np.sqrt((nlo_down / 100)**2 + (lo_up / 100)**2)

                kfactor_with_error['WR'].append(wr)
                kfactor_with_error['N'].append(n)
                kfactor_with_error['kfactor'].append(k)
                kfactor_with_error['pdf_err_low'].append(k_down)
                kfactor_with_error['pdf_err_high'].append(k_up)

# ----------------------------- Plotting -----------------------------------
# First Plot: K-factor
plt.figure(figsize=(10, 6))
for label, color in zip([100, 'WR/2', 'WR -100'], ['red', 'green', 'blue']):
    if x_vals[label]:
        plt.plot(x_vals[label], kfactor_lines[label], label=f'N={label}', color=color)
plt.xlabel('WR [GeV]')
plt.ylabel('K-factor (NLO/LO)')
plt.title('K-factor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../result/20000event/plot1_kfactor.png")

# Second Plot: LO & NLO Cross-sections (log y)
plt.figure(figsize=(10, 6))
for label, color in zip([100, 'WR/2', 'WR -100'], ['red', 'green', 'blue']):
    if x_vals[label]:
        plt.plot(x_vals[label], lo_lines[label], label=f'LO N={label}', marker='$L$', linestyle='--', color=color)
        plt.plot(x_vals[label], nlo_lines[label], label=f'NLO N={label}', marker='$N$', linestyle='-', color=color)
plt.xlabel('WR [GeV]')
plt.ylabel('Cross-section [pb]')
plt.title('Cross-section vs WR (log scale)')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("../result/20000event/plot2_crosssection_log.png")

# Third Plot: LO with scale/pdf errors
plt.figure(figsize=(10, 6))
delta = 40 
for label, color in zip([100, 'WR/2', 'WR -100'], ['red', 'green', 'blue']):
    xs = np.array(x_vals[label])  
    ys = np.array(lo_lines[label])
    errs = np.array(lo_errors[label]).T
    pdfs = np.array(pdf_errors_lo[label]).T
    if len(xs) > 0:
        plt.errorbar(xs - delta, ys, yerr=errs, label=f'LO N={label} (scale)', fmt='o', color=color, capsize=5)
        plt.errorbar(xs + delta, ys, yerr=pdfs, label=f'LO N={label} (pdf)', fmt='o', color=color, capsize=3, alpha=0.4)
plt.xlabel('WR [GeV]')
plt.ylabel('LO Cross-section [pb]')
plt.title('LO Cross-section with Uncertainty')
plt.legend()
plt.yscale('log')
plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0,), numticks=10))
plt.grid(True)
plt.tight_layout()
plt.savefig("../result/20000event/plot3_lo_with_uncertainties.png")

# Fourth Plot: NLO with scale/pdf errors
plt.figure(figsize=(10, 6))
for label, color in zip([100, 'WR/2', 'WR -100'], ['red', 'green', 'blue']):
    xs = np.array(x_vals[label])  # <--- 요거 꼭 해줘야 함
    ys = np.array(nlo_lines[label])
    errs = np.array(nlo_errors[label]).T
    pdfs = np.array(pdf_errors_nlo[label]).T
    if len(xs) > 0:
        plt.errorbar(xs - delta, ys, yerr=errs, label=f'NLO N={label} (scale)', fmt='s', color=color, capsize=5)
        plt.errorbar(xs + delta, ys, yerr=pdfs, label=f'NLO N={label} (pdf)', fmt='s', color=color, capsize=3, alpha=0.4)

plt.xlabel('WR [GeV]')
plt.ylabel('NLO Cross-section [pb]')
plt.title('NLO Cross-section with Uncertainty')
plt.legend()
plt.yscale('log')
plt.gca().yaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0,), numticks=10))
plt.grid(True)
plt.tight_layout()
plt.savefig("../result/20000event/plot4_nlo_with_uncertainties.png")

# Fifth Plot: kfactro pdf errors

# Convert to DataFrame
kfac_df = pd.DataFrame(kfactor_with_error)

# Plot K-factor with PDF error bars
plt.figure(figsize=(10, 6))
colors = {100: 'red', 'WR/2': 'green', 'WR -100': 'blue'}

plt.figure(figsize=(10, 6))
colors = {100: 'red', 'WR/2': 'green', 'WR -100': 'blue'}

for n_type in [100, 'WR/2', 'WR -100']:
    # N값 결정
    n_val_func = lambda wr: wr // 2 if n_type == 'WR/2' else wr - 100 if n_type == 'WR -100' else 100
    subset = kfac_df[kfac_df.apply(lambda row: row['N'] == n_val_func(row['WR']), axis=1)]
    if not subset.empty:
        WRs = subset['WR']
        K = subset['kfactor']
        low = subset['pdf_err_low']
        high = subset['pdf_err_high']

        plt.plot(WRs, K, marker='o', label=f'N={n_type}', color=colors[n_type])
        plt.fill_between(WRs, low, high, alpha=0.2, color=colors[n_type])

plt.xlabel("WR [GeV]")
plt.ylabel("K-factor (NLO / LO)")
plt.title("K-factor with PDF Uncertainty Band (absolute)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("../result/20000event/plot5_kfactor_pdf_band.png")

#------------------------- 2d plot 

# Placeholder CSV path (update this with actual file path)
csv_path = ("../result/20000event/20000_cross_section_summary.csv")  
df = pd.read_csv(csv_path)

# K-factor 계산
df = df[df['LO_crosssection'] != 0].copy()
df['K factor'] = df['NLO_crosssection'] / df['LO_crosssection']

# 열 이름 정리 (pivot용)
df = df.rename(columns={'WR': 'WR mass', 'N': 'N mass'})

# 피벗 테이블 생성
heatmap_data = df.pivot(index='N mass', columns='WR mass', values='K factor')

# 히트맵 그리기
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap="viridis")
plt.xlabel("WR mass [GeV]")
plt.ylabel("N mass [GeV]")
plt.title("K factor Heatmap")
plt.tight_layout()
plt.gca().invert_yaxis()

# Y축 라벨 재설정
n_mass_values = heatmap_data.index.values
tick_indices = [i for i, val in enumerate(n_mass_values) if val % 500 == 0]
tick_labels = [n_mass_values[i] for i in tick_indices]
plt.yticks(ticks=tick_indices, labels=tick_labels)


plt.savefig("../result/20000event/plot7_kfactor_heatmap.png")

#------------------------- 2d plot xsec
# Placeholder CSV path (update this with actual file path)
csv_path = ("../result/20000event/20000_cross_section_summary.csv")  
df = pd.read_csv(csv_path)

# K-factor 계산
df = df[df['LO_crosssection'] != 0].copy()
df['cross_section'] =  df['LO_crosssection']

# 열 이름 정리 (pivot용)
df = df.rename(columns={'WR': 'WR mass', 'N': 'N mass'})

# 피벗 테이블 생성
heatmap_data = df.pivot(index='N mass', columns='WR mass', values='cross_section')

# 히트맵 그리기
# 로그 스케일로 변환 (0 값 방지 위해 작은 수 추가 또는 filter)
log_heatmap_data = np.log10(heatmap_data)

plt.figure(figsize=(10, 8))
sns.heatmap(log_heatmap_data, cmap="viridis")
plt.xlabel("WR mass [GeV]")
plt.ylabel("N mass [GeV]")
plt.title("log10(Cross-section [pb])")
plt.tight_layout()
plt.gca().invert_yaxis()

# Y축 라벨 재설정
n_mass_values = heatmap_data.index.values
tick_indices = [i for i, val in enumerate(n_mass_values) if val % 500 == 0]
tick_labels = [n_mass_values[i] for i in tick_indices]
plt.yticks(ticks=tick_indices, labels=tick_labels)

plt.savefig("../result/20000event/plot7_xsec_2dplot_log.png")