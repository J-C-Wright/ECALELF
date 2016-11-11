import ROOT
from os import popen
import shutil

def make_pu_histograms(config):

    data_filepaths = []
    mc_filepaths = []

    config_content = ''

    f = open(config)
    config_content = f.read()
    f.close()

    for line in config_content.split('\n'):

        if line == '' or line[0] == '#':
            continue

        line_split = line.split()
        tag = line_split[0]
        name = line_split[1]
        ntuple = line_split[2]

        if 'd' in tag and name == 'selected':
            data_filepaths.append(ntuple)
        if 's' in tag and name == 'selected':
            mc_filepaths.append(ntuple)

    if len(data_filepaths) == 0:
        raise Exception,'No data ntuple files found'
    if len(mc_filepaths) == 0:
        raise Exception,'No mc ntuple files found'

    data_tfiles = []
    for filepath in data_filepaths:
        data_tfiles.append(ROOT.TFile.Open(filepath))
    mc_tfiles = []
    for filepath in mc_filepaths:
        mc_tfiles.append(ROOT.TFile.Open(filepath))
    
    config_name = config.split('/')[-1].split('.')[0]
    #Data pileup histogram
    data_pu_hist = ROOT.TH1F('pileup','',60,0,60)
    for tfile in data_tfiles:
        tree = tfile.Get('selected')
        tree.Draw('nPV+1>>pu(60,0,60)')
        hist = ROOT.gROOT.FindObject('pu')
        hist.SetDirectory(0)
        data_pu_hist.Add(hist)
    data_pu_hist.SetDirectory(0)
    data_pu_hist.SaveAs('data/puHistos/pu_data_'+config_name+'.root')

    #MC pileup histogram
    mc_pu_hist = ROOT.TH1F('pileup','',60,0,60)
    for tfile in mc_tfiles:
        tree = tfile.Get('selected')
        tree.Draw('nPV+1>>pu(60,0,60)')
        hist = ROOT.gROOT.FindObject('pu')
        hist.SetDirectory(0)
        mc_pu_hist.Add(hist)
    mc_pu_hist.SetDirectory(0)
    mc_pu_hist.SaveAs('data/puHistos/pu_MC_'+config_name+'.root')

    output_config = ''
    for line in config_content.split('\n'):
        if 'pileup' not in line and line != '':
            output_config += line + '\n'

    output_config += '\n'
    output_config += 'd pileupHist data/puHistos/pu_data_'+config_name+'.root\n'
    output_config += 's pileupHist data/puHistos/pu_MC_'+config_name+'.root\n'

    config_file = open('data/validation/'+config_name+'.dat','w')
    config_file.write(output_config)
    config_file.close()


def make_pu_trees(config):

    command = ''
    command += './bin/ZFitter.exe'
    command += ' -f '+config
    command += ' --regionsFile=data/regions/scaleStep0.dat --saveRootMacro'
    output = popen(command).read()

    with open(config) as f:
        config_content = f.read()

    config_name = config.split('/')[-1].split('.')[0]

    mc_tags = [] 
    for line in config_content.split('\n'):

        if line == '' or line[0] == '#':
            continue

        line_split = line.split()
        tag = line_split[0]
        name = line_split[1]
        ntuple = line_split[2]

        if 's' in tag and name == 'selected':
            mc_tags.append(tag)

    for tag in mc_tags:
        shutil.move('tmp/mcPUtree'+tag+'.root','data/puTree/'+tag+'_'+config_name+'.root')

    output_config = ''
    for line in config_content.split('\n'):
        if 'puTree' not in line and line != '':
            output_config += line+'\n'

    output_config += '\n'
    output_config += 's1 pileup data/puTree/s1_'+config_name+'.root'

    config_file = open('data/validation/'+config_name+'.dat','w')
    config_file.write(output_config)
    config_file.close()

def run_divide(config,interval):

    interval = int(interval)

    command = ''
    command += './bin/ZFitter.exe'
    command += ' -f '+config
    command += ' --runDivide'
    command += ' --nEvents_runDivide '+str(interval)

    output = popen(command).read()
    run_ranges_content = ''
    for line in output.split('\n'):
        parts = line.split()
        if '[DEBUG]' not in line and len(parts) == 3 and len(parts[0].split('-'))==2:
            run_ranges_content += line + '\n'

    config_name = config.split('/')[-1].split('.')[0]
    run_ranges_file = open('data/runRanges/'+config_name+'_interval_'+str(interval)+'.dat','w')
    run_ranges_file.write(run_ranges_content)
    run_ranges_file.close() 



