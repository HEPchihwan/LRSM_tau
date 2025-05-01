import pyhepmc as hep
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

class WRMassReconstructor:
    def __init__(self):
        self.masses = []

    def SetInput(self, input_file):
        self.input = hep.open(input_file)

    def SetTargetParticles(self, id1, id2):
        self.id1 = id1
        self.id2 = id2

    def Run(self):
        for event in self.input:
            p1 = None
            p2 = None
            for p in event.particles:
                if p1 is None and p.pid == self.id1:
                    p1 = p
                elif p2 is None and p.pid == self.id2:
                    p2 = p
            if p1 and p2:
                vec1 = self._get_four_vector(p1.momentum)
                vec2 = self._get_four_vector(p2.momentum)
                mass = self._invariant_mass(vec1, vec2)
                self.masses.append(mass)
        self.input.close()

    @staticmethod
    def _get_four_vector(momentum):
        px, py, pz, E = momentum
        return {"E": E, "px": px, "py": py, "pz": pz}

    @staticmethod
    def _invariant_mass(p1, p2):
        E = p1["E"] + p2["E"]
        px = p1["px"] + p2["px"]
        py = p1["py"] + p2["py"]
        pz = p1["pz"] + p2["pz"]
        return np.sqrt(max(E**2 - px**2 - py**2 - pz**2, 0))


# === 실행 파트 ===
base_path = "/data6/Users/snuintern1/fork_gen_999/submit_files/condorfiles/LO999"
mass_bins = np.linspace(0, 12100, 1210)  # 100 GeV bin width from 0 to 12000
bin_centers = 0.5 * (mass_bins[1:] + mass_bins[:-1])

for wr_mass in range(1000, 6501, 500):  # WR = 1000 to 6500 step 500
    pattern = f"{base_path}/result_WR{wr_mass}_N*/cmsgrid_final.lhe"
    lhe_files = sorted(glob.glob(pattern))
    
    all_hist_data = pd.DataFrame({"mass_bin_center": bin_centers})

    for lhe_path in lhe_files:
        label = os.path.basename(os.path.dirname(lhe_path))  # e.g. result_WR1000_N200
        try:
            reco = WRMassReconstructor()
            reco.SetInput(lhe_path)
            reco.SetTargetParticles(9900016, 15)
            reco.Run()

            hist, _ = np.histogram(reco.masses, bins=mass_bins)
            all_hist_data[label] = hist
            print(f"✅ Processed: {label}")

        except Exception as e:
            print(f"❌ Error processing {label}: {e}")

    # CSV 저장
    output_csv_path = f"WR{wr_mass}_mass_histograms.csv"
    all_hist_data.to_csv(output_csv_path, index=False)
    print(f"\n📁 Saved histogram data to: {output_csv_path}")