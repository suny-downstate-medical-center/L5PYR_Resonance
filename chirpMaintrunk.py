import sys
import os
os.environ["OPENBLAS_NUM_THREADS"] = sys.argv[-2]
N = int(sys.argv[-2])
from os import listdir, mkdir
import numpy as np
import multiprocessing
from math import nan
from scipy.io import savemat 

def chirpForMulti(invar):
    model, sec_num, loc, filename = invar
    if model == 'kole':
        from getCells import KoleCell
        cell, _ = KoleCell()
        seg = cell.apic[sec_num](loc)
        soma_seg = cell.soma(0.5)
    elif model == 'neymotinkole':
        from getCells import NeymotinKoleCell
        cell = NeymotinKoleCell()
        seg = cell.apic[sec_num](loc)
        soma_seg = cell.soma(0.5)
    elif model == 'neymotinharnett':
        from getCells import NeymotinHarnettCell
        cell = NeymotinHarnettCell()
        seg = cell.apic[sec_num](loc)
        soma_seg = cell.soma(0.5)
    elif model == 'neymotinmigliore':
        from getCells import NeymotinMiglioreCell
        cell = NeymotinMiglioreCell()
        seg = cell.apic[sec_num](loc)
        soma_seg = cell.soma(0.5)
    elif model == 'hay':
        from getCells import HayCell
        cell, _ = HayCell()
        seg = cell.apic[sec_num](loc)
        soma_seg = cell.soma[0](0.5)
    elif model == 'ackerantic':
        from getCells import AckerAnticCell
        cell = AckerAnticCell()
        seg = cell.apical[sec_num](loc)
        soma_seg = cell.soma[0](0.5)

    from chirpUtils import applyChirp, getChirp
    amp = 0.025
    f0, f1, t0, Fs, delay = 0.5, 10, 10, 1000, 5 # for looking at bimodal leading phase response in Hay cell
    I, t = getChirp(f0, f1, t0, amp, Fs, delay)
    print('running chirp on ' + str(seg))
    applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1, out_file_name=filename)
    
    print(str(sec) + ' ' + str(loc) + ': done')

#populate data tuple
data = []
models = ['kole', 'neymotinkole', 'neymotinharnett', 'neymotinmigliore', 'hay', 'ackerantic']
## handle each model accordingly
# for model in models:
model = sys.argv[-1]
if model == 'kole':
    from getCells import KoleCell
    cell, trunk = KoleCell()
    for sec_num in trunk:
        nseg = cell.apic[sec_num].nseg 
        if nseg == 1:
            data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/Kole/trunk_data/'+str(cell.apic[sec_num](0.5))])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/Kole/trunk_data/'+str(cell.apic[sec_num](loc))])
if model == 'neymotinkole':
    from getCells import NeymotinKoleCell
    cell = NeymotinKoleCell()
    for sec_num, sec in enumerate(cell.apical_maintrunk):
        nseg = sec.nseg 
        if nseg == 1:
            data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/Neymotin/kole_trunk_data/'+str(cell.apic[sec_num](0.5))])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/Neymotin/kole_trunk_data/'+str(cell.apic[sec_num](loc))])
if model == 'neymotinharnett':
    from getCells import NeymotinHarnettCell
    cell = NeymotinHarnettCell()
    for sec_num, sec in enumerate(cell.apical_maintrunk):
        nseg = sec.nseg 
        if nseg == 1:
            data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/Neymotin/harnett_trunk_data/'+str(cell.apic[sec_num](0.5))])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/Neymotin/harnett_trunk_data/'+str(cell.apic[sec_num](loc))])
if model == 'neymotinmigliore':
    from getCells import NeymotinMiglioreCell
    cell = NeymotinMiglioreCell()
    for sec_num, sec in enumerate(cell.apical_maintrunk):
        nseg = sec.nseg 
        if nseg == 1:
            data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/Neymotin/migliore_trunk_data/'+str(cell.apic[sec_num](0.5))])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/Neymotin/migliore_trunk_data/'+str(cell.apic[sec_num](loc))])
if model == 'hay':
    from getCells import HayCell
    cell, trunk = HayCell()
    for sec_num in trunk:
        nseg = cell.apic[sec_num].nseg 
        if nseg == 1:
            data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/Hay/trunk_data/'+str(cell.apic[sec_num](0.5))])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/Hay/trunk_data/'+str(cell.apic[sec_num](loc))])
if model == 'ackerantic':
    from getCells import AckerAnticCell
    cell = AckerAnticCell()
    for sec_num in cell.apical_maintrunk:
        nseg = cell.apical[sec_num].nseg 
        if nseg == 1:
            data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/AckerAntic/trunk_data/'+str(cell.apic[sec_num](0.5))])
        else:
            for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/AckerAntic/trunk_data/'+str(cell.apic[sec_num](loc))])


data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(N)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()
