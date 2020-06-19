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

moprh_path = '/u/craig/L5PYR_Resonance/suter_shepherd/'
# morph_files = listdir(moprh_path)
morph_files = ['BS0284.CNG.swc', 'BS0430.CNG.swc', 'BS0483.CNG.swc', 'BS0613.CNG.swc']

data = []
for morph_file in morph_files:
    cellID = morph_file.split('.')[0]
    try:
        mkdir('/u/craig/L5PYR_Resonance/SuterChirpData/'+cellID)
    except:
        pass
    from getCells import HayCellSWC
    pt_cell = HayCellSWC(morphology_file=moprh_path+morph_file)
    for ind, sec in enumerate(pt_cell.apic):
        nseg = sec.nseg
        if nseg == 1:
            data.append([ind, 0.5, moprh_path+morph_file, '/u/craig/L5PYR_Resonance/SuterChirpData/'+cellID+ '/apic'+str(ind)+'_0.5'])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([ind, loc, moprh_path+morph_file, '/u/craig/L5PYR_Resonance/SuterChirpData/'+cellID+'/apic'+str(ind)+'_'+str(loc)])


data = tuple(data)

if sys.argv[-1] == 'pt':
    N = 6
    # data = data[:34]
elif sys.argv[-1] == 'zn':
    N = 32
    # data = data[35:225]
elif sys.argv[-1] == 'my':
    N = 10
    # data = data[226:319]
elif sys.argv[-1] == 'el':
    N = 12
    # data = data[320:389]
elif sys.argv[-1] == 'au':
    N = 16
    # data = data[390:]

def mp_handler():
    p = multiprocessing.Pool(N)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()
