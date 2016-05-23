#!/bin/bash
GT=80X_dataRun2_Prompt_v8
echo "============================================================"
echo "Script for sandbox validation on a small amount of events   "


#echo "[INFO] Creating a user directory in /tmp"

#myRawFile=`das_client --query="file dataset=/DoubleEG/Run2016B-v2/RAW" --limit 1 | grep store`
myRawFile="/store/data/Run2016B/SingleElectron/RAW/v2/000/273/450/00000/F448588C-4F1A-E611-AEB9-02163E0145B3.root"

#cmsDriver.py myreco -s RAW2DIGI,RECO -n 100  --filein=$myRawFile --data --conditions=$GT --era=Run2_2016  --scenario=pp --processName=reRECO --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --dirout=$PWD
myRecoFile="file:myreco_RAW2DIGI_RECO.root"

#ALCARAW step
#cmsDriver.py myreco -s ALCA:EcalUncalWElectron -n 100 --data --filein=$myRecoFile --conditions=$GT --secondfilein=$myRawFile --dirout=$PWD --era=Run2_2016  --scenario=pp --processName=alcaRaw --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
myUncalWFile="file:EcalUncalWElectron.root"

#ALCARECO step
#cmsDriver.py myreco -s ALCA:EcalCalWElectron -n 100 --data --filein=$myRecoFile --conditions=$GT --secondfilein=$myRawFile --dirout=$PWD --era=Run2_2016  --scenario=pp --processName=alcaReco --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
myCalWFile="file:EcalCalWElectron.root"

#RERECO step
#echo "[INFO] ALCARERECO Step"
#cmsDriver.py myreco -s ALCA:EcalRecalElectron -n 100 --data --conditions=$GT --nThreads=4 --filein=$myUncalWFile --dirout=$PWD --customise_commands="process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))"   --process=RERECO --customise Calibration/EcalAlCaRecoProducers/customRereco.EcalRecal --era=Run2_2016  --scenario=pp --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 

echo "[INFO] NTuples from ALCARECO"
cmsRun python/alcaSkimming.py isCrab=0 skim=WSkim maxEvents=100 type=ALCARECO files=$myCalWFile doTree=3 tagFile=config/reRecoTags/test80x.py doTreeOnly=1 




#This part is the ntuple production
#echo "[INFO] Running on 100 events, output in $local_dir"
#cmsRun alcaSkimming.py files=file://$local_dir/RAW-RECO.root output=$local_dir/sandbox.root maxEvents=100

#echo "[INFO] Rerecoing with global tag 30Nov (in test.py)"
#cmsRun alcaSkimming.py files=file://$local_dir/sandbox.root output=$local_dir/sandboxRereco.root

#echo "[INFO] Copying official reco file in local"
#xrdcp -v root://eoscms//eos/cms/store/group/alca_ecalcalib/sandbox/rereco30Nov-AOD.root $local_dir

#echo "[INFO] Using reRecoValidation python for validation"
#python reRecoValidation.py AOD > AOD.validationDump
#python reRecoValidation.py sandboxRereco > sandboxRereco.validationDump

#echo "[INFO] Checking the differences"


exit 0



