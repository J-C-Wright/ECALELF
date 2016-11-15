import os
import subprocess
import stat
import re
from os import popen

def createValidationScript(configPath='data/validation/',
                           configFile = '',invMass = 'invMass_SC_corr',baseDir='',
                           regionsPath = 'data/regions/',regionsFile = 'validation.dat',selection=''):

    #Write the script
    scriptContent = ''
    scriptContent += 'cd ' + os.getcwd().split('Calibration')[0] + '\n'
    scriptContent += 'eval $(scram runtime -sh)\n'
    scriptContent += 'cd Calibration/ZFitter/\n'
    scriptContent += '\n'

    #monitoring_validation part
    scriptContent += './script/monitoring_validation.sh'
    scriptContent += ' -f '+configPath+configFile
    scriptContent += ' --invMass_var '+invMass
    scriptContent += ' --baseDir '+baseDir
    scriptContent += ' --selection '+selection
    scriptContent += ' --validation'
    scriptContent += '\n'

    #Write to the script file...
    if not os.path.exists('tmp/validations/'):
        os.makedirs('tmp/validations/')

    script_name = configFile.split('.')[0]

    validationFile = open('tmp/validations/'+script_name+'.sh','w')
    validationFile.write(scriptContent)
    validationFile.close()

    return 'tmp/validations/'+script_name+'.sh'

def RepresentsInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

def submitValidationScript(script='',jobName='valRun',queue='cmscaf1nd',dryRun=False):

    #Get current working directory
    cwd = os.getcwd()+'/'

    #chmod
    os.chmod(cwd+script,0744)

    #Build command
    command = ''
    command += 'bsub'
    command += ' -R "pool>100000" -q '+ queue
    command += ' -M 100000 '
    command += ' -J ' + jobName
    command += ' < ' + cwd + '/' + script

    #Submit command
    id_number = '-1'
    if not dryRun:
        output = popen(command).read()
        words = [re.findall(r'<([^]]*)>',part) for part in output.split()]
        for word in words:
            if len(word)==0: continue
            if RepresentsInt(word[0]):
                id_number = word[0]

    #Get the ID number of the jobs and return it
    if id_number == '-1':
        print "Job was not submitted successfully."
    else:
        print "Job submitted successfully. Job ID is ",id_number

    return id_number


def monitorValidationScript(baseDir='',configFile='',script='',jobName='valRun',
                            invMass = '',selection='',commonCut='Et_25',
                            jobID='',queue='cmscaf1nd',dryRun=False):

    #Check job id
    command = 'bjobs '+jobID
    output = popen(command).read()

    #Is it running?
    if 'is not found' in output or 'EXIT' in output or output == '':

        print "Job "+jobID+" is either EXIT or DONE."
        print "Checking whether it failed..."
        print "Is the summary table at "+baseDir+'/dato/'+configFile.split('.')[0]+'/'+selection+'/'+invMass+'/table/ ?',

        #Check whether the summary table is there. If it is it's done
        table_path = baseDir+'/dato/'+configFile.split('.')[0]+'/'+selection+'/'+invMass+'/table/'+'-'.join(['monitoring_summary',invMass,selection,commonCut])+'.tex'
        file_exists = os.path.isfile(table_path)

        if file_exists:
            print ' Yes, job is finished!'
            return '0'
        else:
            print ' No, job needs to be resubmitted. Resubmitting...'
            jobID = submitValidationScript(script=script)
            return jobID

    else:
        print "Job "+jobID+" is in progress"
        return jobID






configFile = 'Cal_Sep2016_final_v3.dat'
baseDir = configFile.split('.')[0]+'-Batch/'
selection = 'loose25nsRun2'
invMass = 'invMass_SC_must_regrCorr_ele'








