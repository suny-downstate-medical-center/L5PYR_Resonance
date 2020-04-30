from neuron import h, init
#h.load_file("/usr/local/nrn//share/nrn/lib/hoc/stdrun.hoc")
# h.load_file("stdrun.hoc")
import numpy as np 
from scipy.signal import chirp
from pylab import fft, convolve
from scipy.io import savemat

# get chirp stim: based on sam's code form evoizhi/sim.py
def getChirp(f0, f1, t0, amp, Fs, delay):
    time = np.linspace(0,t0+delay*2, (t0+delay*2)*Fs+1)
    chirp_time = np.linspace(0, t0, (t0)*Fs+1)
    ch = chirp(chirp_time, f0, t0, f1, method='linear',phi=-90)
    ch = np.hstack((np.zeros(Fs*delay), ch, np.zeros(Fs*delay)))
    vch = h.Vector(); vch.from_python(ch); vch.mul(amp)
    vtt = h.Vector(); vtt.from_python(time); vtt.mul(Fs)
    return vch, vtt

# get chirp stim: based on sam's code form evoizhi/sim.py
def getChirpLog(f0, f1, t0, amp, Fs, delay):
    time = np.linspace(0,t0+delay*2, (t0+delay*2)*Fs+1)
    chirp_time = np.linspace(0, t0, (t0)*Fs+1)
    ch = chirp(chirp_time, f0, t0, f1, method='linear',phi=-90)
    ch = np.hstack((np.zeros(Fs*delay), ch, np.zeros(Fs*delay)))
    vch = h.Vector(); vch.from_python(ch); vch.mul(amp)
    vtt = h.Vector(); vtt.from_python(time); vtt.mul(Fs)
    return vch, vtt

#calculate path length between two sections
def fromtodistance(origin_segment, to_segment):
    h.distance(0, origin_segment.x, sec=origin_segment.sec)
    return h.distance(to_segment.x, sec=to_segment.sec)

# comput impedance measures
def zMeasures(current, v,  delay, sampr, f1, bwinsz=1):
    ## zero padding
    current = current[int(delay*sampr - 0.5*sampr+1):-int(delay*sampr- 0.5*sampr)]
    current = np.hstack((np.repeat(current[0],int(delay*sampr)),current, np.repeat(current[-1], int(delay*sampr))))
    current = current - np.mean(current)
    v = v[int(delay*sampr - 0.5*sampr)+1:-int(delay*sampr - 0.5*sampr)]
    v = np.hstack((np.repeat(v[0],int(delay*sampr)), v, np.repeat(v[-1], int(delay*sampr))))
    v = v - np.mean(v)

    ## input and transfer impedance
    f_current = (fft(current)/len(current))[0:int(len(current)/2)]
    f_cis = (fft(v)/len(v))[0:int(len(v)/2)]
    z = f_cis / f_current

    ## impedance measures
    Freq       = np.linspace(0.0, sampr/2.0, len(z))
    zAmp       = abs(z)
    zPhase     = np.arctan(np.imag(z)/np.real(z))
    zRes       = np.real(z)
    zReact     = np.imag(z)

    ## smoothing
    fblur = np.array([1.0/bwinsz for i in range(bwinsz)])
    zAmp = convolve(zAmp,fblur,'same')
    zPhase = convolve(zPhase, fblur, 'same')
    zRes = convolve(zRes, fblur, 'same')
    zReact = convolve(zReact, fblur, 'same')

    ## trim
    mask = (Freq >= 0.5) & (Freq <= f1)
    Freq, zAmp, zPhase, zRes, zReact = Freq[mask], zAmp[mask], zPhase[mask], zRes[mask], zReact[mask]

    ## resonance
    zResAmp    = np.max(zAmp)
    zResFreq   = Freq[np.argmax(zAmp)]
    Qfactor    = zResAmp / zAmp[0]
    fVar      = np.std(zAmp) / np.mean(zAmp)

    return Freq, zAmp, zPhase, zRes, zReact, zResAmp, zResFreq, Qfactor, fVar

# voltage attenuation
def Vattenuation(ZinAmp, ZcAmp):
    out = (ZinAmp-ZcAmp) / ZinAmp
    return out

# phase lag
def phaseLag(ZinPhase, ZcPhase):
    out = ZinPhase - ZcPhase
    return out

# apply chirp stimulus to segment
def applyChirp(I, t, seg, soma_seg, t0, delay, Fs, f1, out_file_name = None):

    ## place current clamp on soma
    stim = h.IClamp(seg)
    stim.amp = 0
    stim.dur = (t0+delay*2) * Fs + 1
    I.play(stim._ref_amp, t)

    ## Record time
    t_vec = h.Vector()
    t_vec.record(h._ref_t)

    ## Record soma voltage
    soma_v = h.Vector()
    soma_v.record(soma_seg._ref_v)
    cis_v = h.Vector()
    cis_v.record(seg._ref_v)
    
    ## run simulation
    h.celsius = 34
    h.tstop = (t0+delay*2) * Fs + 1
    h.run()

    soma_np = soma_v.as_numpy()
    
    current_np = np.interp(np.linspace(0, (t0+delay*2) * Fs, soma_np.shape[0], endpoint=True),
                           np.linspace(0,(t0+delay*2) * Fs,(t0+delay*2) * Fs + 1,endpoint=True), I.as_numpy())
    time = t_vec.as_numpy()
    cis_np = cis_v.as_numpy()
    
    samp_rate = (1 / (time[1] - time[0])) * Fs
    
    ## calculate impedance
    Freq, ZinAmp, ZinPhase, ZinRes, ZinReact, ZinResAmp, ZinResFreq, QfactorIn, fVarIn = zMeasures(current_np, cis_np,  delay, samp_rate, f1, bwinsz=20)
    _, ZcAmp, ZcPhase, ZcRes, ZcReact, ZcResAmp, ZcResFreq, QfactorTrans, fVarTrans = zMeasures(current_np, soma_np,  delay, samp_rate, f1, bwinsz=20)

    v_attenuation = Vattenuation(ZinAmp, ZcAmp)
    phase_lag = phaseLag(ZinPhase, ZcPhase)

    dist = fromtodistance(seg, soma_seg)

    ## generate output
    out = {'Freq' : Freq,
        'ZinRes' : ZinRes,
        'ZinReact' : ZinReact,
        'ZinAmp' : ZinAmp,
        'ZinPhase' : ZinPhase,
        'ZcRes' : ZcRes,
        'ZcReact' : ZcReact,
        'ZcAmp' : ZcAmp,
        'ZcPhase' : ZcPhase,
        'phase_lag' : phase_lag,
        'Vattenuation' : v_attenuation,
        'ZinResAmp' : ZinResAmp,
        'ZinResFreq' : ZinResFreq,
        'ZcResAmp' : ZcResAmp,
        'ZcResFreq' : ZcResFreq,
        'QfactorIn' : QfactorIn,
        'QfactorTrans' : QfactorTrans,
        'fVarIn' : fVarIn,
        'fVarTrans' : fVarTrans,
        'dist' : dist}

    out2 = {'soma_np' : soma_np,
            'cis_np' : cis_np,
            'time' : time,
            'current_np' : current_np}

    if out_file_name:
        savemat(out_file_name + '.mat', out)
        savemat(out_file_name + '_traces.mat', out2)
    else:
        return out
