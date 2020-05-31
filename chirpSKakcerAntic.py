import numpy as np
import sys
import multiprocessing

def chirpForMulti(invar):
    sec_num, loc, filename = invar
    from getCells import AckerAnticCell
    pt_cell = AckerAnticCell()
    seg = pt_cell.apic[sec_num](loc)
    from neuron import h
    for sec in h.allsec():
        try: sec.uninsert('SK_E2')
        except: pass
    from chirpUtils import applyChirp, getChirp
    amp = 0.0025
    f0, f1, t0, Fs, delay = 0.5, 20, 20, 1000, 5 # for looking at bimodal leading phase response in Hay cell
    I, t = getChirp(f0, f1, t0, amp, Fs, delay)
    print('running chirp on ' + str(seg))
    applyChirp(I, t, seg, pt_cell.soma[0](0.5), t0, delay, Fs, f1, out_file_name=filename)

data = [[0, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic0'],
        [2, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic2'],
        [4, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic4'],
        [6, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic6'],
        [7, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic6'],
        [10, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic10'],
        [13, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2Acker/apic13']]

data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(4)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()