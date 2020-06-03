import numpy as np
import sys
import multiprocessing
from math import nan
from scipy.io import savemat 

def chirpForMulti(invar):
    sec_num, loc, filename = invar
    from getCells import AllenCell
    pt_cell = AllenCell('./497232419')
    seg = pt_cell.apical[sec_num](loc)
    from neuron import h
    for sec in h.allsec():
        try: sec.uninsert('SK')
        except: pass
    from chirpUtils import applyChirp, getChirp
    amp = 0.0025
    f0, f1, t0, Fs, delay = 0.5, 20, 20, 1000, 5
    I, t = getChirp(f0, f1, t0, amp, Fs, delay)
    print('running chirp on ' + str(seg))
    # applyChirp(I, t, seg, pt_cell.soma[0](0.5), t0, delay, Fs, f1, out_file_name=filename)
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
        ZinPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZinPhase'] == np.max(out['ZinPhase']))])
        ZinLeadPhaseBW.append(freqs[-1] - freqs[0])
        ZinLeadPhaseMinFreq.append(freqs[0])
        ZinSynchFreq.append(freqs[-1])
        ZinLeadPhaseBool.append(out['ZinPhase'] > 0)
    else:
        ZinPeakPhaseFreq.append(nan)
        ZinLeadPhaseBW.append(0)
        ZinLeadPhaseMinFreq.append(nan)
        ZinSynchFreq.append(nan)
        ZinLeadPhaseBool.append(out['ZinPhase'] > 0)

    freqs = out['Freq'][np.argwhere(out['ZcPhase'] > 0)]
    if len(freqs) > 0:
        ZcPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZcPhase'] == np.max(out['ZcPhase']))])
        ZcLeadPhaseBW.append(freqs[-1] - freqs[0])
        ZcLeadPhaseMinFreq.append(freqs[0])
        ZcSynchFreq.append(freqs[-1])
        ZcLeadPhaseBool.append(out['ZcPhase'])
    else:
        ZcPeakPhaseFreq.append(nan)
        ZcLeadPhaseBW.append(0)
        ZcLeadPhaseMinFreq.append(nan)
        ZcSynchFreq.append(nan)
        ZcLeadPhaseBool.append(out['ZcPhase'])
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
            'ZinPeakPhaseFreq' : ZinPeakPhaseFreq, 
            'ZinLeadPhaseBW' : ZinLeadPhaseBW,
            'ZinLeadPhaseMinFreq' : ZinLeadPhaseMinFreq,
            'ZinSynchFreq' : ZinSynchFreq,
            'ZinLeadPhaseBool' : ZinLeadPhaseBool,
            'ZcPeakPhaseFreq' : ZcPeakPhaseFreq,
            'ZcLeadPhaseBW' : ZcLeadPhaseBW,
            'ZcLeadPhaseMinFreq' : ZcLeadPhaseMinFreq,
            'ZcSynchFreq' : ZcSynchFreq,
            'ZcLeadPhaseBool' : ZcLeadPhaseBool}

    savemat(filename + '.mat',output)

# data = [[0, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Allen/apic0'],
#         [2, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Allen/apic2'],
#         [4, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Allen/apic4'],
#         [6, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Allen/apic6'],
#         [8, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Allen/apic8'],
#         [10, 0.5,'/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Allen/apic10']]

data = []
from getCells import AllenCell
pt_cell = AllenCell('./497232419')
for ind, sec in enumerate(pt_cell.apical):
    nseg = sec.nseg
    if nseg == 1:
        data.append([ind, 0.5, '/u/craig/L5PYR_Resonance/497232419/noSK/apic'+str(ind)+'_0.5'])
    else:
        for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
            data.append([ind, loc, '/u/craig/L5PYR_Resonance/497232419/noSK/apic'+str(ind)+'_'+str(loc)])

data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(6)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()