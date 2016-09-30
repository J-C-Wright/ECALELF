import ROOT
import RegionsFinder as rf

ref_config = 'Cal_Sep2016_ref.dat'
laser_v3_config = 'Cal_Sep2016_laser_v3.dat'

ref_files = rf.getFilesFromConfig(configFile=ref_config,tag='d')
laser_v3_files = rf.getFilesFromConfig(configFile=laser_v3_config,tag='d')
mc_file = rf.getFilesFromConfig(configFile=ref_config,tag='s')[0]

variable = 'invMass_SC_must_regrCorr_ele'

loose25nsCut = '((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25))'
regionCuts = rf.regionCuts

regions = ['EE-gold']


for region in regions:

    regionParts = [loose25nsCut]
    for part in region.split('-'):
        regionParts.append(regionCuts[part])
        
    cut = '&&'.join(regionParts)

    print region,' ',cut
    print
    
    ROOT.gROOT.SetBatch(ROOT.kTRUE)

    bins = 100
    xmin = 80
    xmax = 100

    print "Making laser_v3 histo"
    laser_v3_hist = ROOT.TH1F('Cal_Sep2016_laser_v3','Cal_Sep2016_laser_v3',bins,xmin,xmax)
    laser_v3_tfiles = []
    for f in laser_v3_files:
        tfile = ROOT.TFile.Open(f)
        laser_v3_tfiles.append(tfile)

    laser_v3_trees = []
    for tfile in laser_v3_tfiles:
        tree = tfile.Get('selected')
        laser_v3_trees.append(tree)

    for tree in laser_v3_trees:
        tree.Draw(variable+'>>var('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)
        hist = ROOT.gROOT.FindObject('var')
        hist.SetDirectory(0)
        laser_v3_hist.Add(hist)

    laser_v3_hist.Scale(1/laser_v3_hist.Integral())
    laser_v3_hist.SetDirectory(0)

    print "Making ref histo"
    ref_hist = ROOT.TH1F('Cal_Sep2016_ref','Cal_Sep2016_ref',bins,xmin,xmax)

    ref_tfiles = []
    for f in ref_files:
        tfile = ROOT.TFile.Open(f)
        ref_tfiles.append(tfile)

    ref_trees = []
    for tfile in ref_tfiles:
        tree = tfile.Get('selected')
        ref_trees.append(tree)

    for tree in ref_trees:
        tree.Draw(variable+'>>var('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)
        hist_ref = ROOT.gROOT.FindObject('var')
        hist_ref.SetDirectory(0)
        ref_hist.Add(hist)

    ref_hist.Scale(1/ref_hist.Integral())
    ref_hist.SetDirectory(0)

    print "Making mc histo"
    tfile = ROOT.TFile.Open(mc_file)
    tree = tfile.Get('selected')
    tree.Draw(variable+'>>var('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)
    mc_hist = ROOT.gROOT.FindObject('var')
    mc_hist.Scale(1/mc_hist.Integral())
    mc_hist.SetDirectory(0)
   
    c1 = ROOT.TCanvas('c1')
    mc_hist.SetLineColor(ROOT.kRed)
    mc_hist.Draw()
    ref_hist.SetLineColor(ROOT.kBlue)
    ref_hist.Draw('same')
    laser_v3_hist.SetLineColor(ROOT.kBlack)
    laser_v3_hist.Draw('same')

    c1.Print(region+'.pdf')
    c1.Print(region+'.png')
    













