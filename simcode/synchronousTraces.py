# from getCells import M1Cell
import numpy as np
# s = M1Cell()
# seg = s.net.cells[0].secs['apic_22']['hObj'](0.5)
# soma_seg = s.net.cells[0].secs['soma']['hObj'](0.5)
from getCells import NeymotinHarnettCell
cell = NeymotinHarnettCell()
seg = cell.apic[22](0.5)
soma_seg = cell.soma(0.5)
from neuron import h
dend_v = h.Vector().record(seg._ref_v)
soma_v = h.Vector().record(soma_seg._ref_v)
time = h.Vector().record(h._ref_t)

amp = 0.05
f0, f1, t0, Fs, delay = 2, 2, 2, 1000, 5 
from chirpUtils import getChirp, applyChirp
I, t = getChirp(f0, f1, t0, amp, Fs, delay)
out = applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1)

soma_np = soma_v.as_numpy()
dend_np = dend_v.as_numpy()
time_np = time.as_numpy()
sampr = (1 / (time[1] - time[0])) * Fs
dend_np = dend_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]
soma_np = soma_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]

dend_np = dend_np - dend_np[0]
soma_np = soma_np - soma_np[0]
dend_np = np.divide(dend_np,np.max(dend_np))
soma_np = np.divide(soma_np, np.max(soma_np))

from matplotlib import pyplot as plt 
plt.ion()
plt.subplot(2,1,1)
plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),dend_np, 'c-', label='Dendrite')
plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),soma_np, 'c--', label='Soma')
plt.legend()
plt.title('Neymotin et al., 2017', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

del(cell)
del(seg)
del(soma_seg)
del(h)
from getCells import M1Cell
# import numpy as np
s = M1Cell()
seg = s.net.cells[0].secs['apic_22']['hObj'](0.5)
soma_seg = s.net.cells[0].secs['soma']['hObj'](0.5)
# from getCells import NeymotinHarnettCell
# cell = NeymotinHarnettCell()
# seg = cell.apic[22](0.5)
# soma_seg = cell.soma(0.5)
from neuron import h
dend_v = h.Vector().record(seg._ref_v)
soma_v = h.Vector().record(soma_seg._ref_v)
time = h.Vector().record(h._ref_t)

amp = 0.05
f0, f1, t0, Fs, delay = 2, 2, 2, 1000, 5 
from chirpUtils import getChirp, applyChirp
I, t = getChirp(f0, f1, t0, amp, Fs, delay)
out = applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1)

soma_np = soma_v.as_numpy()
dend_np = dend_v.as_numpy()
time_np = time.as_numpy()
sampr = (1 / (time[1] - time[0])) * Fs
dend_np = dend_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]
soma_np = soma_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]

dend_np = dend_np - dend_np[0]
soma_np = soma_np - soma_np[0]
dend_np = np.divide(dend_np,np.max(dend_np))
soma_np = np.divide(soma_np, np.max(soma_np))

plt.subplot(2,1,2)
plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),dend_np, 'm-', label='Dendrite')
plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),soma_np, 'm--', label='Soma')
plt.legend()
plt.title('Dura-Bernal et al., 2019', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# f0, f1, t0, Fs, delay = 6.4, 6.4, 1, 1000, 5
# f0, f1, t0, Fs, delay = 3.8, 3.8, 1, 1000, 5
# # from chirpUtils import getChirp, applyChirp
# I, t = getChirp(f0, f1, t0, amp, Fs, delay)
# out = applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1)

# soma_np = soma_v.as_numpy()
# dend_np = dend_v.as_numpy()
# time_np = time.as_numpy()
# sampr = (1 / (time[1] - time[0])) * Fs
# dend_np = dend_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]
# soma_np = soma_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]

# dend_np = dend_np - dend_np[0]
# soma_np = soma_np - soma_np[0]
# dend_np = np.divide(dend_np,np.max(dend_np))
# soma_np = np.divide(soma_np, np.max(soma_np))

# plt.subplot(3,1,2)
# plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),dend_np, label='Dendrite')
# plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),soma_np, label='Soma')
# # plt.legend()
# # plt.title('Synchronous Frequnecy: 6.4 Hz', fontsize=16)
# plt.title('Synchronous Frequnecy: 3.8 Hz', fontsize=16)
# plt.ylabel('Normalized Membrane Potential', fontsize=16)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)

# f0, f1, t0, Fs, delay = 20, 20, 1, 1000, 5
# # from chirpUtils import getChirp, applyChirp
# I, t = getChirp(f0, f1, t0, amp, Fs, delay)
# out = applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1)

# soma_np = soma_v.as_numpy()
# dend_np = dend_v.as_numpy()
# time_np = time.as_numpy()
# sampr = (1 / (time[1] - time[0])) * Fs
# dend_np = dend_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]
# soma_np = soma_np[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]

# dend_np = dend_np - dend_np[0]
# soma_np = soma_np - soma_np[0]
# dend_np = np.divide(dend_np,np.max(dend_np))
# soma_np = np.divide(soma_np, np.max(soma_np))

# plt.subplot(3,1,3)
# plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),dend_np, label='Dendrite')
# plt.plot(np.linspace(-0.5,t0+0.5,len(dend_np)),soma_np, label='Soma')
# # plt.legend()
# plt.title('20 Hz', fontsize=16)
# plt.xlabel('Time (s)', fontsize=16)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)