import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import simpson
import os

# === 모델 정의 ===
def double_gauss_exp(x, A1, mu1, sigma1, A2, mu2, sigma2, a, b):
    return (
        A1 * np.exp(-0.5 * ((x - mu1) / sigma1) ** 2) +
        A2 * np.exp(-0.5 * ((x - mu2) / sigma2) ** 2) +
        a  * np.exp(-b * x)
    )

def single_gauss_exp(x, A1, mu1, sigma1, a, b):
    return (
        A1 * np.exp(-0.5 * ((x - mu1) / sigma1) ** 2) +
        a  * np.exp(-b * x)
    )

# === 루프 시작 ===
histogram_dir = "/data6/Users/snuintern1/LRSM_tau/K_Factor/WRtoNLtoLLJJ/analysis/by_siheon/my_example/histogram/data"
csv_output_path = "/data6/Users/snuintern1/LRSM_tau/K_Factor/WRtoNLtoLLJJ/analysis/by_siheon/my_example/histogram/result/fit_results_summary.csv"
plot_output_dir = "/data6/Users/snuintern1/LRSM_tau/K_Factor/WRtoNLtoLLJJ/analysis/by_siheon/my_example/histogram/result/fit_plots/fit_plots"
os.makedirs(plot_output_dir, exist_ok=True)

summary = []

for WR_mass in range(1000, 6501, 500):
    hist_file = f"{histogram_dir}/WR{WR_mass}_mass_histograms.csv"
    if not os.path.exists(hist_file):
        continue

    df = pd.read_csv(hist_file)
    mass_bins = df["mass_bin_center"]

    for N_mass in range(100, WR_mass, 100):
        col = f"result_WR{WR_mass}_N{N_mass}"
        if col not in df.columns:
            continue

        counts = df[col].fillna(0).values
        if counts.sum() == 0:
            continue

        peak_idx = np.argmax(counts)
        mu1_guess = np.clip(mass_bins[peak_idx], WR_mass - 500, WR_mass + 500)
        A1_guess = counts[peak_idx]
        sigma1_guess = 50
        sigma1_guess = np.clip(sigma1_guess, 100, 200)
        a_guess = counts[-1] / 2 if counts[-1] > 0 else 1e-3
        b_guess = 0.002

        mu2_guess = 0
        A2_guess = 0
        sigma2_guess = 100
        fit_type = "single"
        left_mask = (mass_bins < WR_mass * 0.7) & (mass_bins > 100)

        if left_mask.sum() > 0:
            A2_guess = counts[left_mask].max()
            mu2_guess = mass_bins[left_mask].iloc[np.argmax(counts[left_mask])]
            mu2_guess = np.clip(mu2_guess, 10, WR_mass * 0.9 - 10)
            sigma2_guess = np.clip(sigma2_guess, 100, 500)
            fit_type = "double"
            
            if mu2_guess < WR_mass * 0.8:
                mu2_guess = WR_mass * 0.5
                
                
        else:
            fit_type = "single"

        
        print(mu2_guess,"mu2_guess")
        try:
            if fit_type == "double":
                p0 = [A1_guess, mu1_guess, sigma1_guess, A2_guess, mu2_guess, sigma2_guess, a_guess, b_guess]
                bounds = (
                    [0, WR_mass - 1000, 100, 0, 10, 100, 0, 0.00001],
                    [np.inf, WR_mass + 1000, 500, np.inf, WR_mass * 0.9, 1000, np.inf, 0.1]
                )
                popt, _ = curve_fit(double_gauss_exp, mass_bins, counts, p0=p0, bounds=bounds, maxfev=200000)
                A1, mu1, sigma1, A2, mu2, sigma2, a, b = popt
            else:
                p0 = [A1_guess, mu1_guess, sigma1_guess, a_guess, b_guess]
                bounds = (
                    [0, WR_mass - 500, 10, 0, 0.00001],
                    [np.inf, WR_mass + 500, 200, np.inf, 0.1]
                )
                popt, _ = curve_fit(single_gauss_exp, mass_bins, counts, p0=p0, bounds=bounds, maxfev=200000)
                A1, mu1, sigma1, a, b = popt

            x_fit = np.linspace(min(mass_bins), max(mass_bins), 1000)
            gauss1 = A1 * np.exp(-0.5 * ((x_fit - mu1) / sigma1) ** 2)
            expo = a * np.exp(-b * x_fit)
            gauss2 = A2 * np.exp(-0.5 * ((x_fit - mu2) / sigma2) ** 2) if fit_type == "double" else 0
            total_fit = gauss1 + expo + (gauss2 if fit_type == "double" else 0)

            on_shell_events = simpson(gauss1, x_fit)
            off_shell_events = simpson(gauss2, x_fit) if fit_type == "double" else 0
            total_events = counts.sum()

            # ±4σ 범위에서 직접 histogram에서 갯수 추출
            N_sigma = 4
            on_min = mu1 - N_sigma * sigma1
            on_max = mu1 + N_sigma * sigma1
            off_min = mu2 - N_sigma * sigma2 if fit_type == "double" else None
            if off_min <0 :
                off_min = 0
            off_max = mu2 + N_sigma * sigma2 if fit_type == "double" else None
            on_count = counts[(mass_bins >= on_min) & (mass_bins <= on_max)].sum()
            off_count = counts[(mass_bins >= off_min) & (mass_bins <= off_max)].sum() if fit_type == "double" else 0

            # === 그림 저장 ===
            plt.figure(figsize=(8, 5))
            plt.plot(mass_bins, counts, 'o', label="Histogram")
            plt.plot(x_fit, total_fit, '-', label="Fit")
            plt.plot(x_fit, gauss1, '--', label="On-shell")
            if fit_type == "double":
                plt.plot(x_fit, gauss2, '--', label="Off-shell")
            plt.plot(x_fit, expo, ':', label="Exp bkg")
            plt.axvline(on_min, color='green', linestyle=':', label='On-shell ±4σ')
            plt.axvline(on_max, color='green', linestyle=':')
            if fit_type == "double":
                plt.axvline(off_min, color='red', linestyle=':', label='Off-shell ±4σ')
                plt.axvline(off_max, color='red', linestyle=':')
            plt.xlabel("Mass [GeV]")
            plt.ylabel("Events")
            plt.title(f"WR{WR_mass}_N{N_mass}: Mass Fit")
            plt.xticks(np.arange(0, max(mass_bins)+1, 1000))
            plt.grid(True)
            plt.legend()
            plot_path = os.path.join(plot_output_dir, f"WR{WR_mass}_N{N_mass}_fit.png")
            plt.savefig(plot_path)
            plt.close()

            # 결과 기록
            summary.append({
                "WR": WR_mass,
                "N": N_mass,
                "TotalEvents": total_events,
                "OnRange": f"{on_min:.1f}-{on_max:.1f}",
                "OffRange": f"{off_min:.1f}-{off_max:.1f}" if fit_type == "double" else "-",
                "OnShellEvents": on_count,
                "OffShellEvents": off_count
            })

        except Exception as e:
            print(f"❌ Fit failed for WR{WR_mass}_N{N_mass}: {e}")

# CSV 저장
summary_df = pd.DataFrame(summary)
summary_df.to_csv(csv_output_path, index=False)
print(f"✅ 결과 저장 완료: {csv_output_path}")

