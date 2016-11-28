import re
import os
import subprocess
import stat
from os import popen

def RepresentsInt(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

def make_bsub_array(scripts = None, queue = '1nh', label='myJob'):

    cwd = os.getcwd()+'/'
    commands = []

    for i,script in enumerate(scripts):

        #chmod
        os.chmod(cwd+script,0744)

        #Build command
        command = ''
        command += 'bsub'
        command += ' -R "pool>10000" -q '+ queue
        command += ' -M 10000 '
        command += ' -J '+label+ str(i)
        command += ' < ' + cwd + '/' + script

        #Submit command
        commands.append(command)

    return commands

def id_from_submission_output(output=None):

    words = [re.findall(r'<([^]]*)>',part) for part in output.split()]
    job_id = ''
    for word in words:
        if len(word)==0: continue
        if RepresentsInt(word[0]):
            job_id = word[0]
    return job_id

def submit_jobs(commands = None,dryRun=False):

    job_ids = []
    for command in commands:

        if dryRun:
            print '[DRY RUN] '+command

        else:
            output = popen(command).read()

            job_id = id_from_submission_output(output=output)

            if job_id == '':
                raise Exception, "Job was not submitted properly:\n"+output
            else:
                job_ids.append(job_id)
                print "Job submitted successfully. Job ID is ",job_id
    if dryRun:
        return {}
    else:
        return dict(zip(job_ids,commands))

def write_job_catalogue(baseDir=None, job_dict=None, file_name=None):

    content = ''
    for job_id,value in job_dict.iteritems():
        content += job_id + ':'
        content += value + '\n'

    catalogue = open(baseDir+file_name,'w')
    catalogue.write(content)
    catalogue.close()

def read_job_catalogue(baseDir=None, file_name=None):

    catalogue = open(baseDir+file_name,'r')
    content = catalogue.read().split('\n')

    job_ids = []
    values = []
    for line in content:
        if line == '': continue
        parts = line.split(':')
        job_ids.append(parts[0])
        values.append(parts[1])

    return dict(zip(job_ids,values))

def update_job_catalogue(baseDir=None,file_name=None,replacement_ids_dict=None):

    with open(baseDir+file_name,'r') as catalogue:
        content = catalogue.read().split('\n')

    replacement_keys = replacement_ids_dict.keys()
    updated_content = ''
    for line in content:
        if line == '': continue
        parts = line.split(':')

        if parts[0] in replacement_keys:
            updated_content += replacement_ids_dict[parts[0]]+':'
        else:
            updated_content += parts[0]+':'
        updated_content += parts[1]+'\n'

    with open(baseDir+file_name,'w') as catalogue:
        catalogue.write(updated_content)

def check_jobs(command_dict=None,product_dict=None):

    old_ids = []
    new_ids = []

    for job_id in command_dict.keys():

        output = popen('bjobs '+job_id).read()
        
        run_or_pend = any(substring in output for substring in ['RUN','PEND'])

        products = product_dict[job_id].split(',')
        missing = 0
        progress = ''
        for i,product in enumerate(products):
            if os.path.isfile(product):
                progress += '-'
            else:
                missing += 1 
                progress += ' '

        if 'RUN' in output:
            #Job is running
            print 'Job '+job_id+' is RUN      |'+progress+'|'

        elif 'PEND' in output:
            #Job is pending
            print 'Job '+job_id+' is PEND     |'+progress+'|'

        elif 'EXIT' in output:
            #Job has failed
            print 'Job '+job_id+' is EXIT     |'+progress+'|',
            #Resubmit?
            if missing > 0:
                #Inform and resubmit
                print '<-- This one failed. Missing '+str(missing)+' products'
                output = popen(command_dict[job_id]).read()
                new_job_id = id_from_submission_output(output=output)
                new_ids.append(new_job_id)
                old_ids.append(job_id)
            else:
                print ' All expected products are present. Not bothering to resubmit'

        elif 'DONE' in output:
            #job is done
            print 'Job '+job_id+' is DONE     |'+progress+'|',
            if missing > 0:
                #Inform and resubmit
                print '<-- This one failed. Missing '+str(missing)+' products'
                output = popen(command_dict[job_id]).read()
                new_job_id = id_from_submission_output(output=output)
                new_ids.append(new_job_id)
                old_ids.append(job_id)
            else:
                print
        else:
            print 'Job '+job_id+' not found   |'+progress+'|',
            if missing > 0:
                #Inform and resubmit
                print '<-- This one failed. Missing '+str(missing)+' products'
                output = popen(command_dict[job_id]).read()
                new_job_id = id_from_submission_output(output=output)
                new_ids.append(new_job_id)
                old_ids.append(job_id)
            else:
                print ' All expected products are present'

    return dict(zip(old_ids,new_ids))
            
def check_all_complete(command_dict=None,product_dict=None):

    done_count = 0
    job_ids = command_dict.keys()
    for job_id in job_ids:

        output = popen('bjobs '+job_id).read()

        products = product_dict[job_id].split(',')
        missing = 0

        for i,product in enumerate(products):
            if not os.path.isfile(product):
                missing += 1 

        if missing == 0:
            done_count += 1

    print "There are "+str(done_count)+" jobs complete out of "+str(len(job_ids))

    if len(job_ids) == done_count:
        return True
    else:
        return False













