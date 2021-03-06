# Load in the goods
import numpy as np
import sys
from scipy.io import savemat
from math import nan

# parse cmd line inputs, load PT cell template
## load cell
if sys.argv[-2] == 'Hay':
    from getCells import HayCell
    pt_cell = HayCell()
elif sys.argv[-2] == 'Neymotin':
    from getCells import NeymotinCell
    pt_cell = NeymotinCell(slope=100)
elif sys.argv[-2] == 'AckerAntic':
    from getCells import AckerAnticCell
    pt_cell = AckerAnticCell()
elif sys.argv[-2] == 'Kole':
    from getCells import KoleCell
    pt_cell = KoleCell()
else:
    from getCells import AllenCell
    # try:
    pt_cell = AllenCell(sys.argv[-2])
    # except:
    #     print('Error: invalid cell type')

## specify stimulated section and soma segment
section = sys.argv[-1]
if sys.argv[-2] == 'Neymotin' or sys.argv[-2] == 'Hay' or sys.argv[-2] == 'Kole':
    if section.split('.')[1][:4] == 'apic':
        sec = pt_cell.apic[int(section.split('.')[1].split('[')[1].split(']')[0])]
    else:
        sec = pt_cell.dend[int(section.split('.')[1].split('[')[1].split(']')[0])]
else:
    if section.split('[')[0][:4] == 'apic':
        sec = pt_cell.apical[int(section.split('[')[1].split(']')[0])]
    else:
        sec = pt_cell.basal[int(section.split('[')[1].split(']')[0])]

if sys.argv[-2] == 'Neymotin' or sys.argv[-2] == 'Kole':
    soma_seg = pt_cell.soma(0.5)
else:
    soma_seg = pt_cell.soma[0](0.5)

# define current stimulus
from chirpUtils import applyChirp
from chirpUtils import getChirp
amp = 0.0025
## f0, f1, t0, Fs, delay = 0.5, 50, 50, 1000, 12 # original for all cells
f0, f1, t0, Fs, delay = 0.5, 100, 100, 1000, 5 # for looking at bimodal leading phase response in Hay cell
I, t = getChirp(f0, f1, t0, amp, Fs, delay)

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
nseg = sec.nseg
if nseg == 1:
    loc = 0.5
    out = applyChirp(I, t, sec(loc), soma_seg, t0, delay, Fs, f1)
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
    print(str(sec) + ' ' + str(loc))
else:
    for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
        out = applyChirp(I, t, sec(loc), soma_seg, t0, delay, Fs, f1)
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

savemat('/home/craig_kelley_downstate_edu/L5PYR_Resonance/' + sys.argv[-2] + '/impedance_measures/' + sec.name() + '.mat',output)