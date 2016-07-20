import os
import subprocess


def createSplitRunRangeFiles(path = 'data/runRanges/',runRangesFile = ''):

    assert (runRangesFile != ''),'File name is empty'

    splitDir = 'tmp/runRangeSplits/'+runRangesFile.split('_interval_')[0]+'/'

    if not os.path.exists(splitDir):
        os.makedirs(splitDir)

    print 'Writing split run range files to ',splitDir

    splitNames = []

    with open(path+runRangesFile) as f:
        for line in f.read().split('\n'):
            if line != '':

                runMin = line.split('\t')[0].split('-')[0]
                runMax = line.split('\t')[0].split('-')[1]

                splitName = runMin+'_'+runMax+'_split.dat'

                splitFile = open(splitDir+splitName,'w')
                splitFile.write(line)
                splitFile.close()

                splitNames.append(splitDir+splitName)
    f.close()
    return splitNames

def createSplitRunScripts(splitFiles = [],configPath='data/validation/',
                          configFile = '',invMass = 'invMass_SC_corr',baseDir='',
                          updateOnly = '--updateOnly', outDirMC = '', outDirData = '',commonCut='Et_25'):

    assert (configFile != ''),'validation file name is empty'
    assert (len(splitFiles) != 0),'SplitFiles is empty'
    assert (baseDir != ''),'Base directory string is empty'

    print 'Writing split scripts to tmp/runRangeSplits/'+configFile.split('.')[0]+'/'

    scriptNames = []
    for file in splitFiles:

        scriptName = file.replace('.dat','.sh')
        
        scriptNames.append(scriptName)

        #Write the script
        scriptContent = ''
        scriptContent += 'cd ' + os.getcwd().split('Calibration')[0] + '\n'
        scriptContent += 'cmsenv\n'
        scriptContent += 'cd Calibration/ZFitter/\n'
        
        scriptContent += '\n'

        #stability_split.sh part...
        scriptContent += './script/stability_split.sh'
        scriptContent += ' -f '+configPath+configFile
        scriptContent += ' --runRangesFile '+file
        scriptContent += ' --invMass_var '+invMass
        scriptContent += ' --baseDir '+baseDir
        scriptContent += ' --stability'
        logname = scriptName.split('/')[-1].replace('.sh','.log')
        scriptContent += ' > '+outDirData+'/log/'+logname
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

def submitSplitRunScripts(splitScripts = []):

    assert len(splitScripts) > 0, 'No scripts to submit to batch!!'

    chmod = 'chmod -R 744 tmp/runRangeSplits/22-06-2016-GoldJson/.'
    process = subprocess.Popen(chmod.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

    for i,script in enumerate(splitScripts):

        #Submit command
        command = ''
        command += 'bsub'
        command += ' -R "pool>30000" -q 1nh'
        command += ' -J StabSplit'+str(i)
        command += ' < '+script

        print 'Command is ',command
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print output




runRangesFile = '22-06-2016-GoldJson_interval_100000.dat'

splitFiles = createSplitRunRangeFiles(runRangesFile=runRangesFile)

invMass = 'invMass_SC_corr'
selection = 'loose'
configFile = '22-06-2016-GoldJson.dat'
baseDir = configFile.split('.')[0]+'-Batch/'

outDirData,outDirMC = createOutputDirectories(baseDir=baseDir,configFile=configFile,
                            selection=selection,invMass=invMass)

splitScripts = createSplitRunScripts(splitFiles=splitFiles,configFile=configFile,
                                    baseDir=baseDir,outDirMC=outDirMC,invMass=invMass,
                                    outDirData=outDirData
                                    )
submitSplitRunScripts(splitScripts)
