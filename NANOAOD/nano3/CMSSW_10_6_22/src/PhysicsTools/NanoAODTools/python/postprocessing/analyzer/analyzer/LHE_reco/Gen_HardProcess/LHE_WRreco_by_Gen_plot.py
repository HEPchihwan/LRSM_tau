import os
from ROOT import TCanvas, TH1D, TFile, TLegend, TLatex
from ROOT import kRed, kGreen, kAzure, gStyle

# (1) mWR -> [mN 리스트], 선 색깔 리스트 등 기존 그대로 사용
d_mp = {1000:[100,500,900], 2000:[100,1000,1900], 4000:[100,2000,3900]}
l_col = [kRed+1, kGreen+2, kAzure+2]

# (2) 새로 정의한 사전
d_plots = {
    "not_using_tau_from_N_":     ["WR_mass"],
    "using_tau_from_WR_": ["WR_mass"],
    "onshell_":         ["WR_mass"],
    "off_shell_":        ["secWR_mass"],
    "offshell_":        ["FirstWR_mass"]
}

# 예: 히스토그램 파일들이 있는 디렉토리 (사용 상황에 맞게 수정)
dirname = "/data6/Users/snuintern1/nano3/CMSSW_10_6_22/src/PhysicsTools/NanoAODTools/python/postprocessing/analyzer/analyzer/LHE_reco/Gen_HardProcess/run_result/result/merged_files"

################################################################################
# 메인 루프
################################################################################
for obj in d_plots:          # 새 dictionary에서 "오브젝트"를 반복
    for var in d_plots[obj]: # 오브젝트별로 [pt,eta], 또는 [mass] 등 반복
        for mWR in d_mp:     # mWR 후보들 (1000, 2000, 4000)
            
            # 결과 저장 경로: 기존처럼 mWR별 폴더만 만든 예시
            outdir = f"run_result/fig/signalsample/WR{mWR}"
            os.system(f"mkdir -p {outdir}")

            # 캔버스, 레전드 설정
            c = TCanvas(f"{obj}_{var}_WR{mWR}", "", 1000, 1000)
            l = TLegend(0.5, 0.675, 0.85, 0.875)
            latex = TLatex()
            latex.SetNDC()
            l.SetFillStyle(0)
            l.SetBorderSize(0)

            # 두 번 그리기 위해 먼저 최대 bin 높이를 구하기
            idx = 0
            maxy = []
            for mN in d_mp[mWR]:
                fpath = f"{dirname}/WR{mWR}N{mN}.root"
                f = TFile(f"{dirname}/WR{mWR}N{mN}.root")
                # h = plots/ + obj + _ + var
                # 예: h = f.Get("plots/tau_cut_leading_pt")
                
                h = f.Get(f"plots/{obj}{var}")
                
                
                if obj =="not_using_tau_from_N_":
                    h.GetXaxis().SetTitle("On,Offshell WR Mass Reconstruct")
                    if mWR ==1000: 
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)

                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                
                if obj =="using_tau_from_WR_":
                    h.GetXaxis().SetTitle("Onshell WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                
                if obj =="onshell_":
                    h.GetXaxis().SetTitle("Onshell WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                
                if  obj =="off_shell_":
                    h.GetXaxis().SetTitle("Offshell Second WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                        
                if obj == "offshell_":
                    h.GetXaxis().SetTitle("Offshell First WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*3.0)
                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*3.0)

                
                # 안전장치: 혹시 hist가 없으면 continue
                if not h:
                    print(f"Cannot find histogram: plots/{obj}_{var} in file {dirname}/WR{mWR}N{mN}.root")
                    continue

                # 정규화
                h.Scale(1./h.Integral())
                
                


                # 최대 bin 저장
                maxy.append(h.GetMaximum())

            ####################################################################
            # 실제 그리기(두 번째 루프)
            ####################################################################
            idx = 0
            for mN in d_mp[mWR]:
                fpath = f"{dirname}/WR{mWR}N{mN}.root"
                f = TFile(f"{dirname}/WR{mWR}N{mN}.root")
                
                h = f.Get(f"plots/{obj}{var}")
                
                if obj =="not_using_tau_from_N_":
                    h.GetXaxis().SetTitle("On,Offshell First WR Mass Reconstruct")
                    if mWR ==1000: 
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)

                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                
                if obj =="using_tau_from_WR_":
                    h.GetXaxis().SetTitle("Onshell First WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)

                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                
                if obj =="onshell_":
                    h.GetXaxis().SetTitle("Onshell First,Second WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)

                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)

                if  obj =="off_shell_":
                    h.GetXaxis().SetTitle("Offshell Second WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*1.5)
                        
                if obj == "offshell_":
                    h.GetXaxis().SetTitle("Offshell First WR Mass Reconstruct")
                    if mWR ==1000:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*3.0)
                    else:
                        h.Rebin(10)
                        h.SetTitle("")
                        h.GetXaxis().SetRangeUser(0, mWR*3.0)
                        
                
                h.GetXaxis().SetTitleSize(0.03)
                h.GetXaxis().SetTitleOffset(1.5)

                h.SetDirectory(0)
                h.SetStats(0)
                h.Scale(1./h.Integral())

                h.SetLineColor(l_col[idx])
                h.SetLineWidth(4)

                

                # y축 최대값
                if maxy:
                    h.GetYaxis().SetRangeUser(0, max(maxy)*1.5)
                h.GetYaxis().SetTitle("A.U.")
                h.GetYaxis().SetTitleSize(0.05)
                
                
                
                

                # 레전드에 추가
                l.AddEntry(h, f"m_{{WR}}={mWR} GeV, m_{{N}}={mN} GeV","l")

                c.cd()
                if idx == 0:
                    h.Draw("hist")
                else:
                    h.Draw("hist same")
                
                idx += 1

            ####################################################################
            # CMS 라벨 붙이기
            ####################################################################
            textSize = 0.5*gStyle.GetPadTopMargin()
            latex.SetTextFont(61)
            latex.SetTextSize(textSize)
            latex.DrawLatex(0.2, 0.8, "CMS")
            latex.SetTextFont(52)
            latex.SetTextSize(0.75*textSize)
            latex.DrawLatex(0.2, 0.76, "Simulation")

            # 레전드, 마진 등
            l.Draw()
            c.SetLeftMargin(0.15)
            c.SetBottomMargin(0.1)
            c.Draw()

            # 이미지 저장
            out_png = f"{outdir}/{obj}_{var}.png"
            #out_pdf = f"{outdir}/{obj}_{var}.pdf"
            c.SaveAs(out_png)
            #c.SaveAs(out_pdf)
            print(f"Saved plots: {out_png}")
            #out_pdf