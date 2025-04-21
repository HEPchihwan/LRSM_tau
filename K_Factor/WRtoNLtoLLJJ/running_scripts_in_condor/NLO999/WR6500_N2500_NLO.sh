#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/Chihwan-An/genproductions.git
cd genproductions/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJ_WR6500_N2500_NLO cards/NLO999/WRtoNLtoLLJJ_WR6500_N2500_NLO pdmv
ls
mkdir result_WR6500_N2500_NLO
ls
mv *.tar.xz result_WR6500_N2500_NLO
mv *.log result_WR6500_N2500_NLO
cd result_WR6500_N2500_NLO
tar -xavf *.tar.xz
FILE="runcmsgrid.sh"
sed -i 's/5000\*9/20000*9/g' "$FILE"
sed -i 's/: 5000 )/: 20000 )/g' "$FILE"

sed -i 's/10000\*9/20000*9/g' "$FILE"
sed -i 's/: 10000 )/: 20000 )/g' "$FILE"
./runcmsgrid.sh 20000 234567
rm -rf mgbasedir/
