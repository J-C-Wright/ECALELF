
cd /afs/cern.ch/work/j/jwright/private/ECAL_31-05-16_New3/CMSSW_7_4_12_patch4/src/

cmsenv

cd Calibration/ZFitter/

FILENAME=July2016
FILE=data/validation/03to22-06-16-GoldJson.dat
INTERVAL=100000

#rm -rf data/puHistos/*
#rm -rf data/puTree/*
#rm -rf tmp/*

#./script/Init_calibration_procedure.sh ${FILE} ${INTERVAL}

./script/stability_split.sh -f data/validation/22-06-2016-GoldJson.dat --runRangesFile data/runRanges/22-06-2016-GoldJson_interval_100000.dat --invMass_var invMass_SC_corr --baseDir 22-06-2016-GoldJson-Batch/ --stability 

