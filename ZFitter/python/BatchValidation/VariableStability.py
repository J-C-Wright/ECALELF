import os
import subprocess
import stat
from os import popen

def createSplitRegionFiles(path = 'data/regions/',regionsFile = ''):

    assert (regionsFile != ''),'File name is empty'

    splitDir = 'tmp/regionSplits/'+regionsFile.split('.')[0]+'/'

    if not os.path.exists(splitDir):
        os.makedirs(splitDir)

    print 'Writing split region files to ',splitDir

    splitNames = []

    with open(path+regionsFile) as f:
        for line in f.read().split('\n'):
            if line != '' and line[0] != '#':

                splitName = line.replace('.','p')+'_split.dat'

                splitFile = open(splitDir+splitName,'w')
                splitFile.write(line)
                splitFile.close()

                splitNames.append(splitDir+splitName)
    f.close()
    return splitNames

def createSplitRegionScripts( splitFiles = [],configPath='data/validation/',
                              configFile = '',invMass = 'invMass_SC_corr',baseDir='',
                              outDirMC = '', outDirData = '',commonCut='Et_25',
                              extraOptions='',selection=''):

    assert (configFile != ''),'validation file name is empty'
    assert (len(splitFiles) != 0),'SplitFiles is empty'
    assert (baseDir != ''),'Base directory string is empty'

    print 'Writing split scripts to ' + '/'.join(splitFiles[0].split('/')[:3])

    scriptNames = []
    for file in splitFiles:

        scriptName = file.replace('.dat','.sh')
        
        scriptNames.append(scriptName)

        #Write the script
        scriptContent = ''
        scriptContent += 'cd ' + os.getcwd().split('Calibration')[0] + '\n'
        scriptContent += 'eval $(scram runtime -sh)\n'
        scriptContent += 'cd Calibration/ZFitter/\n'
        scriptContent += '\n'
    
        #ZFitter command
        scriptContent += './bin/ZFitter.exe'
        scriptContent += ' -f '+configPath+configFile
        scriptContent += ' --regionsFile '+file
        scriptContent += ' --updateOnly'
        scriptContent += ' --invMass_var '+invMass
        scriptContent += ' --commonCut='+commonCut
        scriptContent += ' --selection '+selection
        scriptContent += ' --outDirFitResMC='+outDirMC+'/fitres'
        scriptContent += ' --outDirFitResData='+outDirData+'/fitres'
        scriptContent += ' --outDirImgMC='+outDirMC+'/img'
        scriptContent += ' --outDirImgData='+outDirData+'/img'

        if extraOptions != '':
            scriptContent += ' ' + extraOptions
        scriptContent += '\n'

        #Write to the script file...
        splitFile = open(scriptName,'w')
        splitFile.write(scriptContent)
        splitFile.close()

    return scriptNames

def createOutputDirectories(baseDir='',configFile='',selection='',invMass='',configPath='data/validation/'):

    validation = configFile.split('.')[0]
    if not os.path.exists(baseDir):
        os.makedirs(baseDir)
    #Data directories
    outDirData = baseDir+'dato/'+configFile.split('.')[0]+'/'+selection+'/'+invMass+'/'
    if not os.path.exists(outDirData):
        os.makedirs(outDirData)
    if not os.path.exists(outDirData+'fitres'):
        os.makedirs(outDirData+'fitres')
    if not os.path.exists(outDirData+'img'):
        os.makedirs(outDirData+'img')
    if not os.path.exists(outDirData+'table'):
        os.makedirs(outDirData+'table')
    if not os.path.exists(outDirData+'log'):
        os.makedirs(outDirData+'log')

    #MC directories
    mcName,puName = getMCNameAndPUName(configFile=configFile)
    outDirMC = baseDir+'/MC/'+mcName+'/'+puName+'/'+selection+'/'+invMass+'/'
    if not os.path.exists(outDirMC):
        os.makedirs(outDirMC)
    if not os.path.exists(outDirMC+'fitres'):
        os.makedirs(outDirMC+'fitres')
    if not os.path.exists(outDirMC+'img'):
        os.makedirs(outDirMC+'img')

    return [outDirData,outDirMC]


