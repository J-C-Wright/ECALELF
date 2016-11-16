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
from BatchValidation import MonitoringSummary as ms
from BatchValidation import JobHandling as jh

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
    if monitoringMode:
        runRangesFile = configFile.split('.')[0]+'_interval_'+str(interval)+'.dat'
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
    history_scripts = hs.createSplitRunScripts( splitFiles=splitFiles,configFile=configFile,
                                                baseDir=baseDir,outDirMC=outDirMC,invMass=invMass,
                                                outDirData=outDirData,regionsFile=regionsFile,
                                                extraOptions='',selection=selection)
    ms_script = ms.createValidationScript( configFile=configFile,baseDir=baseDir,selection=selection,invMass=invMass)

    #Assemble into list
    scripts = history_scripts + [ms_script]

    submission_commands = jh.make_bsub_array(scripts=scripts,queue=queue)

    #Dry run ends here. No need for submission or monitoring 
    if dryRun:
        sys.exit(0)

    if not monitoringMode:

        #Submit and store the job IDs
        jobs_command_dict = jh.submit_jobs(commands=submission_commands,dryRun=dryRun)

        #Associate ids to expected products
        product_keys = []
        product_values = []
        for key,value in jobs_command_dict.iteritems():
            script = value.split()[-1]
            if 'tmp/validations/' in script:
                ms_product_files = ms.expected_products()
                ms_product_files_and_paths = []
                for product_file in ms_product_files:
                    ms_product_files_and_paths.append(outDirData+'/fitres/'+product_file)
                product_values.append(','.join(ms_product_files_and_paths))
            else:
                product_files = hs.fitresFileNamesFromScriptName(script,regionsFile=regionsFile)
                product_files_and_paths = []
                for product_file in product_files:
                    product_files_and_paths.append(outDirData+'/fitres/'+product_file)
                product_values.append(','.join(product_files_and_paths))
            product_keys.append(key)
        jobs_products_dict = dict(zip(product_keys,product_values))

        #Write catalog files
        jh.write_job_catalogue(baseDir=baseDir, job_dict=jobs_command_dict, file_name='commands_catalog.dat')
        jh.write_job_catalogue(baseDir=baseDir, job_dict=jobs_products_dict, file_name='products_catalog.dat')

    else:
        jobs_command_dict=jh.read_job_catalogue(baseDir=baseDir,file_name='commands_catalog.dat')
        jobs_products_dict=jh.read_job_catalogue(baseDir=baseDir,file_name='products_catalog.dat')

    
    #Monitor the jobs
    checkPeriod = 60.0
    starttime = time.time()
    complete = False

    while not complete:

        print '\n'
        print 'Checking jobs at ', strftime("%H:%M:%S", gmtime())
        id_changes = jh.check_jobs(command_dict=jobs_command_dict,product_dict=jobs_products_dict)

        #If there are changes update the dictionaries and the catalog files
        print "There are "+str(len(id_changes))+" resubmitted jobs"
        if len(id_changes) > 0:
            print "Updating..."
            for old_id,new_id in id_changes.iteritems():

                print old_id,'-->',new_id

                jobs_command_dict[new_id] = jobs_command_dict[old_id]
                del jobs_command_dict[old_id]
                jobs_products_dict[new_id] = jobs_products_dict[old_id]
                del jobs_products_dict[old_id]

            jh.update_job_catalogue(baseDir=baseDir,replacement_ids_dict=id_changes,file_name='commands_catalog.dat')
            jh.update_job_catalogue(baseDir=baseDir,replacement_ids_dict=id_changes,file_name='products_catalog.dat')
            
        complete = jh.check_all_complete(job_ids=jobs_command_dict.keys())
        time.sleep(checkPeriod - ((time.time() - starttime) % checkPeriod))

    #If the jobs are complete, make the table
    print "Jobs are all done! Time to make the table..."
    tableName = hs.makeTable(runRangesFile=runRangesFile,outDirMC=outDirMC,outDirData=outDirData,
                               invMass=invMass,selection=selection,regionsFile=regionsFile,extraOptions='')

    #Housekeeping
    output = popen('rm -r LSF*').read()
    print output





