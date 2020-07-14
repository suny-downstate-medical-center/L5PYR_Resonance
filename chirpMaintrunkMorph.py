import sys
import os
os.environ["OPENBLAS_NUM_THREADS"] = sys.argv[-1]
N = int(sys.argv[-1])
from os import listdir, mkdir
import numpy as np
import multiprocessing
from math import nan
from scipy.io import savemat 
import json

def chirpForMulti(invar):
    model, sec_num, loc, filename = invar
    cell = HayCellSWC('../suter_shepherd/' + model)
    seg = cell.apic[sec_num](loc)
    soma_seg = cell.soma[0](0.5)
    from chirpUtils import applyChirp, getChirp
    amp = 0.025
    f0, f1, t0, Fs, delay = 0.5, 10, 10, 1000, 5 # for looking at bimodal leading phase response in Hay cell
    I, t = getChirp(f0, f1, t0, amp, Fs, delay)
    print('running chirp on ' + str(seg))
    applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1, out_file_name=filename)
    
    print(str(seg) + ': done')

#populate data tuple
data = []
with open('suter_shepherd_trunk_data.json','rb') as fileObj:
    models = json.load(fileObj)

## handle each model accordingly
# for model in models:
# model = sys.argv[-1]
for model in models.keys():
    if len(models[model]) > 0:
        cellID = model.split('.')[0]
        try:
            os.mkdir('/u/craig/L5PYR_Resonance/Hay/suter_trunk_data/'+cellID+'/')
        except:
            pass
        from getCells import HayCellSWC
        cell = HayCellSWC('../suter_shepherd/'+model)
        for sec_num in models[model]:
            nseg = cell.apic[sec_num].nseg 
            if nseg == 1:
                data.append([model, sec_num, 0.5, '/u/craig/L5PYR_Resonance/Hay/suter_trunk_data/'+cellID+'/'+str(cell.apic[sec_num](0.5))])
            else:
                for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
                    data.append([model, sec_num, loc, '/u/craig/L5PYR_Resonance/Hay/suter_trunk_data/'+cellID+'/'+str(cell.apic[sec_num](loc))])

data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(N)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()
