import ROOT

def createPileupHists(configPath='data/validation/',configFile = ''):

    with open(configPath+configFile) as f:
        for line in f.read().split('\n'):
            ntuple = line.split()[2]
            tag = line.split()[0]

            #Do what macro/pu.C does
                #open the tree
                #draw the hist
                #extract the hist
                #save as tmp/pu_temp.root








