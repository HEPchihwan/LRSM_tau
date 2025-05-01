import pyhepmc as hep
import numpy as np
import matplotlib.pyplot as plt
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
lhe_files = sorted(glob.glob(f"{base_path}/result_WR*_N*/cmsgrid_final.lhe"))  # 수정 필요할 수도 있음

output_dir = "./histogram/wr_mass_plots"
os.makedirs(output_dir, exist_ok=True)

for lhe_path in lhe_files:
    label = os.path.basename(os.path.dirname(lhe_path))
    try:
        reco = WRMassReconstructor()
        reco.SetInput(lhe_path)
        reco.SetTargetParticles(9900016, 15)
        reco.Run()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(reco.masses, bins=40, histtype='step', linewidth=1.5)
        ax.set_title(label.replace("_", " "), fontsize=10)
        ax.set_xlabel("M [GeV]", fontsize=10)
        ax.set_ylabel("Events", fontsize=10)
        ax.grid(True)
        ax.tick_params(axis='both', which='major', labelsize=8)

        save_path = os.path.join(output_dir, f"{label}.png")
        plt.savefig(save_path, dpi=200)
        plt.close(fig)  # 리소스 해제 필수

        print(f"✅ Saved: {save_path}")

    except Exception as e:
        print(f"❌ Error processing {label}: {e}")
