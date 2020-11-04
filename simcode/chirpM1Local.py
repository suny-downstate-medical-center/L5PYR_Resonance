import sys
from os import listdir, mkdir
import numpy as np
import multiprocessing
from math import nan
from scipy.io import savemat 

from getCells import M1Cell
s = M1Cell()
sec_num = sys.argv[-2]
loc = float(sys.argv[-1])
from neuron import h 
for sec in h.allsec():
    for seg in sec.allseg():
        try:
            seg.cal.gcalbar = s.net.cells[0].secs['soma']['hObj'](0.5).gcalbar
        except:
            pass
seg = s.net.cells[0].secs[sec_num]['hObj'](loc)
soma_seg = s.net.cells[0].secs['soma']['hObj'](0.5)
from chirpUtils import applyChirp, getChirp
amp = 0.025
f0, f1, t0, Fs, delay = 0.5, 10, 10, 1000, 5 # for looking at bimodal leading phase response in Hay cell
I, t = getChirp(f0, f1, t0, amp, Fs, delay)
print('running chirp on ' + str(seg))
filename = 'M1_PTcell/nohotzone_trunk_data/'+sec_num+sys.argv[-1]
applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1, out_file_name=filename)
