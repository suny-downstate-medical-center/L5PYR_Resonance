from getCells import HayCell
import numpy as np
import sys
from scipy.io import savemat
from math import nan

pt_cell = HayCell()

sec_list = [pt_cell.apic[58],
    pt_cell.apic[33],
    pt_cell.dend[12]]

soma_seg = pt_cell.soma[0](0.5)

from chirpUtils import applyChirp
from chirpUtils import getChirp
amp = 0.0025
amp = amp * 10 # as per srdjan's suggestion
amp = amp * 2
f0, f1, t0, Fs, delay = 0.5, 20, 20, 1000, 5 # 12 # original for all cells
I, t = getChirp(f0, f1, t0, amp, Fs, delay)

loc = 0.5
for sec in sec_list:
    out = applyChirp(I, t, sec(loc), soma_seg, t0, delay, Fs, f1, out_file_name='/u/craig/L5PYR_Resonance/amplitude_test_double/' + str(sec))