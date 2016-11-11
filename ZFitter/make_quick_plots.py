roots = [
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016B-ZSkim-Prompt_v2/273150-275376/271036_276811-ICHEP/withExtras2/unmerged-allRange.root"
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016B-ZSkim-Prompt_v2/273150-275376/271036_276811-ICHEP/withExtras/extraCalibTree-unmerged-allRange.root"
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016B-ZSkim-Prompt_v2/273150-275376/271036_276811-ICHEP/withExtras/eleIDTree-unmerged-allRange.root"
    
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016C-ZSkim-Prompt_v2/275420-276283/271036_276811-ICHEP/withExtras2/unmerged-allRange.root"
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016C-ZSkim-Prompt_v2/275420-276283/271036_276811-ICHEP/withExtras/extraCalibTree-unmerged-allRange.root"
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016C-ZSkim-Prompt_v2/275420-276283/271036_276811-ICHEP/withExtras/eleIDTree-unmerged-allRange.root"
    
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016D-ZSkim-Prompt_v2/276315-276811/271036_276811-ICHEP/withExtras2/unmerged-allRange.root"
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016D-ZSkim-Prompt_v2/276315-276811/271036_276811-ICHEP/withExtras/extraCalibTree-unmerged-allRange.root"
    "root://eoscms//eos/cms/store/group/dpg_ecal/alca_ecalcalib/ecalelf/ntuples/13TeV/ALCARERECO/80X_dataRun2_Prompt_v10/DoubleEG-Run2016D-ZSkim-Prompt_v2/276315-276811/271036_276811-ICHEP/withExtras/eleIDTree-unmerged-allRange.root"
]

import ROOT

branch = "invMass_SC_must_regrCorr_ele"

for f in roots:
    fin  =  ROOT.TFile.Open(f)
    c = ROOT.TCanvas("c","c",500,500)
    c.cd()
    tree =  fin.Get("selected")
    tree.Draw("invMass_SC_must_regrCorr_ele>>h(60,80,110)")
    #h = ROOT.gDirectory.Get("h")
    raw_input('...')
    #c.SaveAs("mass_"+branc+"_"+roots.index(f)+".png")
    
