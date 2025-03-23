#!/bin/bash

# 병합 결과를 저장할 디렉토리
OUTPUT_DIR="merged_files"
mkdir -p "$OUTPUT_DIR"

# WR 폴더 탐색
find . -mindepth 2 -maxdepth 2 -type d | while read -r subfolder; do
    # 부모 폴더(Wr1000)와 자식 폴더(N100)의 이름 추출
    PARENT_DIR=$(basename "$(dirname "$subfolder")")  # WR1000
    CHILD_DIR=$(basename "$subfolder")               # N100

    # 현재 폴더의 .root 파일 목록 가져오기
    ROOT_FILES=("$subfolder"/*.root)

    # .root 파일이 있는지 확인
    if [[ -f "${ROOT_FILES[0]}" ]]; then
        # 병합 파일 이름: WR1000_N100.root 형식
        OUTPUT_FILE="$OUTPUT_DIR/${PARENT_DIR}${CHILD_DIR}.root"

        # hadd 명령 실행
        echo "Merging files in $subfolder -> $OUTPUT_FILE"
        hadd -f "$OUTPUT_FILE" "${ROOT_FILES[@]}"
    else
        echo "No .root files in $subfolder, skipping."
    fi
done