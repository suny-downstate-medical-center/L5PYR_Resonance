from getCells import HayCell
cell = HayCell()
from neuron import h, gui
from synUtils import *

soma_seg = cell.soma[0](0.5)
stim_segs = [cell.apic[2](0.5), cell.apic[36](0.8)]
ampa_weights = [0.125, 0.065]
nmda_weights = [0.03, 0.05]

start = 200
factor = 2

for i, stim_seg in enumerate(stim_segs):
    SC = ampa_weights[i]
    TP, TP_soma = getTp(stim_seg, start, SC / factor)
    sweepLags(stim_seg, soma_seg, SC / factor, SC / (factor*5), SC / (factor*10), start, TP, 1, outpath='/u/craig/L5PYR_Resonance/timeDomainOutput/Hay/')