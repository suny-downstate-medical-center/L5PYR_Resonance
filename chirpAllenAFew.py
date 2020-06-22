import sys
import os
if  sys.argv[-1] == 'pt':
    os.environ["OPENBLAS_NUM_THREADS"] = "6"
elif sys.argv[-1] == 'zn':
    os.environ["OPENBLAS_NUM_THREADS"] = "32"
elif sys.argv[-1] == 'my':
    os.environ["OPENBLAS_NUM_THREADS"] = "16"
elif sys.argv[-1] == 'el':
    os.environ["OPENBLAS_NUM_THREADS"] = "12"
elif sys.argv[-1] == 'au':
    os.environ["OPENBLAS_NUM_THREADS"] = "16"

from os import listdir, mkdir
import numpy as np
import multiprocessing
from math import nan
from scipy.io import savemat 

def chirpForMulti(invar):
    sec_num, loc, morph_file, filename = invar
    from getCells import HayCellSWC
    pt_cell = HayCellSWC(morphology_file=morph_file)
    seg = pt_cell.apic[sec_num](loc)
    from chirpUtils import applyChirp, getChirp
    amp = 0.0025
    f0, f1, t0, Fs, delay = 0.5, 20, 20, 1000, 5 # for looking at bimodal leading phase response in Hay cell
    I, t = getChirp(f0, f1, t0, amp, Fs, delay)
    print('running chirp on ' + str(seg))
    out = applyChirp(I, t, seg, pt_cell.soma[0](0.5), t0, delay, Fs, f1)
    ZinResAmp = []
    ZinResFreq = []
    ZcResAmp = []
    ZcResFreq = []
    dist = []
    QfactorIn = []
    QfactorTrans = []
    fVarIn = []
    fVarTrans = []
    ZinPeakPhaseFreq = []
    ZinLeadPhaseBW = []
    ZinLeadPhaseMinFreq = []
    ZinSynchFreq = []
    ZinLeadPhaseBool = []
    ZcPeakPhaseFreq = []
    ZcLeadPhaseBW = []
    ZcLeadPhaseMinFreq = []
    ZcSynchFreq = []
    ZcLeadPhaseBool = []
    ZinResAmp.append(out['ZinResAmp'])
    ZinResFreq.append(out['ZinResFreq'])
    ZcResAmp.append(out['ZcResAmp'])
    ZcResFreq.append(out['ZcResFreq'])
    dist.append(out['dist'])
    QfactorIn.append(out['QfactorIn'])
    QfactorTrans.append(out['QfactorTrans'])
    fVarIn.append(out['fVarIn'])
    fVarTrans.append(out['fVarTrans'])

    freqs = out['Freq'][np.argwhere(out['ZinPhase'] > 0)]
    if len(freqs) > 0:
        ZinSynchFreq.append(freqs[-1])
    else:
        ZinSynchFreq.append(nan)

    freqs = out['Freq'][np.argwhere(out['ZcPhase'] > 0)]
    if len(freqs) > 0:
        freqs = freqs[freqs<10]
        ZcSynchFreq.append(freqs[-1])
    else:
        ZcSynchFreq.append(nan)
    print(str(sec) + ' ' + str(loc) + ': done')

    output = { 'ZinResAmp' : ZinResAmp,
            'ZinResFreq' : ZinResFreq,
            'ZcResAmp' : ZcResAmp,
            'ZcResFreq' : ZcResFreq,
            'dist' : dist,
            'QfactorIn' : QfactorIn,
            'QfactorTrans' : QfactorTrans,
            'fVarIn' : fVarIn,
            'fVarTrans' : fVarTrans,
            'ZinSynchFreq' : ZinSynchFreq,
            'ZcSynchFreq' : ZcSynchFreq}

    savemat(filename + '.mat',output)

# moprh_path = '/u/craig/L5PYR_Resonance/suter_shepherd/'
moprh_path = '/u/craig/L5PYR_Resonance/allen_morphs/'
morph_files = listdir(moprh_path)

if sys.argv[-1] == 'pt':
    N = 6
    # data = data[:34]
    morph_files = ['BS0416.CNG.swc']
elif sys.argv[-1] == 'zn':
    N = 16#32
    # morph_files = ['BS0284.CNG.swc', 'BS0430.CNG.swc', 'BS0483.CNG.swc', 'BS0613.CNG.swc']
    # morph_files = ['Rorb-IRES2-Cre-D_Ai14-197353.06.02.01_496079587_m.swc']
    morph_files = ['Rbp4-Cre_KL100_Ai14-203498.04.02.01_496001061_m.swc', 'Rbp4-Cre_KL100_Ai14-203503.04.01.01_527109145_m.swc', 'Scnn1a-Tg2-Cre_Ai14-176962.05.01.01_495335447_m.swc', 'Scnn1a-Tg3-Cre_Ai14-168093.03.02.01_491119592_m.swc', 'Scnn1a-Tg3-Cre_Ai14-177297.05.02.01_495335458_m.swc']
    # data = data[35:225]
elif sys.argv[-1] == 'my':
    N = 12
    morph_files = ['BS0475.CNG.swc', 'BS0477.CNG.swc']
    # data = data[226:319]
elif sys.argv[-1] == 'el':
    N = 12
    morph_files = ['BS0412.CNG.swc', 'BS0413.CNG.swc']
    # data = data[320:389]
elif sys.argv[-1] == 'au':
    N = 16
    morph_files = ['BS0478.CNG.swc', 'BS0480.CNG.swc', 'BS0582.CNG.swc']
    # data = data[390:]

data = []
for morph_file in morph_files:
    # cellID = morph_file.split('.')[0]
    cellID = morph_file.split('_')[-2]
    try:
        mkdir('/u/craig/L5PYR_Resonance/AllenChirpData/'+cellID)
    except:
        pass
    from getCells import HayCellSWC
    pt_cell = HayCellSWC(morphology_file=moprh_path+morph_file)
    for ind, sec in enumerate(pt_cell.apic):
        nseg = sec.nseg
        if nseg == 1:
            data.append([ind, 0.5, moprh_path+morph_file, '/u/craig/L5PYR_Resonance/AllenChirpData/'+cellID+ '/apic'+str(ind)+'_0.5'])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([ind, loc, moprh_path+morph_file, '/u/craig/L5PYR_Resonance/AllenChirpData/'+cellID+'/apic'+str(ind)+'_'+str(loc)])


data = tuple(data)



def mp_handler():
    p = multiprocessing.Pool(N)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()
