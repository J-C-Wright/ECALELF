import ROOT
import RegionsFinder as rf

final_v3_config = 'Cal_Sep2016_final_v3.dat'

final_v3_files = rf.getFilesFromConfig(configFile=final_v3_config,tag='d')
mc_file = rf.getFilesFromConfig(configFile=final_v3_config,tag='s')[0]

variable = 'invMass_SC_must_regrCorr_ele'

loose25nsCut = '((energySCEle_must_regrCorr_ele[0]/cosh(etaSCEle[0]) >= 25)&&(energySCEle_must_regrCorr_ele[1]/cosh(etaSCEle[1]) >= 25))'
regionCuts = rf.regionCuts

regions = ['EB']


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

    print "Making final_v3 histo"
    final_v3_hist = ROOT.TH1F('Cal_Sep2016_final_v3','Cal_Sep2016_final_v3',bins,xmin,xmax)
    final_v3_tfiles = []
    for f in final_v3_files:
        tfile = ROOT.TFile.Open(f)
        final_v3_tfiles.append(tfile)

    final_v3_trees = []
    for tfile in final_v3_tfiles:
        tree = tfile.Get('selected')
        final_v3_trees.append(tree)

    for tree in final_v3_trees:
        tree.Draw(variable+'>>var('+str(bins)+','+str(xmin)+','+str(xmax)+')',cut)
        hist = ROOT.gROOT.FindObject('var')
        hist.SetDirectory(0)
        final_v3_hist.Add(hist)

    final_v3_hist.Scale(1/final_v3_hist.Integral())
    final_v3_hist.SetDirectory(0)

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
    final_v3_hist.SetLineColor(ROOT.kBlack)
    final_v3_hist.Draw('same')

    c1.Print('Final'+region+'.pdf')
    c1.Print('Final'+region+'.png')
    













