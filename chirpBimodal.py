# Load in the goods
import numpy as np
import sys
from scipy.io import savemat
from math import nan

# parse cmd line inputs, load PT cell template
## load cell
from getCells import HayCell
pt_cell = HayCell()

## specify stimulated section and soma segment
secList = [pt_cell.apic[9]]#, pt_cell.apic[65]]
soma_seg = pt_cell.soma[0](0.5)

# define current stimulus
from chirpUtils import applyChirp
from chirpUtils import getChirp
amp = 0.0025
## f0, f1, t0, Fs, delay = 0.5, 50, 50, 1000, 12 # original for all cells
f0, f1, t0, Fs, delay = 0.5, 100, 100, 1000, 5 # for looking at bimodal leading phase response in Hay cell
I, t = getChirp(f0, f1, t0, amp, Fs, delay)

# define output variables

#main loop
for sec in secList:
    nseg = sec.nseg
    if nseg == 1:
        loc = 0.5
        applyChirp(I, t, sec(loc), soma_seg, t0, delay, Fs, f1, out_file_name='/home/craig_kelley_downstate_edu/L5PYR_Resonance/Hay/Bimodal/' + str(sec(loc)))
    else:
        for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
            applyChirp(I, t, sec(loc), soma_seg, t0, delay, Fs, f1, out_file_name='/home/craig_kelley_downstate_edu/L5PYR_Resonance/Hay/Bimodal/' + str(sec(loc)))