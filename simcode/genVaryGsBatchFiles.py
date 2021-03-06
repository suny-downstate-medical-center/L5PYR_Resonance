# load in packages
import sys
import os

# Handle command line arguments
## load cell
from getCells import HayCell
pt_cell = HayCell()

## create output directories
out_path = '/home/craig_kelley_downstate_edu/L5PYR_Resonance/Hay/Vary_Local_Gs/'

try:
    os.mkdir(out_path)
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

factors = ['m0.25', 'm0.20', 'm0.15', 'm0.10', 'm0.05', '0.0', '0.05', '0.10', '0.15', '0.20', '0.25']

# main code for generating sbatch files and bash file to submit them
## create bash file
sh_file = open(out_path+'gcp_batch_files/chirp-batch.sh','w')
sh_file.write('#!/bin/bash\n')
i = 0
## loop for sbatch files
### loop through ih amd im factors
for ih_factor in factors:
    for im_factor in factors:
        #### basal sections
        # for i, sec in enumerate(pt_cell.basal):
        sec = pt_cell.apic[65]
        file_name = str(sec) + '_ih_' + ih_factor + '_im_' + im_factor + '-batch.sbatch'
        file = open(out_path+'gcp_batch_files/'+file_name,'w')
        
        file.write('#!/bin/bash\n')
        job_name = '#SBATCH --job-name=' + str(sec)+ '_ih_' + ih_factor + '_im_' + im_factor + '\n'
        file.write(job_name)
        file.write('#SBATCH -A default\n')
        file.write('#SBATCH -t 12:00:00\n')
        file.write('#SBATCH --nodes=1\n')
        file.write('#SBATCH --ntasks-per-node=1\n')
        log_line = '#SBATCH -o ' + out_path + 'logs/' + str(sec) + '_ih_' + ih_factor + '_im_' + im_factor +  '.log\n'
        file.write(log_line)
        err_line = '#SBATCH -e ' + out_path + 'errs/' + str(sec) + '_ih_' + ih_factor + '_im_' + im_factor +  '.err\n'
        file.write(err_line)
        # if i == 0:
        #     file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        #     file.write('#SBATCH --mail-type=end\n')
        file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
        file.write('cd /home/craig_kelley_downstate_edu/L5PYR_Resonance/\n')
        run_line = 'ipython varyLocalGsGCP.py ' + ih_factor + ' ' + im_factor + ' ' + str(sec) + '\n'
        file.write(run_line)
        file.close()
        
        ##### write to bash file calling sbash
        sh_line = 'sbatch ' + file_name + '\n'
        sh_file.write(sh_line)
        #### apical sections
        # for i, sec in enumerate(pt_cell.apical):
        #     file_name = str(sec) + '_ih_' + ih_factor + '_im_' + im_factor + '-batch.sbatch'
        #     file = open(out_path+'gcp_batch_files/'+file_name,'w')
            
        #     file.write('#!/bin/bash\n')
        #     job_name = '#SBATCH --job-name=' + str(sec)+ '\n'
        #     file.write(job_name)
        #     file.write('#SBATCH -A default\n')
        #     file.write('#SBATCH -t 12:00:00\n')
        #     file.write('#SBATCH --nodes=1\n')
        #     file.write('#SBATCH --ntasks-per-node=1\n')
        #     log_line = '#SBATCH -o ' + out_path + 'logs/' + str(sec) + '_ih_' + ih_factor + '_im_' + im_factor + '.log\n'
        #     file.write(log_line)
        #     err_line = '#SBATCH -e ' + out_path + 'errs/' + str(sec) + '_ih_' + ih_factor + '_im_' + im_factor + '.err\n'
        #     file.write(err_line)
        #     if i == 0:
        #         file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        #         file.write('#SBATCH --mail-type=end\n')
        #     file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
        #     file.write('cd /home/craig_kelley_downstate_edu/L5PYR_Resonance/\n')
        #     run_line = 'ipython varyLocalGs_hay.py ' + ih_factor + ' ' + im_factor + ' ' + str(sec) + '\n'
        #     file.write(run_line)
        #     file.close()
        
        #     ##### write to bash file calling sbash
        #     sh_line = 'sbatch ' + file_name + '\n'
        #     sh_file.write(sh_line)

sh_file.close()