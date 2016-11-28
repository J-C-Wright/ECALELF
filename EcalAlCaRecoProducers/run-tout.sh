json1=RUN2016C-275657-276283
json2=RUN2016D-276315-276811
json3=RUN2016E-276831-277420
json4=RUN2016F-277981-278808

#json1=RUN2016D-276315-276811
#json2=RUN2016E-276831-277420
#json3=RUN2016C-275657-276283
#json4=RUN2016F-277981-278808


jsonName=MiniAOD-LC
tag=config/reRecoTags/80X_dataRun2_Prompt_v10.py
where=caf
for idx in RUN2016D-276315-276811 RUN2016E-276831-277420
do
    name="/afs/cern.ch/work/y/yhaddad/80X_ECALELF_ntuples/JSON_2016/${idx}_13TeV_PromptReco_JSON_NoL1T.txt"
    json="${idx}"
    echo 
    echo $name  # Each planet on a separate line.
    echo "--------------------------------------"
    echo `parseDatasetFile.sh alcareco_datasets.dat | grep $(echo $json | cut -f1 -d-) | grep $(echo $json | cut -f2 -d-)-$(echo $json | cut -f3 -d-)`
    ./scripts/prodNtuples.sh `parseDatasetFile.sh alcareco_datasets.dat | grep $(echo $json | cut -f1 -d-) | grep $(echo $json | cut -f2 -d-)-$(echo $json | cut -f3 -d-)` \
			     --type MINIAOD -t ${tag} \
			     --scheduler=${where} \
			     --json=${name} \
			     --json_name=${jsonName} \
			     --check #reateOnly
done

