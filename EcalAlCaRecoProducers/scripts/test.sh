#!/bin/bash
GT=80X_dataRun2_Prompt_v8
echo "============================================================"
echo "Script for sandbox validation on a small amount of events   "

#myRawSingleEFileTest=`das_client --query="file dataset=/DoubleEG/Run2016B-v2/RAW" --limit 1 | sort file.nevents`

#echo "[INFO] Creating a user directory in /tmp"
dir="Electron-Run2016B"
mkdir {Single,Double}$dir
singleDir="Single$dir"
doubleDir="Double$dir"

myRawDoubleEGFile="/store/data/Run2016B/DoubleEG/RAW/v2/000/273/730/00000/FC135FA7-9B1F-E611-8960-02163E0146D4.root"
myRawSingleEFile="/store/data/Run2016B/SingleElectron/RAW/v2/000/273/450/00000/F448588C-4F1A-E611-AEB9-02163E0145B3.root"

#RAW TO RECO STEP
#cmsDriver.py myreco -s RAW2DIGI,RECO -n 100  --filein=$myRawSingleEFile --data --conditions=$GT --era=Run2_2016  --scenario=pp --processName=reRECO --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --dirout=$singleDir
mySingleERecoFilePath="file:$singleDir/myreco_RAW2DIGI_RECO.root"
#cmsDriver.py myreco -s RAW2DIGI,RECO -n 100  --filein=$myRawDoubleEGFile --data --conditions=$GT --era=Run2_2016  --scenario=pp --processName=reRECO --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --dirout=$doubleDir
myDoubleEGRecoFilePath="file:$doubleDir/myreco_RAW2DIGI_RECO.root"

#ALCARAW STEP FROM RAW AND RECO
#cmsDriver.py myreco -s ALCA:EcalUncalWElectron -n 100 --data --filein=$mySingleERecoFilePath --conditions=$GT --secondfilein=$myRawSingleEFile --dirout=$singleDir --era=Run2_2016  --scenario=pp --processName=alcaRaw --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
myUncalWFilePath="file:$singleDir/EcalUncalWElectron.root"
#cmsDriver.py myreco -s ALCA:EcalUncalZElectron -n 100 --data --filein=$myDoubleEGRecoFilePath --conditions=$GT --secondfilein=$myRawDoubleEGFile --dirout=$doubleDir --era=Run2_2016  --scenario=pp --processName=alcaRaw --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
myUncalZFilePath="file:$doubleDir/EcalUncalZElectron.root"

#ALCARECO step
#cmsDriver.py myreco -s ALCA:EcalCalWElectron -n 100 --data --filein=$mySingleERecoFilePath --conditions=$GT --secondfilein=$myRawSingleEFile --dirout=$singleDir --era=Run2_2016  --scenario=pp --processName=alcaReco --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
myCalWFilePath="file:$singleDir/EcalCalWElectron.root"
#cmsDriver.py myreco -s ALCA:EcalCalWElectron -n 100 --data --filein=$myDoubleEGRecoFilePath --conditions=$GT --secondfilein=$myRawDoubleEGFile --dirout=$doubleDir --era=Run2_2016  --scenario=pp --processName=alcaReco --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
myCalZFilePath="file:$doubleDir/EcalCalZElectron.root"

#RERECO step
#cmsDriver.py myreco -s ALCA:EcalRecalElectron -n 100 --data --conditions=$GT --nThreads=4 --filein=$myUncalWFilePath --dirout=$singleDir --customise_commands="process.options=cms.untracked.PSet(wantSummary=cms.untracked.bool(True))"   --process=RERECO --customise Calibration/EcalAlCaRecoProducers/customRereco.EcalRecal --era=Run2_2016  --scenario=pp --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
#cmsDriver.py myreco -s ALCA:EcalRecalElectron -n 100 --data --conditions=$GT --nThreads=4 --filein=$myUncalZFilePath --dirout=$doubleDir --customise_commands="process.options=cms.untracked.PSet(wantSummary=cms.untracked.bool(True))"   --process=RERECO --customise Calibration/EcalAlCaRecoProducers/customRereco.EcalRecal --era=Run2_2016  --scenario=pp --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 

echo "[INFO] NTuples from ALCARECO"
cmsRun python/alcaSkimming.py isCrab=0 skim=WSkim maxEvents=100 type=ALCARECO files=$myCalWFilePath doTree=3 tagFile=config/reRecoTags/test80x.py doTreeOnly=1 


exit 0
