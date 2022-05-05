from netParams_unified import netParams 
from cfg_unified import cfg
from netpyne import sim as s
s.create(netParams, cfg)

sec_num = 'apic_20' # indicates stimulated section
loc = 0.5 # indicates stimulated compartment (0-1)
seg = s.net.cells[0].secs[sec_num]['hObj'](loc)
soma_seg = s.net.cells[0].secs['soma']['hObj'](0.5)

## record voltages
from neuron import h, gui
soma_v = h.Vector().record(soma_seg._ref_v)
dend_v = h.Vector().record(seg._ref_v)
time = h.Vector().record(h._ref_t)

## parameters of the chirp stimulus
from chirpUtils import applyChirp, getChirp
amp = 0.025 # amplitude of chirp stim
f0, f1, t0, Fs, delay = 0.5, 20, 20, 1000, 5 # initial and final frequencies, duration, sampling freq, delay
I, t = getChirp(f0, f1, t0, amp, Fs, delay) # defines current clamp

## run simulation
print('Running chirp on ' + str(seg))
out = applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1)

## plotting 
from matplotlib import pyplot as plt 
### traces
trace_fig = plt.figure(figsize=(8,10))
plt.subplot(3,1,1)
plt.plot(t,I)
plt.title('Chirp Sitmulation', fontsize=14)
plt.ylabel('Current (mA)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(4000,16000)
plt.subplot(3,1,2)
plt.plot(time, dend_v)
plt.title(r'Local V$_{memb}$', fontsize=14)
plt.ylabel(r'V$_{memb}$ (mV)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(4000,16000)
plt.ylim(-75,-71)
plt.subplot(3,1,3)
plt.plot(time,soma_v)
plt.title(r'Somatic V$_{memb}$', fontsize=14)
plt.xlabel('Time (ms)', fontsize=14)
plt.ylabel(r'V$_{memb}$ (mV)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlim(4000,16000)
plt.ylim(-76,-74)
plt.tight_layout()
plt.show()

### complex Zc
z_fig = plt.figure(figsize=(8,8))
plt.plot(out['ZinRes'], out['ZinReact'])
plt.xlabel(r'Resistance (M$\Omega$)', fontsize=14)
plt.ylabel(r'Reactance (M$\Omega$)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title(r'Transfer Impedance: Z$_{c}$', fontsize=16)
plt.show()

### ZAP
zAmp_fig = plt.figure(figsize=(8,8))
plt.plot(out['Freq'], out['ZcAmp'])
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel(r'|Z$_c$| (M$\Omega$)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Impedance Amplitude Profile: ZAP', fontsize=16)
plt.show()

### ZPP
zAmp_fig = plt.figure(figsize=(8,8))
plt.plot(out['Freq'], out['ZcPhase'])
plt.plot([0,10],[0,0])
plt.xlabel('Frequency (Hz)', fontsize=14)
plt.ylabel(r'$\Phi_c$ (radians)', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Impedance Phase Profile: ZPP', fontsize=16)
plt.show()