# load in packages
import sys
import os

# Handle command line arguments
## load cell
if sys.argv[-1] == 'Hay':
    from getCells import HayCell
    pt_cell = HayCell()
elif sys.argv[-1] == 'Neymotin':
    from getCells import NeymotinCell
    pt_cell = NeymotinCell()
elif sys.argv[-1] == 'AckerAntic':
    from getCells import AckerAnticCell
    pt_cell = AckerAnticCell()
elif sys.argv[-1] == 'Kole':
    from getCells import KoleCell
    pt_cell = KoleCell()
else:
    from getCells import AllenCell
    try:
        pt_cell = AllenCell(sys.argv[-1])
    except:
        print('Error: invalid cell type')

## create output directories
out_path = '/home/craig_kelley_downstate_edu/L5PYR_Resonance/' + sys.argv[-1] + '/'
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

# main code for generating sbatch files and bash file to submit them
## create bash file
sh_file = open(out_path+'gcp_batch_files/chirp-batch.sh','w')
sh_file.write('#!/bin/bash\n')
## loop for sbatch files
### basal sections
for i, sec in enumerate(pt_cell.basal):
    file_name = str(sec)+'-batch.sbatch'
    file = open(out_path+'gcp_batch_files/'+file_name,'w')
    
    file.write('#!/bin/bash\n')
    job_name = '#SBATCH --job-name=' + str(sec)+ '\n'
    file.write(job_name)
    file.write('#SBATCH -A default\n')
    file.write('#SBATCH -t 24:00:00\n')
    file.write('#SBATCH --nodes=1\n')
    file.write('#SBATCH --ntasks-per-node=1\n')
    log_line = '#SBATCH -o ' + out_path + 'logs/' + str(sec) + '.log\n'
    file.write(log_line)
    err_line = '#SBATCH -e ' + out_path + 'errs/' + str(sec) + '.err\n'
    file.write(err_line)
    if i == 0:
        file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        file.write('#SBATCH --mail-type=end\n')
    file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
    file.write('cd /home/craig_kelley_downstate_edu/L5PYR_Resonance/\n')
    run_line = 'ipython chirpForGCP.py ' + sys.argv[-1] + ' ' + str(sec) + '\n'
    file.write(run_line)
    file.close()
    
    #### write to bash file calling sbash
    sh_line = 'sbatch ' + file_name + '\n'
    sh_file.write(sh_line)
### apical sections
for i, sec in enumerate(pt_cell.apical):
    file_name = str(sec)+'-batch.sbatch'
    file = open(out_path+'gcp_batch_files/'+file_name,'w')
    
    file.write('#!/bin/bash\n')
    job_name = '#SBATCH --job-name=' + str(sec)+ '\n'
    file.write(job_name)
    file.write('#SBATCH -A default\n')
    file.write('#SBATCH -t 24:00:00\n')
    file.write('#SBATCH --nodes=1\n')
    file.write('#SBATCH --ntasks-per-node=1\n')
    log_line = '#SBATCH -o ' + out_path + 'logs/' + str(sec) + '.log\n'
    file.write(log_line)
    err_line = '#SBATCH -e ' + out_path + 'errs/' + str(sec) + '.err\n'
    file.write(err_line)
    if i == 0:
        file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        file.write('#SBATCH --mail-type=end\n')
    file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
    file.write('cd /home/craig_kelley_downstate_edu/L5PYR_Resonance/\n')
    run_line = 'ipython chirpForGCP.py ' + sys.argv[-1] + ' ' + str(sec) + '\n'
    file.write(run_line)
    file.close()
    
    #### write to bash file calling sbash
    sh_line = 'sbatch ' + file_name + '\n'
    sh_file.write(sh_line)

sh_file.close()