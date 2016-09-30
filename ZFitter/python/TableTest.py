#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import stat
import sys
from os import popen
import sched,time
from time import gmtime,strftime
from optparse import OptionParser
from BatchValidation import VariableStability as vs

def get_options():

    parser = OptionParser()

    parser.add_option( "-q", "--queue",
                       dest="queue", default='cmscaf1nh',
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

    return parser.parse_args()


if __name__ == '__main__':

    (opt, args) =  get_options()

    queue = opt.queue
    regionsFile=opt.regionsFile
    configFile = opt.configFile
    selection = opt.selection
    invMass = opt.invMass
    dryRun = opt.dryRun
    monitoringMode = opt.monitoringMode
    baseDir = configFile.split('.')[0]+'-Batch/'
    if opt.runRangesFile == '':
        runRangesFile = configFile.split('.')[0]+'_interval_100000.dat'
        #check it exists
        #if not init calibraition stuff
    else:
        runRangesFile = opt.runRangesFile

    print "Run details:"
    print "Queue: ",queue
    print "Regions file: ",regionsFile
    print "Config file: ",configFile
    print "Selection: ",selection
    print "Inv. mass: ",invMass
    print "Dry run: ", dryRun
    print "Monitoring mode: ",monitoringMode
    print "Runranges file: ",runRangesFile
    print "Base dir: ",baseDir

    #Making the split runrange files in tmp
    outDirData,outDirMC = vs.createOutputDirectories(baseDir=baseDir,configFile=configFile,
                                selection=selection,invMass=invMass)

    tableName = vs.makeTable(regionsFile=regionsFile,outDirMC=outDirMC,outDirData=outDirData,
                               invMass=invMass,selection=selection,extraOptions='')











