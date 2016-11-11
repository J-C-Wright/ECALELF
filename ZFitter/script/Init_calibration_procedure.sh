#! /bin/bash
source script/functions.sh
source script/bash_functions_calibration.sh

file=`basename $1  .dat`

if [[ $1 = "" ]]; then
    echo "you should specify the validation file"; exit;
fi

echo " [yacine] make directories ..."
mkdir -p data/puHistos
mkdir -p data/puTree

echo " [yacine] checking that nothing is inside ..."
rm -rf data/puHistos/*
rm -rf data/puHistos/*

#add branch r9 => not safe in 2016 scenario
##./script/addBranch.sh data/validation/${file}.dat R9Eleprime
#make pileupHist: they are used to make pileupTrees, and also they arerequired for step1
pileupHist
##make pileupTree
pileupTrees
#

if [[ $2 = "" ]]; then
    echo "you should specify the interval if you want to divide the runs"; exit;
fi
interval=$2
echo "Splitting in runNumbers: events ~ $2"
./script/divider_run.sh $file $interval
