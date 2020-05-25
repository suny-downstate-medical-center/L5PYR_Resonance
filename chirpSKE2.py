import numpy as np
import sys
import multiprocessing

def chirpForMulti(invar):
    sec_num, loc, filename = invar
    from getCells import HayCell
    pt_cell = HayCell()
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

data = [[0, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2/apic0_0.5'],
        [2, 0.25, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2/apic2_2.5'],
        [14, 0.5, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2/apic14_0.5'],
        [36, 0.14, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2/apic36_0.14'],
        [36, 0.8, '/u/craig/L5PYR_Resonance/timeDomainOutput/chirpSKE2/apic36_0.8']]

data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(5)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()