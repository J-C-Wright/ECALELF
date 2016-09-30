import ROOT
import os
import subprocess
import stat
from os import popen

def getFilesFromConfig(path='data/validation/',configFile='',tag=''):

    assert configFile != '', 'Must specify the config file'
    assert (tag == 'd' or tag == 's'), 'Must specify the data/MC tag (d or s)'

    files = []
    with open(path+configFile) as f:
        for line in f.read().split('\n'):
            if line == '': continue
            parts = line.split()
            if tag in parts[0] and parts[1] == 'selected':
                files.append(parts[2])

    return files
    f.close()

def getPUHistogramFromFiles(rootFiles = []):

    assert len(rootFiles) != 0,'Must specify files'

    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    puHist = ROOT.TH1F("pileup","",60,0,60)
    for f in rootFiles:
        tfile = ROOT.TFile.Open(f)
        tree = tfile.Get("selected")
        tree.Draw("nPV+1>>pu(60,0,60)")
        hist = ROOT.gROOT.FindObject("pu")
        hist.SetDirectory(0)
        puHist.Add(hist)

    puHist.SetDirectory(0)
    return puHist

def getPUTrees(path='data/validation/',configFile=''):

    assert configFile != '', 'Must specify the config file'

    numMC = len(getFilesFromConfig(configFile=configFile, tag='s'))
    command = './bin/ZFitter.exe'
    command += ' -f '+path+configFile
    command += ' --regionsFile=data/regions/scaleStep0.dat --saveRootMacro'
    print command
    
    output = popen(command).read()
    print output

    trees = []
    for i in range(numMC):
        trees.append('s'+str(i+1)+'_'+configFile.replace('.dat','.root'))
        command = 'cp tmp/mcPUtrees'+str(i+1)+'.root data/puTree/'
        command += 's'+str(i+1)+'_'+configFile.replace('.dat','.root')
        print command
        output = popen(command).read()

    return trees








configFile='rereco-weights-august.dat'
path = 'data/puHistos/'

datafiles = getFilesFromConfig(configFile=configFile, tag='d')
mcfiles = getFilesFromConfig(configFile=configFile, tag='s')

dataPU = getPUHistogramFromFiles(datafiles)

mcPU = getPUHistogramFromFiles(mcfiles)

dataFile = ROOT.TFile(path+"pu_data_"+configFile.replace('.dat','.root'),"RECREATE")
dataFile.cd()
dataPU.Write()
dataFile.Close()

mcFile = ROOT.TFile(path+"pu_mc_"+configFile.replace('.dat','.root'),"RECREATE")
mcFile.cd()
mcPU.Write()
mcFile.Close()

treeNames = getPUTrees(configFile=configFile)







