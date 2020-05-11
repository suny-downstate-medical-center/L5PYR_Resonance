from getCells import AckerAnticCell
cell = AckerAnticCell()
from neuron import h, gui
from chirpUtils import findSc
stim_seg = cell.basal[12](0.5)
# stim_seg = cell.apical[15](0.5)
# stim_seg = cell.apical[2](0.5)
soma_seg = cell.soma[0](0.5)
v_stim = h.Vector()
v_soma = h.Vector()
t_vec = h.Vector()
v_stim.record(stim_seg._ref_v)    
v_soma.record(soma_seg._ref_v)
t_vec.record(h._ref_t)
start = 200
SC = findSc(stim_seg, soma_seg, start, 0.5, 0.01)
# SC = findSc(stim_seg, soma_seg, start, 0.006, 0.0001)
from chirpUtils import getTp
TP = getTp(stim_seg, start, SC / 2)
from chirpUtils import sweepLags
allLags = []
allWeights = []
factors = [2, 4, 8, 16]
for factor in factors:
    lags, testWeights = sweepLags(stim_seg, soma_seg, SC / factor, SC / (factor*5), SC / (factor*10), start, TP, 5)#TP / 10)
    allLags.append(lags)
    allWeights.append(testWeights)