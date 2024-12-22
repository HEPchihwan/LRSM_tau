#include "Wtau_test.h"

void Wtau_test::initializeAnalyzer(){
}

void Wtau_test::executeEvent(){


  AnalyzerParameter param;

  executeEventFromParameter(param);

}

void Wtau_test::executeEventFromParameter(AnalyzerParameter param){
  if(!PassMETFilter()) return;
  FillHist("Not triggered", 0., 1., 10, 0., 10.); // 메트 필터를 통과하지 못했을 경우의 히스토그램
  Event ev = GetEvent();
  
  
  // mu _ tau trigger   -> return 을 사용하면 뮤 타우 트리거단계에서 타우 트리거 까지 가기전에 탈출하므로 retutn 사용하지 않음.
  if((ev.PassTrigger({"HLT_Mu50_v","HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v"}))){
    FillHist("mu_tau", 0., 1., 10, 0., 10.);

    vector<Tau> muTaus = GetTaus("Tight", 0., 2.1);
    std::sort(muTaus.begin(), muTaus.end(), PtComparing);
    if (muTaus.size() != 0){ // tauID 통과하지 못한 경우 탈락
      FillHist("mu_tau",1. ,1. ,10. ,0. ,10. );
      // pt 값이 190이상인 경우만 
      if (muTaus.at(0).Pt() > 190){
        FillHist("mu_tau", 2., 1., 10, 0., 10.);
      }
    }
  }


  // tau _ trigger
  if(!(ev.PassTrigger("HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v")))return;
  else{
    FillHist("tau", 0., 1., 10, 0., 10.); // 타우만을 통과했을 경우의 히스토그램

    vector<Tau> Taus = GetTaus("Tight", 0., 2.1);
    std::sort(Taus.begin(), Taus.end(), PtComparing);
    if (Taus.size() == 0) return; // tauID 통과하지 못한 경우 탈락
    FillHist("tau",1. ,1. ,10. ,0. ,10. );

    // pt 값이 190이상인 경우만 
    if (Taus.at(0).Pt() < 190) return;
    FillHist("tau", 2., 1., 10, 0., 10.);
  }
  



}

Wtau_test::Wtau_test(){

}

Wtau_test::~Wtau_test(){

}


//mutrigger HLT_Mu50_v
//HLT_MediumChargedIsoPFTau180HighPtRelaxedIso_Trk50_eta2p1_v