{

  f = new TFile("eta_zee_ecalelf.root","RECREATE");
  chain = new TChain("selected");
  chain->Add ("root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10_PS_v1/DoubleEG-Run2016B-ZSkim-Prompt_v2/273150-275376/271036_276811-ICHEP/withExtras3/DoubleEG-Run2016B-ZSkim-Prompt_v2-273150-275376.root");
  chain->Add("root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10_PS_v1/DoubleEG-Run2016C-ZSkim-Prompt_v2/275420-276283/271036_276811-ICHEP/withExtras3/DoubleEG-Run2016C-ZSkim-Prompt_v2-275420-276283.root");
  chain->Add("root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10_PS_v1/DoubleEG-Run2016D-ZSkim-Prompt_v2/276315-276811/271036_276811-ICHEP/withExtras3/DoubleEG-Run2016D-ZSkim-Prompt_v2-276315-276811.root");
  
  /*
  chain->Draw("etaSCEle[0]>>h_eta_lead_ele_inc(600,-3,3)"   ,"(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25))","colz");
  chain->Draw("etaSCEle[1]>>h_eta_sublead_ele_inc(600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25))","colz");

  chain->Draw("etaSCEle[0]>>h_eta_lead_ele_gold(600,-3,3)"   ,"(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[0]>= 0.94)","colz");
  chain->Draw("etaSCEle[1]>>h_eta_sublead_ele_gold(600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[1]>= 0.94)","colz");

  chain->Draw("etaSCEle[0]>>h_eta_lead_ele_bad(600,-3,3)"   ,"(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[0]< 0.94)","colz");
  chain->Draw("etaSCEle[1]>>h_eta_sublead_ele_bad(600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[1]< 0.94)","colz");

  chain->Draw("etaSCEle[0]>>h_eta_lead_ele_both_gold(600,-3,3)"   ,"(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[0]< 0.94 && R9Ele[1]< 0.94)","colz");
  chain->Draw("etaSCEle[1]>>h_eta_sublead_ele_both_gold(600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[1]< 0.94 && R9Ele[0]< 0.94)","colz");

  chain->Draw("etaSCEle[0]>>h_eta_sublead_ele_not_gold(600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && !(R9Ele[1]>= 0.94 && R9Ele[0]>= 0.94)","colz");
  chain->Draw("etaSCEle[1]>>h_eta_sublead_ele_not_gold(600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && !(R9Ele[1]>= 0.94 && R9Ele[0]>= 0.94)","colz");
  */

  chain->Draw("etaSCEle[0]:etaSCEle[1]>>h2_eta_inc(600,-3,3,600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25))","colz");
  chain->Draw("etaSCEle[0]:etaSCEle[1]>>h2_eta_both_gold(600,-3,3,600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[1]>= 0.94 && R9Ele[0]>= 0.94)","colz");
  chain->Draw("etaSCEle[0]:etaSCEle[1]>>h2_eta_notgold(600,-3,3,600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && !(R9Ele[1]>= 0.94 && R9Ele[0]>= 0.94)","colz");
  chain->Draw("etaSCEle[0]:etaSCEle[1]>>h2_eta_both_bad(600,-3,3,600,-3,3)","(((eleID[0] & 128)==128)&&((eleID[1] & 128)==128))&&((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25)) && (R9Ele[1]< 0.94 && R9Ele[0]< 0.94)","colz");
  
  
  f->Write();
}
