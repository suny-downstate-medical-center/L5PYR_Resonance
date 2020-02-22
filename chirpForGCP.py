# Load in the goods
from neuron import h, init
# h.load_file("stdrun.hoc")
import numpy as np
import sys
from scipy.io import savemat

# define current stimulus
from chirpUtils import applyChirp
from chirpUtils import getChirp
amp = 0.0025
f0, f1, t0, Fs, delay = 0.5, 50, 50, 1000, 12
I, t = getChirp(f0, f1, t0, amp, Fs, delay)

# load PT cell template
h.load_file("./cells/PTcell.hoc")
ihMod2str = {'harnett': 1, 'kole': 2, 'migliore': 3}
pt_cell = h.PTcell(ihMod2str['migliore'], 14*2)

# define output variables
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

#main loop
section = sys.argv[-1]
if section.split('.')[1][:4] == 'apic':
    sec = pt_cell.apic[int(section.split('.')[1].split('[')[1].split(']')[0])]
else:
    sec = pt_cell.dend[int(section.split('.')[1].split('[')[1].split(']')[0])]

nseg = sec.nseg
if nseg == 1:
    loc = 0.5
    out = applyChirp(I, t, sec(loc), pt_cell.soma(0.5), t0, delay, Fs, f1)
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
    ZinPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZinPhase'] == np.max(out['ZinPhase']))])
    ZinLeadPhaseBW.append(freqs[-1] - freqs[0])
    ZinLeadPhaseMinFreq.append(freqs[0])
    ZinSynchFreq.append(freqs[-1])
    ZinLeadPhaseBool.append(out['ZinPhase'] > 0)

    freqs = out['Freq'][np.argwhere(out['ZcPhase'] > 0)]
    ZcPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZcPhase'] == np.max(out['ZcPhase']))])
    ZcLeadPhaseBW.append(freqs[-1] - freqs[0])
    ZcLeadPhaseMinFreq.append(freqs[0])
    ZcSynchFreq.append(freqs[-1])
    ZcLeadPhaseBool.append(out['ZcPhase'])
    print(str(sec) + ' ' + str(loc))
else:
    for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
        out = applyChirp(I, t, sec(loc), pt_cell.soma(0.5), t0, delay, Fs, f1)
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
        ZinPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZinPhase'] == np.max(out['ZinPhase']))])
        ZinLeadPhaseBW.append(freqs[-1] - freqs[0])
        ZinLeadPhaseMinFreq.append(freqs[0])
        ZinSynchFreq.append(freqs[-1])
        ZinLeadPhaseBool.append(out['ZinPhase'] > 0)

        freqs = out['Freq'][np.argwhere(out['ZcPhase'] > 0)]
        ZcPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZcPhase'] == np.max(out['ZcPhase']))])
        ZcLeadPhaseBW.append(freqs[-1] - freqs[0])
        ZcLeadPhaseMinFreq.append(freqs[0])
        ZcSynchFreq.append(freqs[-1])
        ZcLeadPhaseBool.append(out['ZcPhase'])
        print(str(sec) + ' ' + str(loc))

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

savemat('/home/craig_kelley_downstate_edu/M1_Res/impedance_measures/'+sec.name()+'.mat',output)