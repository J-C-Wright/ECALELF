#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
import os
import pwd
import subprocess
import stat
import sys
from os import popen
import sched,time
from time import gmtime,strftime
from optparse import OptionParser
from distutils.dir_util import copy_tree
from BatchValidation import HistoryStability as hs
from BatchValidation import InitCalibration as ic
from BatchValidation import MonitoringSummary as ms
from BatchValidation import JobHandling as jh
from StabilityPlotter import Plotter as sp
import pandas   as pd
from shutil     import copyfile

def get_options():

    parser = OptionParser()

    parser.add_option( '-q', '--queue',
                       dest='queue', default='cmscaf1nd',
                       help='''
                       Specifies which queue to submit jobs to. Default is cmscaf1nh.
                       ''')
    parser.add_option( '-c', '--configFile',
                       dest='configFile', default='',
                       help='''
                       Input configuration file that contains the input n-tuples, and PU info.
                       This will look inside data/validation/ files should be placed there.
                       ''',
                       metavar='FILE')
    parser.add_option( '-r', '--runRange',
                       dest='runRangesFile', default='',
                       help='''
                       Input configuration file that contains the run ranges.
                       This will look inside data/runRanges/ files should be placed there.
                       ''',
                       metavar='FILE')
    parser.add_option( '-R', '--regionsFile',
                       dest='regionsFile', default='stability.dat',
                       help='''
                       Input regions file that contains the regions to run over
                       This will look inside data/regions/ files should be placed there.
                       ''',
                       metavar='FILE')
    parser.add_option( '-i', '--invMass',
                       dest='invMass', default='invMass_SC_corr',
                       help='''
                       Invariant mass variable name.
                       ''')
    parser.add_option( '-s','--selection',
                       dest='selection',default='loose25nsRun2',
                       help='''
                       Specifies the selection to be used. Default is loose25nsRun2
                       ''')
    parser.add_option( '-d','--dryRun',
                       action='store_true',dest='dryRun',
                       help='''
                       Activates dry run mode and does not submit anything to the batch
                       ''')
    parser.add_option( '-m','--monitorMode',
                       action='store_true',dest='monitoringMode',
                       help='''
                       Activates monitoring mode. Does not create and submit jobs, just looks at status of running jobs.
                       ''')
    parser.add_option('-n','--interval',
                      dest='interval',default='100000',
                      help='''
                      Interval to divide runs over: min events in each run division(approx.)
                      ''')
    parser.add_option('--iovs',
                      dest='iovs_file', default='',
                      help='''
                      List of IOV's to be drawn on the history plots
                      The file should be structured as folowing :
                      | run | date | time | info |
                      ''',
                      metavar='FILE')
 
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


    print 'Run details:'
    print 'Queue: ',queue
    print 'Regions file: ',regionsFile
    print 'Config file: ',configFile
    print 'Selection: ',selection
    print 'Inv. mass: ',invMass
    print 'Dry run: ', dryRun
    print 'Monitoring mode: ',monitoringMode
    if monitoringMode:
        runRangesFile = configFile.split('.')[0]+'_interval_'+str(interval)+'.dat'
    if runRangesFile == '':
        print 'Runranges file: to be generated'
    else:
        print 'Runranges file: ',runRangesFile
    print 'Base dir: ',baseDir
    print 'Interval: ',interval

    #--------------------
    #Preparation
    #--------------------

    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    #Make pileup stuff and runranges file
    if not monitoringMode and runRangesFile=='':
        print 'Making PU histograms...'
        ic.make_pu_histograms(config='data/validation/'+configFile)
        print 'Making PU trees...'
        ic.make_pu_trees(config='data/validation/'+configFile)
        print 'Making run divisions...'
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

    #--------------------
    #Submission
    #--------------------

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

    
    #--------------------
    #Monitoring 
    #--------------------

    checkPeriod = 180.0
    starttime = time.time()
    complete = False

    while not complete:

        print '\n'
        print 'Checking jobs at ', strftime('%H:%M:%S', gmtime())
        id_changes = jh.check_jobs(command_dict=jobs_command_dict,product_dict=jobs_products_dict)

        #If there are changes update the dictionaries and the catalog files
        print 'There are '+str(len(id_changes))+' resubmitted jobs'
        if len(id_changes) > 0:
            print 'Updating...'
            for old_id,new_id in id_changes.iteritems():

                print old_id,'-->',new_id

                jobs_command_dict[new_id] = jobs_command_dict[old_id]
                del jobs_command_dict[old_id]
                jobs_products_dict[new_id] = jobs_products_dict[old_id]
                del jobs_products_dict[old_id]

            jh.update_job_catalogue(baseDir=baseDir,replacement_ids_dict=id_changes,file_name='commands_catalog.dat')
            jh.update_job_catalogue(baseDir=baseDir,replacement_ids_dict=id_changes,file_name='products_catalog.dat')
            
        complete = jh.check_all_complete(command_dict=jobs_command_dict,product_dict=jobs_products_dict)
        if not complete:
            time.sleep(checkPeriod - ((time.time() - starttime) % checkPeriod))

    #--------------------
    #History table
    #--------------------

    print 'Jobs are all done! Time to make the table...'
    tableName = hs.makeTable(runRangesFile=runRangesFile,outDirMC=outDirMC,outDirData=outDirData,
                               invMass=invMass,selection=selection,regionsFile=regionsFile,extraOptions='')

    #make the config file
    config_content = ''
    config_content += outDirData + '/table/' + 'monitoring_stability-'+invMass+'-'+selection+'.tex\t\t'
    config_content += 'data/runRanges/' + runRangesFile + '\t\t'
    config_content += configFile.split('.')[0] + '\t\t'
    config_content += 'Blue\n'

    config_file = open(baseDir+'history_plots.cfg','w')
    config_file.write(config_content)
    config_file.close()
    
    #--------------------
    #History plots
    #--------------------

    #Make plots directory
    plot_path = baseDir+'/HistoryPlots/'+invMass+'_'+selection+'/'
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)

    #Read info from config
    names,runRanges,tables,colours = sp.get_tables_from_config(path=baseDir,config='history_plots.cfg')
    
    #Get regions
    regions = []
    with open('data/regions/'+regionsFile) as rf:
        lines = rf.read().split('\n')
        for line in lines:
            if '#' in line or line == '': continue
            regions.append(line)

    #Get IOVs
    iovs = None
    iovs_file = 'eras_only.dat'
    if os.path.exists('data/iovs/'+iovs_file):
        iovs =  pd.read_csv( 'data/iovs/'+iovs_file ,sep=' ', names = ['run', 'date', 'time', 'playload', 'info'])
    print iovs

    #Making the plots
    print "Starting plotmaking..."
    for region in regions:
        print "Region: ",region

        #Prepare dataframe for each config entry
        dataFrames = []
        for table,runRange in zip(tables,runRanges):
            d = sp.read_run_range(path='data/runRanges/',file=runRangesFile)
            d = sp.append_variables(path=outDirData+'/table/',file='monitoring_stability-'+invMass+'-'+selection+'.tex',data=d,category=region)

            dataFrames.append(d)

        variables = []
        xVars = ['Nevents',
                 'UnixTime',
                 'run_number',
                 'UnixTime_min',
                 'UnixTime_max',
                 'run_min',
                 'run_max',
                 'date_min',
                 'date_max',
                 'time']

        for label in dataFrames[0].columns.values.tolist():
            if 'MC' not in label and label not in xVars and '_err' not in label:
                variables.append(label)

        #Loop over the vars
        for var in variables:
            #Get associated monte carlo info, or a placeholder
            varmc = var.replace('data','MC')

            mc_datasets = []
            mc_errorsets = []
            data_datasets = []
            data_errorsets = []

            for data in dataFrames:
                if 'MC' not in varmc:
                    print "[WARNING] MC counterpart not found for ", var
                    mc_datasets.append([])
                    mc_errorsets.append([])
                else:
                    mc_datasets.append(data[varmc])
                    mc_errorsets.append(data[varmc+'_err'])

                data_datasets.append(data[var])
                data_errorsets.append(data[var+'_err'])

            evenXs = [False,True]
            timevars = ['run_min','time']
            for timevar in timevars:
                for evenX in evenXs:
                    sp.plot_stability( xData = dataFrames[0][timevar], data_datasets = data_datasets,
                                       data_errorsets = data_errorsets, mc_datasets = mc_datasets,
                                       mc_errorsets = mc_errorsets, label = sp.var_labels[var],
                                       category = region, path=plot_path, evenX = evenX,
                                       xVar='', iovs=iovs, names=names,oldStyle=True,colours=colours)
    

    print '...Done! Local plots are in '+baseDir+'/HistoryPlots/'+invMass+'_'+selection+'/'

    
    user = pwd.getpwuid( os.getuid() )[ 0 ]
    www_path = '/afs/cern.ch/user/'+user[0]+'/'+user+'/www/'
    if os.path.exists(www_path):
        print "Making web page..."
        if not os.path.exists(www_path+baseDir.split('-Batch')[0]):
            os.makedirs(www_path+baseDir.split('-Batch')[0])

        print baseDir+'/HistoryPlots/'+invMass+'_'+selection+'/,'+www_path+baseDir.split('-Batch')[0]+'/'
        print '/afs/cern.ch/work/j/jwright/public/index.php'+','+www_path+baseDir.split('-Batch')[0]+'/'+'index.php'

        copy_tree(baseDir+'/HistoryPlots/'+invMass+'_'+selection+'/',www_path+baseDir.split('-Batch')[0]+'/')
        copyfile('/afs/cern.ch/work/j/jwright/public/index.php',www_path+baseDir.split('-Batch')[0]+'/'+'index.php')
        print 'Plots available at http://'+user+'.web.cern.ch/'+user+'/'+baseDir.split('-Batch')[0]+'/'




    #--------------------
    #Slides
    #--------------------