def getMCNameAndPUName(configPath = 'data/validation/',configFile = ''):

    #MC directories
    with open(configPath+configFile) as f:
        mcFiles = []
        puFiles = []
        for line in f.read().split('\n'):
        #Get MC name from config
            if len(line.split()) == 0: continue
            if 's' in line.split()[0] and line.split()[1] == 'selected':
                mcFiles.append(line.split()[2])

        #Get PU name from config
            if len(line.split()) == 0: continue
            if 'd' in line.split()[0] and line.split()[1] == 'pileupHist':
                puFiles.append(line.split()[2])

        assert len(mcFiles) == 1, '[ERROR] Too many or no MC files in config'
        mcName = mcFiles[0].split('/')[-1]
        mcName = mcName.replace('.root','')
        assert len(puFiles) == 1, '[ERROR] Too many or no PU files in config'
        puName = puFiles[0].split('/')[-1]
        puName = puName.replace('.root','')

    f.close()
    return [mcName,puName]


def createWhichMC(outDirData='',baseDir='',configFile='',selection='',invMass='',configPath='data/validation/'):
        mcName,puName = getMCNameAndPUName(configFile=configFile)
        whichMC = open(outDirData+'whichMC.txt','w')
        whichMC.write(baseDir+'/MC/'+mcName+'/'+puName+'/'+selection+'/'+invMass+'/')
        whichMC.close()


def submitSplitRegionScripts(jobNames = [],splitScripts = [],queue='1nh',dryRun=False):

    assert len(splitScripts) > 0, 'No scripts to submit to batch!!'

    print 'There are ', len(splitScripts),' jobs to be submitted.'
    cwd = os.getcwd()+'/'
    jobs = []

    for i,script in enumerate(splitScripts):

        #chmod
        os.chmod(cwd+script,0744)

        #Build command
        command = ''
        command += 'bsub'
        command += ' -R "pool>30000" -q '+queue
        if len(jobNames) == 0:
            command += ' -J Split'+str(i)
        else:
            command += ' -J '+jobNames[i]
        command += ' < '+cwd+'/'+script

        #Submit command
        if len(jobNames) == 0:
            jobs.append('Split'+str(i))
        else:
            jobs.append(jobNames[i])

        if not dryRun:
            output = popen(command).read()
            print output

    return jobs


def makeTable(runRangesDir = 'data/runRanges/',commonCut='Et_25',outDirMC='',outDirData='',invMass = '',selection='',regionsPath='data/regions/',regionsFile='',extraOptions=''):

    assert regionsFile != '', 'Must specify the regions file'

    command = ''
    command += './script/makeTable.sh'
    command += ' --regionsFile ' + regionsPath+regionsFile
    command += ' --commonCut ' + commonCut
    command += ' --outDirFitResMC ' + outDirMC + '/fitres'
    command += ' --outDirFitResData ' + outDirData + '/fitres'
    if extraOptions != '':
        command += ' ' + extraOptions
    command += ' > ' + outDirData + '/table/' + regionsFile.split('.')[0] + '-'+invMass+'-'+selection+'.tex'

    print command
    
    os.chmod(os.getcwd()+'/script/makeTable.sh',0744)

    popen(command)

    return regionsFile.split('.')[0] + '-'+invMass+'-'+selection+'.tex'

def monitorJobs(jobNames=[],splitScripts=[],outDirMC='',outDirData='',verbose=False,dryRun=True,regionsPath='data/regions/',regionsFile=''):

    assert regionsFile != '', 'Must specify the regions file'
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

        fileNames = fitresFileNamesFromScriptName(splitScript)
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
        submitSplitRegionScripts(jobNames= resubNames,splitScripts=resub,queue='cmscaf1nh',dryRun=dryRun)
    else:
        print "No resubmissions needed :)"

    if len(resub) == 0 and finish == len(jobNames):
        return True
    else:
        return False

def fitresFileNamesFromScriptName(scriptName = '',commonCut = 'Et_25'):

    assert scriptName != '', 'Script name must not be empty'
    
    types = ['.tex','.root','.txt']

    fileNames = []
    
    for t in types:
        name = scriptName.split('/')[-1].split('_split')[0] + '-' + commonCut + t
        fileNames.append(name)

    return fileNames

