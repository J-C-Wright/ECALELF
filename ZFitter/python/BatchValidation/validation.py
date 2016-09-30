import os
import subprocess
import stat
from os import popen

def createValidationScript(configPath='data/validation/',
                           configFile = '',invMass = 'invMass_SC_corr',baseDir='',
                           updateOnly = '--updateOnly', outDirMC = '', outDirData = '',commonCut='Et_25',
                           regionsPath = 'data/regions/',regionsFile = 'validation.dat'):

    #Write the script
    scriptContent = ''
    scriptContent += 'cd ' + os.getcwd().split('Calibration')[0] + '\n'
    scriptContent += 'eval $(scram runtime -sh)\n'
    scriptContent += 'cd Calibration/ZFitter/\n'
    scriptContent += '\n'

    #validation part...
    scriptContent += './script/monitoring_validation.sh'
    scriptContent += ' -f '+configPath+configFile
    scriptContent += ' --runRangesFile '+file
    scriptContent += ' --invMass_var '+invMass
    scriptContent += ' --baseDir '+baseDir
    scriptContent += ' --validation'
    scriptContent += '\n'

    #Write to the script file...
    splitFile = open(scriptName,'w')
    splitFile.write(scriptContent)
    splitFile.close()


