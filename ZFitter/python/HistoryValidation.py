#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
import os
import subprocess
import stat
import sys
from os import popen
import sched,time
from time import gmtime,strftime
from optparse import OptionParser
from BatchValidation import HistoryStability as hs
from BatchValidation import InitCalibration as ic

def get_options():

    parser = OptionParser()

    parser.add_option( "-q", "--queue",
                       dest="queue", default='cmscaf1nd',
                       help="""
                       Specifies which queue to submit jobs to. Default is cmscaf1nh.
                       """)
    parser.add_option( "-c", "--configFile",
                       dest='configFile', default='',
                       help="""
                       Input configuration file that contains the input n-tuples, and PU info.
                       This will look inside data/validation/ files should be placed there.
                       """,
                       metavar="FILE")
    parser.add_option( "-r", "--runRange",
                       dest="runRangesFile", default='',
                       help="""
                       Input configuration file that contains the run ranges.
                       This will look inside data/runRanges/ files should be placed there.
                       """,
                       metavar="FILE")
    parser.add_option( "-R", "--regionsFile",
                       dest="regionsFile", default='stability.dat',
                       help="""
                       Input regions file that contains the regions to run over
                       This will look inside data/regions/ files should be placed there.
                       """,
                       metavar="FILE")
    parser.add_option( "-i", "--invMass",
                       dest="invMass", default='invMass_SC_corr',
                       help="""
                       Invariant mass variable name.
                       """)
    parser.add_option( "-s","--selection",
                       dest="selection",default="loose25nsRun2",
                       help="""
                       Specifies the selection to be used. Default is loose25nsRun2
                       """)
    parser.add_option( "-d","--dryRun",
                       action="store_true",dest="dryRun",
                       help="""
                       Activates dry run mode and does not submit anything to the batch
                       """)
    parser.add_option( "-m","--monitorMode",
                       action="store_true",dest="monitoringMode",
                       help="""
                       Activates monitoring mode. Does not create and submit jobs, just looks at status of running jobs.
                       """)
    parser.add_option("-n","--interval",
                      dest="interval",default="100000",
                      help="""
                      Interval to divide runs over: min events in each run division(approx.)
                      """)

    return parser.parse_args()


if __name__ == '__main__':

    (opt, args) =  get_options()

    queue = opt.queue
    regionsFile=opt.regionsFile
    runRangesFile = opt.runRangesFile
    configFile = opt.configFile
    selection = opt.selection
    invMass = opt.invMass
    dryRun = opt.dryRun
    monitoringMode = opt.monitoringMode
    baseDir = configFile.split('.')[0]+'-Batch/'
    interval = int(opt.interval)


    print "Run details:"
    print "Queue: ",queue
    print "Regions file: ",regionsFile
    print "Config file: ",configFile
    print "Selection: ",selection
    print "Inv. mass: ",invMass
    print "Dry run: ", dryRun
    print "Monitoring mode: ",monitoringMode
    if runRangesFile == '':
        print "Runranges file: to be generated"
    else:
        print "Runranges file: ",runRangesFile
    print "Base dir: ",baseDir
    print "Interval: ",interval

    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    #Make pileup stuff and runranges file
    if not monitoringMode and runRangesFile=='':
        print "Making PU histograms..."
        ic.make_pu_histograms(config='data/validation/'+configFile)
        print "Making PU trees..."
        ic.make_pu_trees(config='data/validation/'+configFile)
        print "Making run divisions..."
        ic.run_divide(config='data/validation/'+configFile,interval=interval)
        runRangesFile = configFile.split('.')[0]+'_interval_'+str(interval)+'.dat'

    #Making the split runrange files in tmp
    splitFiles = hs.createSplitRunRangeFiles(runRangesFile=runRangesFile)

    #Creating the output directories
    outDirData,outDirMC = hs.createOutputDirectories(baseDir=baseDir,configFile=configFile,
                                selection=selection,invMass=invMass)

    #Creating the job scripts
    splitScripts = hs.createSplitRunScripts(splitFiles=splitFiles,configFile=configFile,
                                        baseDir=baseDir,outDirMC=outDirMC,invMass=invMass,
                                        outDirData=outDirData,regionsFile=regionsFile,
                                        extraOptions='',selection=selection)
    if dryRun:
        sys.exit(0)
                                        
    #Submitting the jobs
    if not monitoringMode:
        jobNames = hs.submitSplitRunScripts(splitScripts=splitScripts,queue=queue,dryRun=dryRun)
    else:
        jobNames = hs.submitSplitRunScripts(splitScripts=splitScripts,queue=queue,dryRun=True)

    #Monitor the jobs and resubmit when they fail
    checkPeriod = 300.0
    starttime = time.time()
    if monitoringMode:
        complete = hs.monitorJobs(jobNames,splitScripts,outDirMC,outDirData,verbose=True,dryRun=dryRun,regionsFile=regionsFile,queue=queue)
    else:
        complete = False
    while not complete:
        time.sleep(checkPeriod - ((time.time() - starttime) % checkPeriod))
        print 'Checking jobs at ', strftime("%H:%M:%S", gmtime())
        complete = hs.monitorJobs(jobNames,splitScripts,outDirMC,outDirData,verbose=True,dryRun=dryRun,regionsFile=regionsFile,queue=queue)

    #Make the stability .tex table
    if complete:
        print "Jobs are all done! Time to make the table..."
        tableName = hs.makeTable(runRangesFile=runRangesFile,outDirMC=outDirMC,outDirData=outDirData,
                                   invMass=invMass,selection=selection,regionsFile=regionsFile,extraOptions='')

