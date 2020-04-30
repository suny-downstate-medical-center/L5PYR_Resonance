# Load in the goods
from mpi4py import MPI
import numpy as np
import sys
from scipy.io import savemat
from math import nan

def varyLocalGs(pt_cell, stim_sec, ih_factor, im_factor):

    # parse cmd line inputs, load PT cell template
    ## load cell
    

    ## specify stimulated section and soma segment
    # section = sys.argv[-1]
    # if section.split('.')[1][:4] == 'apic':
    #     stim_sec = pt_cell.apic[int(section.split('.')[1].split('[')[1].split(']')[0])]
    # else:
    #     stim_sec = pt_cell.dend[int(section.split('.')[1].split('[')[1].split(']')[0])]
    soma_seg = pt_cell.soma[0](0.5)

    ## specify factors to change gbar ih/im by, ih comes first
    # if sys.argv[-3][0] == 'm':
    #     ih_factor = float(sys.argv[-3][1:]) * -1.0
    # else:
    #     ih_factor = float(sys.argv[-3])
    # if sys.argv[-2][0] == 'm':
    #     im_factor = float(sys.argv[-2][1:])  * -1.0
    # else:
    #     im_factor = float(sys.argv[-2])

    # changes to Im/Ih
    ## determine original values
    orig_km = []
    orig_ih = []
    for seg in stim_sec.allseg():
        try:
            orig_km.append(seg.Im.gImbar_Im)
        except:
            orig_km.append(0)
        try:
            orig_ih.append(seg.Ih.gIhbar_Ih)
        except:
            orig_ih.append(0)
    ## change Ih/Im
    count = 0
    for seg in stim_sec.allseg():
        try:
            seg.Im.gImbar_Im = orig_km[count] + im_factor * orig_km[count]
        except:
            pass
        try:
            seg.ih.gIhbar_Ih = orig_ih[count] + ih_factor * orig_ih[count]
        except:
            pass
        count = count + 1

    # define current stimulus
    from chirpUtils import applyChirp
    from chirpUtils import getChirp
    amp = 0.0025
    f0, f1, t0, Fs, delay = 0.5, 50, 50, 1000, 12
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

    # main loop
    nseg = stim_sec.nseg
    # if nseg == 1:
    loc = 0.5
    out = applyChirp(I, t, stim_sec(loc), soma_seg, t0, delay, Fs, f1)
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
        # print(str(stim_sec) + ' ' + str(loc))
    # else:
    #     for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
    #         out = applyChirp(I, t, stim_sec(loc), soma_seg, t0, delay, Fs, f1)
    #         ZinResAmp.append(out['ZinResAmp'])
    #         ZinResFreq.append(out['ZinResFreq'])
    #         ZcResAmp.append(out['ZcResAmp'])
    #         ZcResFreq.append(out['ZcResFreq'])
    #         dist.append(out['dist'])
    #         QfactorIn.append(out['QfactorIn'])
    #         QfactorTrans.append(out['QfactorTrans'])
    #         fVarIn.append(out['fVarIn'])
    #         fVarTrans.append(out['fVarTrans'])

    #         freqs = out['Freq'][np.argwhere(out['ZinPhase'] > 0)]
    #         if len(freqs) > 0:
    #             ZinPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZinPhase'] == np.max(out['ZinPhase']))])
    #             ZinLeadPhaseBW.append(freqs[-1] - freqs[0])
    #             ZinLeadPhaseMinFreq.append(freqs[0])
    #             ZinSynchFreq.append(freqs[-1])
    #             ZinLeadPhaseBool.append(out['ZinPhase'] > 0)
    #         else:
    #             ZinPeakPhaseFreq.append(nan)
    #             ZinLeadPhaseBW.append(0)
    #             ZinLeadPhaseMinFreq.append(nan)
    #             ZinSynchFreq.append(nan)
    #             ZinLeadPhaseBool.append(out['ZinPhase'] > 0)

    #         freqs = out['Freq'][np.argwhere(out['ZcPhase'] > 0)]
    #         if len(freqs) > 0:
    #             ZcPeakPhaseFreq.append(out['Freq'][np.argwhere(out['ZcPhase'] == np.max(out['ZcPhase']))])
    #             ZcLeadPhaseBW.append(freqs[-1] - freqs[0])
    #             ZcLeadPhaseMinFreq.append(freqs[0])
    #             ZcSynchFreq.append(freqs[-1])
    #             ZcLeadPhaseBool.append(out['ZcPhase'])
    #         else:
    #             ZcPeakPhaseFreq.append(nan)
    #             ZcLeadPhaseBW.append(0)
    #             ZcLeadPhaseMinFreq.append(nan)
    #             ZcSynchFreq.append(nan)
    #             ZcLeadPhaseBool.append(out['ZcPhase'])

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

    savemat('/u/craig/L5PYR_Resonance/Hay/Vary_Local_Gs/ih_' + sys.argv[-3] + '_im_' + sys.argv[-2] + '/' + stim_sec.name() + '.mat', output)

def doNothing():
    x = 2 + 2

from getCells import HayCell
pt_cell = HayCell()
sec = pt_cell.apic[65]

from neuron import h#, gui
#h.load_file('stdrun.hoc')
pc = h.ParallelContext()
pc.runworker()

factors = [-0.25, -0.2, -0.15, -0.10, -0.05, 0.0, 0.05, 0.1, 0.15, 0.2, 0.25]

for ih_factor in factors:
    for im_factor in factors:
        pc.submit(varyLocalGs, pt_cell, sec, ih_factor, im_factor)
        # pc.submit(doNothing)
        print('yup')
        # varyLocalGs(pt_cell, sec, ih_factor, im_factor)

pc.done()
