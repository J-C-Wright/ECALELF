json1=RUN2016C-275657-276283
json2=RUN2016D-276315-276811
json3=RUN2016E-276831-277420
json4=RUN2016F-277981-278808
json5=RUN2016G-278820-280385
json6=RUN2016G-279653-280385
json7=RUN2016H-281613-282037

jsonName=MiniAOD-LC
tag=config/reRecoTags/80X_dataRun2_Prompt_v12.py
where=remoteGlidein #lsf #remoteGlidein #caf
json="${json7}"
name="/afs/cern.ch/work/y/yhaddad/80X_ECALELF_ntuples/JSON_2016/${json}_13TeV_PromptReco_JSON_NoL1T.txt"
echo "name == $name "
echo "check if the JSON file is there"
ls -lthr $name
echo 
echo "--------------------------------------"
echo `parseDatasetFile.sh alcareco_datasets.dat | grep $(echo $json | cut -f1 -d-) | grep $(echo $json | cut -f2 -d-)-$(echo $json | cut -f3 -d-)`
echo " ======= "
./scripts/prodNtuplesCrab3.sh `parseDatasetFile.sh alcareco_datasets.dat | grep $(echo $json | cut -f1 -d-) | grep $(echo $json | cut -f2 -d-)-$(echo $json | cut -f3 -d-)` \
			 --type MINIAOD -t ${tag} \
			 --scheduler=${where} \
			 --json=${name} \
			 --json_name=${jsonName} \
			 --submitOnly #--createOnly # --submitOnly # -s noSkim 
