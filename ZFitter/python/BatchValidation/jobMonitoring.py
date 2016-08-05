import os
import subprocess
import stat
from os import popen
from BatchValidation import stability as stab

def monitorJobs(jobNames=[],splitScripts=[],outDirMC='',outDirData='',verbose=False,dryRun=True,regionsFile=''):

    assert (len(jobNames) > 0 and len(splitScripts) > 0), 'Both job names array and scripts array must not be empty'
    assert (len(jobNames) == len(splitScripts)), 'Jobs names array length must equal scripts array length'

    catalog = zip(jobNames,splitScripts)
    bjobs = popen('bjobs').read()

    resub = []
    resubNames = []
    actives = 0
    failed = 0
    finish = 0

    for jobName,splitScript in catalog:
        
        info = ''
        for line in bjobs.split('\n'):
            if len(line.split()) < 7:continue
            if jobName == line.split()[6]:
                info = line

        if verbose : print jobName+' ',
        attributes = info.split()

        active = len(attributes) > 1 and (attributes[2] == 'RUN' or attributes[2] == 'PEND')
        if verbose:
            if active:
                print 'Job is active       |',
            else:
                print 'Job is EXIT or DONE |',

        fileNames = fitresFileNamesFromScriptName(splitScript,regionsFile=regionsFile)
        fileStatuses = []
        progress = ''
        for fileName in fileNames:
            fileExists = os.path.isfile(outDirData+'/fitres/'+fileName)
            fileStatuses.append(fileExists)
            if verbose:
                if fileExists:
                    progress += '-'
                else:
                    progress += ' '
        if verbose:
            print progress,'|',
        
        if active:
            if verbose : print attributes[-1]
            actives += 1
        elif not active and 0 in fileStatuses:
            if verbose : print '<---- This one failed'
            resub.append(splitScript)
            resubNames.append(jobName)
            failed += 1
        else:
            if verbose : print ' Done!'
            finish += 1

    print 'There are ',actives,' active jobs ', failed,
    print ' failed jobs ',finish,' completed jobs out of ',
    print len(jobNames),' total jobs'
    if len(resub) != 0:
        print 'The following are to be resubmitted:'
        for name,script in zip(resubNames,resub):
            print name,' ',script
        stab.submitSplitRunScripts(jobNames= resubNames,splitScripts=resub,queue='cmscaf1nh',dryRun=dryRun)
    else:
        print "No resubmissions needed :)"

    if len(resub) == 0 and finish == len(jobNames):
        return True
    else:
        return False

def fitresFileNamesFromScriptName(scriptName = '',commonCut = 'Et_25',regionsFile='data/regions/stability.dat'):

    assert scriptName != '', 'Script name must not be empty'
    
    runMin = scriptName.split('/')[-1].split('_')[0]
    runMax = scriptName.split('/')[-1].split('_')[1]
    regions = getRegions(regionsFile)
    types = ['.tex','.root','.txt']

    fileNames = []
    for region in regions:
        for type in types:
            name = region+'-runNumber_'+runMin+'_'+runMax+'-'+commonCut+type
            fileNames.append(name)

    return fileNames

def getRegions(regionsFile='data/regions/stability.dat'):
    
    regions = []
    with open(regionsFile) as f:
        for line in f.read().split('\n'):
            if '#' not in line and line != '':
                regions.append(line)
    return regions
 
