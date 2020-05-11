from getCells import AckerAnticCell
cell = AckerAnticCell()
from mpi4py import MPI
from neuron import h, gui
from chirpUtils import findSc, getTp, sweepLags
import numpy as np
# h.load_file('stdrun.hoc')

# pc = h.ParallelContext()
# pcid = pc.id()
# pc.set_maxstep(100)
pcid = 1

def wholeShebang(loc, cell):
    stim_seg = cell.basal[34](loc)
    soma_seg = cell.soma[0](0.5)

    v_stim = h.Vector()
    v_soma = h.Vector()
    t_vec = h.Vector()
    v_stim.record(stim_seg._ref_v)    
    v_soma.record(soma_seg._ref_v)
    t_vec.record(h._ref_t)
    start = 200
    factor = 4

    SC = findSc(stim_seg, soma_seg, start, 0.5, 0.01)
    TP = getTp(stim_seg, start, SC / 2)
    
    sweepLags(stim_seg, soma_seg, SC / factor, SC / (factor*5), SC / (factor*10), start, TP, 1, outfile='/u/craig/L5PYR_Resonance/timeDomainOutput/basal35_'+str(loc)+'.json')

locs = [0.25, 0.5, 0.75]
wholeShebang(locs[pcid, cell])

# pc.runworker()
# nseg = 11
# for loc in np.linspace(1/(nseg+1), nseg/(nseg+1), nseg):
#     pc.submit(wholeShebang, loc)

# while pc.working(): pass

