import sys
sys.path.insert(0,'../my_netpyne')
import os
os.environ["OPENBLAS_NUM_THREADS"] = sys.argv[-1]
N = int(sys.argv[-1])
from os import listdir, mkdir
import numpy as np
import multiprocessing
from math import nan
from scipy.io import savemat 

def chirpForMulti(invar):
    sec_num, loc, filename = invar
    from getCells import M1Cell
    s = M1Cell()
    seg = s.net.cells[0].secs[sec_num]['hObj'](loc)
    soma_seg = s.net.cells[0].secs['soma']['hObj'](0.5)

    from chirpUtils import applyChirp, getChirp
    amp = 0.025
    f0, f1, t0, Fs, delay = 0.5, 10, 10, 1000, 5 # for looking at bimodal leading phase response in Hay cell
    I, t = getChirp(f0, f1, t0, amp, Fs, delay)
    print('running chirp on ' + str(seg))
    applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1, out_file_name=filename)
    
    print(str(seg) + ': done')

#populate data tuple
data = []

from getCells import M1Cell
s = M1Cell()
for sec_key in s.net.cells[0].secLists['apical_maintrunk']:
    nseg = s.net.cells[0].secs[sec_key]['hObj'].nseg 
    if nseg == 1:
        data.append([sec_key, 0.5, '/u/craig/L5PYR_Resonance/M1_PTcell/trunk_data/'+sec_key+'_0.5'])
    else:
        for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
            data.append([sec_key, loc, '/u/craig/L5PYR_Resonance/M1_PTcell/trunk_data/'+sec_key+'_'+str(loc)])

data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(N)
    p.map(chirpForMulti, data)

if __name__ == '__main__':
    mp_handler()
