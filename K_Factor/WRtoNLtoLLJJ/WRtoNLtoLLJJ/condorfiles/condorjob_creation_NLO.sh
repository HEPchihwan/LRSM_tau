#!/bin/bash
# generate_jobs.sh

# 템플릿 파일 이름
template="template_NLO.jds"

# WR 값을 2000부터 6500까지 500 단위로 반복
for WR in {1000..6500..500}; do
    # N 값은 고정값 100, WR의 반, 그리고 WR에서 100을 뺀 값으로 설정
    N_fixed=100
    N_half=$((WR / 2))
    N_WR_minus_100=$((WR - 100))
    
    # 각 WR에 대해 세 가지 N 값에 대해 파일 생성
    for N in $N_fixed $N_half $N_WR_minus_100; do
        # 출력 파일 이름: 예) WR2000N100.jds, WR2000N1000.jds, WR2000N1900.jds
        outfile="WR${WR}N${N}_NLO.jds"
        
        # 템플릿 파일에서 "WR2000"을 "WR${WR}"로, "N100"을 "N${N}"로 치환하되, 
        # 이미 템플릿에는 _NLO가 포함되어 있으므로 그대로 두어야 함.
        sed -e "s/WR2000/WR${WR}/g" -e "s/N100/N${N}/g" "$template" > "$outfile"
        
        echo "Generated $outfile"
    done
done