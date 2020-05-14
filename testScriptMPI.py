from getCells import AckerAnticCell
cell = AckerAnticCell()
from mpi4py import MPI
from neuron import h, gui
from chirpUtils import findSc, getTp, sweepLags
import numpy as np
# h.load_file('stdrun.hoc')

pc = h.ParallelContext()
pcid = pc.id()
pc.set_maxstep(100)
#pcid = 0

def wholeShebang(loc, cell, SC):
    stim_seg = cell.basal[33](loc)
    soma_seg = cell.soma[0](0.5)
    print(str(loc))
    print(str(SC))

    v_stim = h.Vector()
    v_soma = h.Vector()
    t_vec = h.Vector()
    v_stim.record(stim_seg._ref_v)    
    v_soma.record(soma_seg._ref_v)
    t_vec.record(h._ref_t)
    start = 200
    factor = 4
    # firstShot = 0.75
    # SC = findSc(stim_seg, soma_seg, start, firstShot, 0.01)
    TP = getTp(stim_seg, start, SC / factor)
    
    sweepLags(stim_seg, soma_seg, SC / factor, SC / (factor*5), SC / (factor*10), start, TP, 1, outfile='/u/craig/L5PYR_Resonance/timeDomainOutput/basal35_'+str(loc)+'.json')

# locs = [0.25, 0.5, 0.75]
locs = [0.1, 0.5, 0.9]
SCs = [0.06, 0.65, 1100]
wholeShebang(locs[pcid], cell, SCs[pcid])

# pc.runworker()
# nseg = 11
# for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
#     pc.submit(wholeShebang, loc)

# while pc.working(): pass