# load in packages
import sys
import os

# Handle command line arguments
## load cell

from getCells import HayCell
morph_file = './morphologies/cell3.asc'
pt_cell = HayCell(morphology_file=morph_file)

## create output directories
out_path = '/home/craig_kelley_downstate_edu/L5PYR_Resonance/Hay/' + morph_file.split('/')[-1].split('.')[0] + '/'
try:
    os.mkdir(out_path)
except:
    pass
try:
    os.mkdir(out_path + 'impedance_measures')
except:
    pass
try:
    os.mkdir(out_path + 'gcp_batch_files')
except:
    pass
try:
    os.mkdir(out_path + 'logs')
except:
    pass
try:
    os.mkdir(out_path + 'errs')
except:
    pass

sec = pt_cell.apic[102]
nseg = sec.nseg
import numpy as np

# main code for generating sbatch files and bash file to submit them
## create bash file
sh_file = open(out_path+'gcp_batch_files/apic102-batch.sh','w')
sh_file.write('#!/bin/bash\n')
## loop for sbatch files
### basal sections
for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
    file_name = str(loc)+'-batch.sbatch'
    file = open(out_path+'gcp_batch_files/'+file_name,'w')
    
    file.write('#!/bin/bash\n')
    job_name = '#SBATCH --job-name=' + str(loc)+ '\n'
    file.write(job_name)
    file.write('#SBATCH -A default\n')
    file.write('#SBATCH -t 12:00:00\n')
    file.write('#SBATCH --nodes=1\n')
    file.write('#SBATCH --ntasks-per-node=1\n')
    log_line = '#SBATCH -o ' + out_path + 'logs/' + str(loc) + '.log\n'
    file.write(log_line)
    err_line = '#SBATCH -e ' + out_path + 'errs/' + str(loc) + '.err\n'
    file.write(err_line)
    if i == 0:
        file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        file.write('#SBATCH --mail-type=end\n')
    file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
    file.write('cd /home/craig_kelley_downstate_edu/L5PYR_Resonance/\n')
    run_line = 'ipython chirpCell3apic102.py ' + str(loc)  + '\n'
    file.write(run_line)
    file.close()
    
    #### write to bash file calling sbash
    sh_line = 'sbatch ' + file_name + '\n'
    sh_file.write(sh_line)
### apical sections
for i, sec in enumerate(pt_cell.apical):
    file_name = str(loc)+'-batch.sbatch'
    file = open(out_path+'gcp_batch_files/'+file_name,'w')
    
    file.write('#!/bin/bash\n')
    job_name = '#SBATCH --job-name=' + str(loc)+ '\n'
    file.write(job_name)
    file.write('#SBATCH -A default\n')
    file.write('#SBATCH -t 12:00:00\n')
    file.write('#SBATCH --nodes=1\n')
    file.write('#SBATCH --ntasks-per-node=1\n')
    log_line = '#SBATCH -o ' + out_path + 'logs/' + str(loc) + '.log\n'
    file.write(log_line)
    err_line = '#SBATCH -e ' + out_path + 'errs/' + str(loc) + '.err\n'
    file.write(err_line)
    if i == 0:
        file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        file.write('#SBATCH --mail-type=end\n')
    file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
    file.write('cd /home/craig_kelley_downstate_edu/L5PYR_Resonance/\n')
    run_line = 'ipython chirpCell3apic102.py ' + str(loc)  + '\n'
    file.write(run_line)
    file.close()
    
    #### write to bash file calling sbash
    sh_line = 'sbatch ' + file_name + '\n'
    sh_file.write(sh_line)

sh_file.close()