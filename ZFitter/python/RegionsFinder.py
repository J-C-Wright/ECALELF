import ROOT
import os
import subprocess
import stat
from os import popen

regionCuts = {
    'EB':'((abs(etaEle[0]) < 1.4222)&&(abs(etaEle[1]) < 1.4222))',
    'EE':'((abs(etaEle[0]) > 1.566 && abs(etaEle[0]) < 2.5)&&(abs(etaEle[1]) > 1.566 && abs(etaEle[1]) < 2.5))',
    'gold':'((R9Ele[0] > 0.94)&&(R9Ele[1] > 0.94))',
    'bad':'((R9Ele[0] > 0.94)&&(R9Ele[1] > 0.94))',
    'EBp':'(etaEle[0]<1.4222)&&(etaEle[1]<1.4222)&&(etaEle[0]>0)&&(etaEle[1]>0)',
    'EBm':'(etaEle[0]>-1.4222)&&(etaEle[1]>-1.4222)&&(etaEle[0]<0)&&(etaEle[1]<0)',
    'EEp':'(etaEle[0]>1.566 && etaEle[0]<2.5)&&(etaEle[1]>1.566 && etaEle[1]<2.5)',
    'EEm':'(etaEle[0]<-1.566 && etaEle[0]>-2.5)&&(etaEle[1]<-1.566 && etaEle[1]>-2.5)',
    '':''
    }

def getFilesFromConfig(path='data/validation/',configFile='',tag=''):
    print 'Getting files from config'

    assert configFile != '', 'Must specify the config file'
    assert (tag == 'd' or tag == 's'), 'Must specify the data/MC tag (d or s)'

    files = []
    with open(path+configFile) as f:
        for line in f.read().split('\n'):
            if line == '': continue
            parts = line.split()
            if tag in parts[0] and parts[1] == 'selected':
                files.append(parts[2])

    f.close()
    return files

def getVarHistogramFromFiles(rootFiles = [],branch = '',bins = 100,isIndexed=False,xmin = None,xmax=None,maxevals=-1,regions = ['']):
    print 'Getting variable histo from root files'

    assert len(rootFiles) != 0,'Must specify files'

    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    if xmin != None and xmax == None:
        _,xmax = getMinMaxFromFiles(rootFiles=rootFiles,branch=branch,isIndexed=isIndexed,maxevals=maxevals)
    elif xmax != None and xmin == None:
        xmin,_ = getMinMaxFromFiles(rootFiles=rootFiles,branch=branch,isIndexed=isIndexed,maxevals=maxevals)
    elif xmax == None and xmin == None:
        xmin,xmax = getMinMaxFromFiles(rootFiles=rootFiles,branch=branch,isIndexed=isIndexed,maxevals=maxevals)

    if bins == -1:
        bins = int(xmax-xmin)

    print "xmin: ",xmin
    print "xmax: ",xmax
    print "bins: ",bins

    for region in regions:
        print region, regionCuts[region]

    varHists = []

    for region in regions:
        if region == '':
            cut = ''
        else:
            cut = regionCuts[region]

        varHist = ROOT.TH1F(branch,'',bins,xmin,xmax)
        for f in rootFiles:
            print f[100:]
            tfile = ROOT.TFile.Open(f)
            tree = tfile.Get('selected')

            if isIndexed:

                print 'drawing hists...'
                tree.Draw(branch+'[0]>>var0('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)
                tree.Draw(branch+'[1]>>var1('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)

                hist0 = ROOT.gROOT.FindObject('var0')
                hist0.SetDirectory(0)

                hist1 = ROOT.gROOT.FindObject('var1')
                hist1.SetDirectory(0)

                print 'adding hists...'
                varHist.Add(hist0)
                varHist.Add(hist1)

            else:

                tree.Draw(branch+'>>var('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)
                hist = ROOT.gROOT.FindObject('var')
                hist.SetDirectory(0)
                varHist.Add(hist)

        varHist.SetDirectory(0)
        varHists.append(varHist)

    return varHists

def getMinMaxFromFiles(rootFiles = [],branch = '',isIndexed=False,maxevals=-1):
    print 'Getting min/max from files'

    assert len(rootFiles) != 0,'Must specify files'

    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    xmin = 9999
    xmax = -9999

    for f in rootFiles:
        print f
        tfile = ROOT.TFile.Open(f)
        tree = tfile.Get('selected')

        if maxevals > 0:
            print "Itterating over ",maxevals," entries..."
        else:
            print "Itterating over ",tree.GetEntries()," entries..."

        count = 0
        for entry in tree:

            count += 1
            if (count % 10000 == 0):
                print count

            temp = eval('entry.'+branch)
            for i in range(2):
                if temp[i] < xmin:
                    xmin = temp[i]
                if temp[i] > xmax:
                    xmax = temp[i]

            if maxevals > 0 and count > maxevals:
                count = 0
                break

    print "Final: ",xmin,xmax
    return [xmin,xmax]


def getIntervals(hist = None,interval = 0):
    print 'Getting intervals'
    
    intervalsSet = []

    for hist in varHists:
        bins = hist.GetNbinsX()

        intervals = [hist.GetXaxis().GetBinLowEdge(0)]

        lowBin = 0
        for i in range(bins):
            if (hist.Integral(lowBin,i) > interval):
                lowBin = i
                intervals.append(hist.GetXaxis().GetBinLowEdge(i))
        intervalsSet.append(intervals)

    return intervalSet

def getRegionsContent(variable = '', regions = [], intervals = []):
    print 'Getting regions content'

    regionStrings = []
    for region in regions:
        if region != '':
            for i in range(len(intervals)-1):
                rString = region+'-'+variable+'_'
                rString += '{:3.3f}_{:3.3f}\n'.format(intervals[i],intervals[i+1])
                regionStrings.append(rString)
        else:
            for i in range(len(intervals)-1):
                rString = variable+'_'
                rString += '{:3.3f}_{:3.3f}\n'.format(intervals[i],intervals[i+1])
                regionStrings.append(rString)

    return regionStrings

def writeRegionsFile(path = 'data/regions/',fileName = '',regionStrings = []):
    print 'Writing regions file'

    assert len(regionStrings) != 0, 'Need to give a list of region strings'
    assert fileName != '', 'Need a file name'

    regionsFile = open(path + fileName,'w')
    for string in regionStrings: 
        regionsFile.write(string)
    regionsFile.close()



#configFile = 'yacine_test.dat'
#branch = 'seedLCSCEle'
#variable = 'LC'
#fileName = 'LC_test.dat'
#bins = 250
#isIndexed = True
#regions = ['','EB','EE']
#xmin = 0.0
#interval=100000
#regions=['','EB','EE']
#maxevals = 10000


#files = getFilesFromConfig(configFile=configFile,tag='d')

#hist = getVarHistogramFromFiles(rootFiles=files,branch=branch,bins=bins,isIndexed=isIndexed,xmin=xmin,maxevals=maxevals,regions=regions)

#intervalsSet = getIntervals(hist=hist,interval=interval)
#for region,intervals in zip(regions,intervalsSet):
#    print region
#    for i in range(len(intervals)-1):
#        print intervals[i], ' to ', intervals[i+1]
#    print

#regionStrings = getRegionsContent(variable=variable,regions=regions,intervals=intervals)

#for string in regionStrings:
#    print string,

#writeRegionsFile(fileName=fileName,regionStrings=regionStrings)


