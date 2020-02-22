from neuron import h, init
h.load_file("/usr/local/nrn//share/nrn/lib/hoc/stdrun.hoc")
# load PT cell template
h.load_file("./cells/PTcell.hoc")
ihMod2str = {'harnett': 1, 'kole': 2, 'migliore': 3}
pt_cell = h.PTcell(ihMod2str['migliore'], 14*2)

out_path = '/home/craig_kelley_downstate_edu/M1_Res/gcp_batch_files/'
sh_file = open(out_path+'m1-batch.sh','w')
sh_file.write('#!/bin/bash\n')

for i, sec in enumerate(pt_cell.basal):
    file_name = str(sec)+'-batch.sbatch'
    file = open(out_path+file_name,'w')
    
    file.write('#!/bin/bash\n')
    job_name = '#SBATCH --job-name=' + str(sec)+ '\n'
    file.write(job_name)
    file.write('#SBATCH -A default\n')
    file.write('#SBATCH -t 12:00:00\n')
    file.write('#SBATCH --nodes=1\n')
    file.write('#SBATCH --ntasks-per-node=1\n')
    log_line = '#SBATCH -o /home/craig_kelley_downstate_edu/M1_Res/logs/'+str(sec)+'.log\n'
    file.write(log_line)
    err_line = '#SBATCH -e /home/craig_kelley_downstate_edu/M1_Res/errs/'+str(sec)+'.err\n'
    file.write(err_line)
    if i == 68:
        file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        file.write('#SBATCH --mail-type=end\n')
    file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
    file.write('cd /home/craig_kelley_downstate_edu/M1_Res/\n')
    run_line = 'mpirun -np 1 nrniv -python -mpi chirpForGCP.py ' + str(sec) + '\n'
    file.write(run_line)
    file.close()
    
    #write to bash file calling sbash
    sh_line = 'sbatch ' + file_name + '\n'
    sh_file.write(sh_line)

for i, sec in enumerate(pt_cell.apical):
    file_name = str(sec)+'-batch.sbatch'
    file = open(out_path+file_name,'w')
    
    file.write('#!/bin/bash\n')
    job_name = '#SBATCH --job-name=' + str(sec)+ '\n'
    file.write(job_name)
    file.write('#SBATCH -A default\n')
    file.write('#SBATCH -t 12:00:00\n')
    file.write('#SBATCH --nodes=1\n')
    file.write('#SBATCH --ntasks-per-node=1\n')
    log_line = '#SBATCH -o /home/craig_kelley_downstate_edu/M1_Res/logs/'+str(sec)+'.log\n'
    file.write(log_line)
    err_line = '#SBATCH -e /home/craig_kelley_downstate_edu/M1_Res/errs/'+str(sec)+'.err\n'
    file.write(err_line)
    if i == 102:
        file.write('#SBATCH --mail-user=craig.kelley@downstate.edu\n')
        file.write('#SBATCH --mail-type=end\n')
    file.write('source /home/craig_kelley_downstate_edu/.bashrc\n')
    file.write('cd /home/craig_kelley_downstate_edu/M1_Res/\n')
    run_line = 'mpirun -np 1 nrniv -python -mpi chirpForGCP.py ' + str(sec) + '\n'
    file.write(run_line)
    file.close()
    
    #write to bash file calling sbash
    sh_line = 'sbatch ' + file_name + '\n'
    sh_file.write(sh_line)