import os
import re
import pandas as pd

# 분석할 경로
base_path = "/data6/Users/snuintern1/genproductions/data"

# cross-section 파싱용 정규식
xsec_pattern = re.compile(r"original cross-section:\s*([0-9eE.+-]+)")
scale_pattern = re.compile(r"scale variation:\s*\+([0-9.eE+-]+)% -([0-9.eE+-]+)%")
pdf_pattern = re.compile(r"PDF variation:\s*\+([0-9.eE+-]+)% -([0-9.eE+-]+)%")

# 결과 저장용 딕셔너리
results = {}

# 파일 순회
for fname in os.listdir(base_path):
    if not fname.endswith(".out"):
        continue

    match = re.match(r"WR(\d+)_N(\d+)_(LO|NLO)\.out", fname)
    if not match:
        continue

    WR, N, mode = int(match[1]), int(match[2]), match[3]
    key = (WR, N)

    with open(os.path.join(base_path, fname), "r") as f:
        content = f.read()

    xsec = xsec_pattern.search(content)
    scale = scale_pattern.search(content)
    pdf = pdf_pattern.search(content)

    # NLO: 마지막 Total cross-section 사용, LO: original cross-section 사용
    if mode == "NLO":
        total_xsecs = re.findall(r"Total cross section:\s*([0-9eE.+-]+)", content)
        xsec_val = float(total_xsecs[-1]) if total_xsecs else None
    else:  # LO
        xsec = re.search(r"original cross-section:\s*([0-9eE.+-]+)", content)
        xsec_val = float(xsec.group(1)) if xsec else None
    scale_str = f"+{scale.group(1)}% / -{scale.group(2)}%" if scale else None
    pdf_str = f"+{pdf.group(1)}% / -{pdf.group(2)}%" if pdf else None

    if key not in results:
        results[key] = {}

    results[key][mode] = {
        "crosssection": xsec_val,
        "scale": scale_str,
        "pdf": pdf_str
    }

# 정렬 및 DataFrame 생성
rows = []
for (WR, N) in sorted(results.keys(), key=lambda x: (x[0], x[1])):
    row = {
        "WR": WR,
        "N": N,
        "LO_crosssection": results[(WR, N)].get("LO", {}).get("crosssection"),
        "LO_scale": results[(WR, N)].get("LO", {}).get("scale"),
        "LO_pdf": results[(WR, N)].get("LO", {}).get("pdf"),
        "NLO_crosssection": results[(WR, N)].get("NLO", {}).get("crosssection"),
        "NLO_scale": results[(WR, N)].get("NLO", {}).get("scale"),
        "NLO_pdf": results[(WR, N)].get("NLO", {}).get("pdf"),
    }
    rows.append(row)

df = pd.DataFrame(rows)
df = df.sort_values(by=["WR", "N"])

# 저장
output_path = "../result/20000event/20000_cross_section_summary.csv"
df.to_csv(output_path, index=False)
print(f"Saved to {output_path}")
