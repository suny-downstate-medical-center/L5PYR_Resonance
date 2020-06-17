from getCells import NeymotinCell
cell = NeymotinCell()

cfg = {'ihGbar' : 1.0,  # multiplicative factor for ih gbar in PT cells\
        'ihGbarBasal' : 1.0, # 0.1 # multiplicative factor for ih gbar in PT cells
        'ihlkc'           : 0.2, # ih leak param (used in Migliore)
        'ihlkcBasal'      : 1.0,
        'ihlkcBelowSoma'  : 0.01,
        'ihlke'           : -86,  # ih leak param (used in Migliore)
        'ihSlope'         : 14*2,
        'somaNa'      : 5,
        'dendNa'      : 0.3,
        'axonNa'      : 7,
        'axonRa'      : 0.005,
        'gpas' : 0.5,  # multiplicative factor for pas g in PT cells
        'epas' : 0.9}  # multiplicative factor for pas e in PT cells

from neuron import h

for sec in h.allsec():
    for seg in sec.allseg():
        if 'hd' in dir(seg):
            seg.hd.gbar = seg.hd.gbar * cfg['ihGbar']
            seg.hd.clk = cfg['ihlkc']
            seg.hd.elk = cfg['ihlkc']
            print('changed Ih in ' + str(seg))

for sec in cell.dend:
    for seg in sec.allseg():
            if 'hd' in dir(seg):
                seg.hd.gbar = seg.hd.gbar * cfg['ihGbarBasal']
                seg.hd.clk = seg.hd.clk * cfg['ihlkcBelowSoma']
                print('changed Ih in ' + str(seg))

for seg in cell.soma.allseg():
    if 'hd' in dir(seg):
        seg.hd.clk = seg.hd.clk * cfg['ihlkcBelowSoma']
        print('changed Ih in ' + str(seg))

for sec in cell.dend:
    for seg in cell.allseg():
        if 'nax' in dir(seg):
            seg.nax.gbar = 0.0153130368342 * cfg['dendNa']
        if 'pas' in dir(seg):
            seg.pas.e = seg.pas.e * cfg['epas']
            seg.pas.g = seg.pas.g * cfg['gpas']

for sec in cell.apic:
    for seg in cell.allseg():
        if 'nax' in dir(seg):
            seg.nax.gbar = 0.0153130368342 * cfg['dendNa']
        if 'pas' in dir(seg):
            seg.pas.e = seg.pas.e * cfg['epas']
            seg.pas.g = seg.pas.g * cfg['gpas']

for seg in cell.soma.allseg():
    if 'nax' in dir(seg):
        seg.nax.gbar = 0.0153130368342  * cfg['somaNa']

for seg in cell.axon.allseg():
    if 'nax' in dir(seg):
        seg.nax.gbar = 0.0153130368342  * cfg['axonNa']
    seg.geom.Ra = 137.494564931 * cfg['axonRa'] #0.005 

from chirpUtils import applyChirp, getChirp
amp = 0.0025
f0, f1, t0, Fs, delay = 0.5, 50, 50, 1000, 12 # for looking at bimodal leading phase response in Hay cell
I, t = getChirp(f0, f1, t0, amp, Fs, delay)
seg = cell.apic[26](0.5)
print('running chirp on ' + str(seg))
out = applyChirp(I, t, seg, cell.soma[0](0.5), t0, delay, Fs, f1, out_file_name='/u/craig/L5PYR_Resonance/Neymotin/testPTadjust')