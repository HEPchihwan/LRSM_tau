import os

WRMASSEND = 500
WRMASS = 200

while WRMASS <= WRMASSEND:
    NMASS = 100
    while NMASS < WRMASS:
        if NMASS == WRMASS:
            NMASS = WRMASS - 100

        DIRNAME = f"WRtoNLtoLLJJ_WR{WRMASS}_N{NMASS}"

        os.makedirs(DIRNAME, exist_ok=True)

        os.system(f"cp skeletons_for_LO_Nother/run_card.dat {DIRNAME}/{DIRNAME}_run_card.dat")
        os.system(f"cp skeletons_for_LO_Nother/extramodels.dat {DIRNAME}/{DIRNAME}_extramodels.dat")

        with open("skeletons_for_LO_Nother/proc_card.dat", "r") as f:
            proclines = f.readlines()

        with open("skeletons_for_LO_Nother/customizecards.dat", "r") as f:
            custolines = f.readlines()

        with open(f"{DIRNAME}/{DIRNAME}_proc_card.dat", "w") as procnew:
            for line in proclines:
                if "###OUTPUT" in line:
                    procnew.write(f"output {DIRNAME} --nojpeg\n")
                else:
                    procnew.write(line)

        with open(f"{DIRNAME}/{DIRNAME}_customizecards.dat", "w") as custonew:
            for line in custolines:
                if "###SETMASS9900012" in line:
                    custonew.write(f"set param_card mass 9900012 {NMASS}\n")
                elif "###SETMASS9900014" in line:
                    custonew.write(f"set param_card mass 9900014 {NMASS}\n")
                elif "###SETMASS9900016" in line:
                    custonew.write(f"set param_card mass 9900016 {NMASS}\n")
                elif "###SETMASS34" in line:
                    custonew.write(f"set param_card mass 34 {WRMASS}\n")
                else:
                    custonew.write(line)

        if NMASS == 100:
            NMASS += 100
        elif NMASS == WRMASS - 200:
            NMASS += 100
        else:
            NMASS += 200

    WRMASS += 200