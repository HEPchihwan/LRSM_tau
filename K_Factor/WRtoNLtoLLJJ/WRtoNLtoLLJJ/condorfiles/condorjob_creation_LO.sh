#!/bin/bash
# generate_jobs.sh

# 템플릿 파일 이름
template="template_LO.jds"

# WR 값을 2000부터 6500까지 500 단위로 반복
for WR in {1000..6500..500}; do
    # N 값은 고정값 100, WR의 반, 그리고 WR에서 100을 뺀 값으로 설정
    N_fixed=100
    N_half=$((WR / 2))
    N_WR_minus_100=$((WR - 100))
    
    # 배열에 세 가지 N 값을 저장
    for N in $N_fixed $N_half $N_WR_minus_100; do
        # 출력 파일 이름: 예) WR2000N100.jds, WR2000N1000.jds, WR2000N1900.jds
        outfile="WR${WR}N${N}.jds"
        
        # 템플릿 파일에서 "WR2000"을 "WR${WR}"로, "N100"을 "N${N}"로 전역 치환하여 outfile에 저장
        sed -e "s/WR2000/WR${WR}/g" -e "s/N100/N${N}/g" "$template" > "$outfile"
        
        echo "Generated $outfile"
    done
done