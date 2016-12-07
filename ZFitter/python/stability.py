#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys, getopt
from StabilityPlotter  import Plotter as pt
from shutil     import copyfile
from optparse   import OptionParser
from pprint     import pprint
import pandas   as pd

def get_options():
    parser = OptionParser()

    parser.add_option('--iovs',
                      dest='iovs_file', default='',
                      help='''
                      List of IOV's to be drawn on the history plots
                      The file should be structured as folowing :
                      | run | date | time | info |
                      ''',
                      metavar='FILE')
    parser.add_option('-x','--xVar',
                      dest='xVar',default='',
                      help='''
                      Specify whether the plot should be over run range, or regions
                      ''')
    parser.add_option('-d','--output_dir',
                      dest='output_dir',default='',
                      help='''
                      Output directory for the plots
                      ''')
    parser.add_option('-c','--config',
                      dest='config',default='',
                      help='''
                      Config file containing runranges,tables,and names
                      Structure:
                      table path    runrange path   name    colour
                      ''')
    parser.add_option('--oldStyle',action='store_true',
                      dest='oldStyle',default=False,
                      help='''
                      Enable old-style plots with circles and whatever it was
                      ''')

    return parser.parse_args()


if __name__ == '__main__':

    (opt, args) =  get_options()

    assert opt.output_dir      != '', 'No output dir specified'
    assert opt.config          != '', 'No config specified'
    
    if opt.xVar != '':
        print 'x-axis variable is ', opt.xVar
    else:
        print 'x-axis variables are the times/runNumbers'
    
    if not os.path.exists('plot-stability/'):
        os.makedirs('plot-stability/')
    if not os.path.exists('data-stability/'):
        os.makedirs('data-stability/')

    config = opt.config.split('/')[-1]
    path = opt.config.split(config)[0]
    names,runRanges,tables,colours = pt.get_tables_from_config(path = path,config = config)

    for name in names:
        print "name: ",name
    for table in tables:
        print "table: ",table
    for runRange in runRanges:
        print "runRange: ",runRange
    for colour in colours:
        print "colour: ",colour

    plot_path = opt.output_dir

    style = 'classic'

    #Reading regions from the table file
    regions = pt.read_regions_from_table(path='/'.join(tables[0].split('/')[:-1]),tableFile=tables[0].split('/')[-1],xVar=opt.xVar)
    print 'categories :: ', regions

    # reading iov's
    iovs = None
    if os.path.exists(opt.iovs_file):
        iovs =  pd.read_csv( opt.iovs_file ,sep=' ', names = ['run', 'date', 'time', 'playload', 'info'])
    #Make plots
    print 'Starting plotmaking...'

    for region in regions:
        print 'Category: ',region

        #Prepare dataframe for each config entry
        dataFrames = []
        for table,runRange in zip(tables,runRanges):

            path = '/'.join(table.split('/')[:-1])
            rr_path ='/'.join(runRange.split('/')[:-1]) 

            if opt.xVar != '':
                d=pt.parse_table_over_regions(path=path,tableFile=table.split('/')[-1],category=region,xVar=opt.xVar)
                dataFrames.append(d)
            else:
                #Get runrange and time info from the the runranges file
                d = pt.read_run_range(path=rr_path,file=runRange.split('/')[-1])
                #Get variables information from the stability monitoring .tex file
                d = pt.append_variables(path=path,file=table.split('/')[-1],data=d,category=region)
                dataFrames.append(d)

        #Get variables to make plots of (data, not mc or err vars)
        variables = []
        if opt.xVar != '':
            xVars = [opt.xVar+'_min',opt.xVar+'_max',opt.xVar+'_mid']
        else:
            xVars = ['Nevents'     ,
                        'UnixTime'    ,
                        'run_number'  ,
                        'UnixTime_min',
                        'UnixTime_max',
                        'run_min'     ,
                        'run_max'     ,
                        'date_min'    ,
                        'date_max'    ,
                        'time'        ]

        for label in dataFrames[0].columns.values.tolist():
            if 'MC' not in label and label not in xVars and '_err' not in label:
                variables.append(label)


        Delta_m_ranges = { 'EB':(-3,1),
                           'EE':(-3,1),
                           'EB-absEta_0_1':(-2.5,0.5),
                           'EB-absEta_1_1.4442':(-2.5,0.5),
                           'EE-absEta_1.566_2':(-3.5,1.5),
                           'EE-absEta_2_2.5':(-3.5,1.5)
                           }
        sigma_cb_re_ranges = { 'EB':(1.4,3.5),
                               'EE':(1.4,3.5),
                               'EB-absEta_0_1':(1.0,3.0),
                               'EB-absEta_1_1.4442':(1.0,3.0),
                               'EE-absEta_1.566_2':(2.5,3.75),
                               'EE-absEta_2_2.5':(2.5,3.75)
                               }

        #Loop over the vars
        for var in variables:
            print var
            #Get associated monte carlo info, or a placeholder
            varmc = var.replace('data','MC')

            mc_datasets = []
            mc_errorsets = []
            data_datasets = []
            data_errorsets = []

            for data in dataFrames:
                if 'MC' not in varmc:
                    print '[WARNING] MC counterpart not found for ', var
                    mc_datasets.append([])
                    mc_errorsets.append([])
                else:
                    mc_datasets.append(data[varmc])
                    mc_errorsets.append(data[varmc+'_err'])

                data_datasets.append(data[var])
                data_errorsets.append(data[var+'_err'])


            if opt.xVar == '':

                y_range = None
                if var == 'DeltaM_data':
                    y_range = Delta_m_ranges[region]
                elif var == 'rescaledWidth_data':
                    y_range = sigma_cb_re_ranges[region]

                #Plot as function of date or run numbers
                variations = [['run_min',True],
                              ['time',False]]
                for timevar,evenX in variations:
                    
                        pt.plot_stability( xData = dataFrames[0][timevar], data_datasets = data_datasets,
                                           data_errorsets = data_errorsets, mc_datasets = mc_datasets,
                                           mc_errorsets = mc_errorsets, label = pt.var_labels[var],
                                           category = region, path=plot_path, evenX = evenX,
                                           xVar=opt.xVar, iovs=iovs, names=names,style=style,oldStyle=opt.oldStyle,colours=colours,y_range=y_range)
                
            else:
                xvars = [opt.xVar+'_min',opt.xVar+'_max',opt.xVar+'_mid']
                for xvar in xvars:
                    print 'xVar: ' + xvar
                    pt.plot_stability( xData = dataFrames[0][xvar], data_datasets = data_datasets,
                                       data_errorsets = data_errorsets, mc_datasets = mc_datasets,
                                       mc_errorsets = mc_errorsets, label = pt.var_labels[var],
                                       category = region, path=plot_path, evenX = False,
                                       xVar=opt.xVar,names=names,style=style,oldStyle=opt.oldStyle,colours=colours)







