from WMCore.Configuration import Configuration
config = Configuration()

name = 'MJA_8010_NoMetCut_Run2016G_PRV1'
proc = 'JetHT_Version11'
dataset = '/JetHT/Run2016G-PromptReco-v1/MINIAOD'

# GENERAL
config.section_("General")
config.General.requestName = name+"_"+proc
config.General.workArea    = '/user/ndaci/CRABBY/StudyHLT/Monojet/'+name+'/'+proc+'/'
config.General.transferLogs    = True
#config.General.transferOutput = True

# JOB TYPE
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'treeNadir.py'

config.JobType.pyCfgParams = ['isMC=False',
                              'doTrigObj=True',
                              'filterOnHLT=True',
                              'filterHighMETEvents=False',
                              'metCut=50',
                              'applyL2L3Residuals=True',
                              'addQGLikelihood=False',
                              'addPileupJetID=False',
                              'addPuppiJets=False',
                              'addPuppiMET=False',
                              'addEGMSmear=False',
                              'addMETSystematics=False',
                              'useOfficialMETSystematics=False',
                              'addMETBreakDown=True',
                              'addSubstructureCHS=True',
                              'addSubstructurePuppi=False',
                              'miniAODProcess=RECO',
                              'globalTag=80X_dataRun2_Prompt_v8',
                              'outputFileName=tree.root',
                              'nThreads=1',
                              'isCrab=True']

#config.JobType.pyCfgParams = ['applyL2L3Residuals=True','isMC=False','filterOnHLT=False','filterHighMETEvents=True','usePrivateSQlite=True','miniAODProcess=RECO']
#config.JobType.inputFiles = ['Summer15_25nsV6_DATA.db']
config.JobType.allowUndistributedCMSSW = True
#config.JobType.maxMemoryMB      = 2000
config.JobType.numCores         = 1

# INPUT DATA
config.section_("Data")
config.Data.inputDataset = dataset
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 30000
#config.Data.totalUnits  = 1976
config.Data.publication = False
config.Data.publishDBS  = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag = name+"_"+proc
config.Data.ignoreLocality = False # allows to process inputs on CE != site hosting inputs
config.Data.lumiMask = 'Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'

#config.Data.lumiMask = 
#config.Data.runRange = 

#A custom string to insert in the output file name inside the CRAB-created directory path to allow organizing groups of tasks.
#config.Data.prefix =  

# USER
config.section_("User")
#config.User.email = 'nadir.daci@cern.ch'
#config.User.voRole = 
#config.User.voGroup = 'becms'

# GRID
config.section_("Site")
config.Site.storageSite = 'T2_BE_IIHE'
#config.Site.whitelist = ['']
config.Site.blacklist = ['T1_US_FNAL','T2_UA_KIPT','T2_UK_London_Brunel','T2_CH_CSCS','T2_US_*']
