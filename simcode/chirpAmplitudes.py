from getCells import AckerAnticCell
import numpy as np
import sys
from scipy.io import savemat
from math import nan

pt_cell = AckerAnticCell()

sec_list = [pt_cell.apical[15],
    pt_cell.apical[34],
    pt_cell.basal[8]]

soma_seg = pt_cell.soma[0](0.5)

from chirpUtils import applyChirp
from chirpUtils import getChirp
amp = 0.0025
amp = amp * 10 # as per srdjan's suggestion
f0, f1, t0, Fs, delay = 0.5, 50, 50, 1000, 5 # 12 # original for all cells
I, t = getChirp(f0, f1, t0, amp, Fs, delay)

loc = 0.5
for sec in sec_list:
    out = applyChirp(I, t, sec(loc), soma_seg, t0, delay, Fs, f1, out_file_name='/u/craig/L5PYR_Resonance/amplitude_test/' + str(sec))