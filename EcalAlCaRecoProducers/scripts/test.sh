#!/bin/bash
GT=80X_dataRun2_Prompt_v8
echo "============================================================"
echo "Script for sandbox validation on a small amount of events   "

#echo "[INFO] Creating a user directory in /tmp"
temp=/tmp/$USER/sandboxValidation
mkdir $temp


dir="Electron-Run2016B"
mkdir $temp/{Single,Double}$dir
singleDir="$temp/Single$dir"
doubleDir="$temp/Double$dir"

myRawDoubleEGFile="root://cms-xrd-global.cern.ch//store/data/Run2016B/DoubleEG/RAW/v2/000/273/730/00000/FC135FA7-9B1F-E611-8960-02163E0146D4.root"
myRawSingleEFile="root://cms-xrd-global.cern.ch//store/data/Run2016B/SingleElectron/RAW/v2/000/273/450/00000/F448588C-4F1A-E611-AEB9-02163E0145B3.root"

if [ ! -f "$temp/myRawDoubleEG.root" ]; then
    echo "File not found!, copying to tmp"
    xrdcp $myRawDoubleEGFile "$temp/myRawDoubleEG.root"
else 
    echo "$temp/myRawDoubleEG.root exists"
fi

if [ ! -f "$temp/myRawSingleE.root" ]; then
    echo "File not found!, copying to tmp"
    xrdcp $myRawSingleEFile "$temp/myRawSingleE.root"
else
    echo "$temp/myRawSingleE.root exists"
fi

myRawDoubleEGFileLocal="$temp/myRawDoubleEG.root"
myRawSingleEFileLocal="$temp/myRawSingleE.root"

#RAW TO RECO STEP
mySingleERecoFilePath="$singleDir/myreco_RAW2DIGI_RECO.root"
myDoubleEGRecoFilePath="$doubleDir/myreco_RAW2DIGI_RECO.root"
if [ ! -f "$mySingleERecoFilePath" ]; then
    echo "$mySingleERecoFilePath doesn't exist"
    cmsDriver.py myreco -s RAW2DIGI,RECO -n 100  --filein="file:$myRawSingleEFileLocal" --data --conditions=$GT --era=Run2_2016  --scenario=pp --processName=reRECO --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --dirout=$singleDir
else
    echo "$mySingleERecoFilePath exists"
fi
if [ ! -f "$myDoubleEGRecoFilePath" ]; then
    echo "myDoubleEGRecoFilePath doesn't exist"
    cmsDriver.py myreco -s RAW2DIGI,RECO -n 100  --filein="file:$myRawDoubleEGFileLocal" --data --conditions=$GT --era=Run2_2016  --scenario=pp --processName=reRECO --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs --dirout=$doubleDir
else
    echo "$myDoubleEGRecoFilePath exists"
fi

#ALCARAW STEP FROM RAW AND RECO
myUncalWFilePath="$singleDir/EcalUncalWElectron.root"
myUncalZFilePath="$doubleDir/EcalUncalZElectron.root"
if [ ! -f "$myUncalWFilePath" ]; then
    echo "$myUncalWFilePath doesn't exist"
    cmsDriver.py myreco -s ALCA:EcalUncalWElectron -n 100 --data --filein="file:$mySingleERecoFilePath" --conditions=$GT --secondfilein="file:$myRawSingleEFile" --dirout=$singleDir --era=Run2_2016  --scenario=pp --processName=alcaRaw --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
else
    echo "$myUncalWFilePath exists"
fi
if [ ! -f "$myUncalZFilePath" ]; then
    echo "$myUncalZFilePath doesn't exist"
    cmsDriver.py myreco -s ALCA:EcalUncalZElectron -n 100 --data --filein="file:$myDoubleEGRecoFilePath" --conditions=$GT --secondfilein="file:$myRawDoubleEGFile" --dirout=$doubleDir --era=Run2_2016  --scenario=pp --processName=alcaRaw --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
else 
    echo "$myUncalZFilePath exists"
fi

#ALCARECO step
myCalWFilePath="$singleDir/EcalCalWElectron.root"
myCalZFilePath="$doubleDir/EcalCalZElectron.root"
if [ ! -f "$myCalWFilePath" ]; then
    echo "$myCalWFilePath doesn't exist"
    cmsDriver.py myreco -s ALCA:EcalCalWElectron -n 100 --data --filein="file:$mySingleERecoFilePath" --conditions=$GT --secondfilein="file:$myRawSingleEFile" --dirout=$singleDir --era=Run2_2016  --scenario=pp --processName=alcaReco --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
else
    echo "$myCalWFilePath exists"
fi
if [ ! -f "$myCalZFilePath" ]; then
    echo "$myCalZFilePath doesn't exist"
    cmsDriver.py myreco -s ALCA:EcalCalZElectron -n 100 --data --filein="file:$myDoubleEGRecoFilePath" --conditions=$GT --secondfilein="file:$myRawDoubleEGFile" --dirout=$doubleDir --era=Run2_2016  --scenario=pp --processName=alcaReco --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
else
    echo "$myCalZFilePath exists"
fi


#RERECO step
myRecalWFilePath="$singleDir/EcalRecalElectron.root"
myRecalZFilePath="$doubleDir/EcalRecalElectron.root"
if [ ! -f "$myRecalWFilePath" ]; then
    echo "$myRecalWFilePath doesn't exist"
    cmsDriver.py myreco -s ALCA:EcalRecalElectron -n 100 --data --conditions=$GT --nThreads=4 --filein="file:$myUncalWFilePath" --dirout=$singleDir --customise_commands="process.options=cms.untracked.PSet(wantSummary=cms.untracked.bool(True))"   --process=RERECO --customise Calibration/EcalAlCaRecoProducers/customRereco.EcalRecal --era=Run2_2016  --scenario=pp --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
else
    echo "$myRecalWFilePath exists"
fi
if [ ! -f "$myRecalZFilePath" ]; then
    echo "$myRecalZFilePath doesn't exist"
    cmsDriver.py myreco -s ALCA:EcalRecalElectron -n 100 --data --conditions=$GT --nThreads=4 --filein="file:$myUncalZFilePath" --dirout=$doubleDir --customise_commands="process.options=cms.untracked.PSet(wantSummary=cms.untracked.bool(True))"   --process=RERECO --customise Calibration/EcalAlCaRecoProducers/customRereco.EcalRecal --era=Run2_2016  --scenario=pp --customise=L1Trigger/Configuration/customiseReEmul.L1TEventSetupForHF1x1TPs 
else
    echo "$myRecalZFilePath exists"
fi

echo "[INFO] NTuples from ALCARECO"
#cmsRun python/alcaSkimming.py isCrab=0 skim=WSkim maxEvents=100 type=ALCARECO files="file:$myCalWFilePath" doTree=3 tagFile=config/reRecoTags/test80x.py doTreeOnly=1 
#cmsRun python/alcaSkimming.py isCrab=0 skim=ZSkim maxEvents=100 type=ALCARECO files="file:$myCalZFilePath" doTree=3 tagFile=config/reRecoTags/test80x.py doTreeOnly=1 

exit 0
