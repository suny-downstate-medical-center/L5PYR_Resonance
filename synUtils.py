from neuron import h, init
h.load_file("stdrun.hoc")
import numpy as np 
import json
import multiprocessing

#calculate path length between two sections
def fromtodistance(origin_segment, to_segment):
    h.distance(0, origin_segment.x, sec=origin_segment.sec)
    return h.distance(to_segment.x, sec=to_segment.sec)

def createNMDAsyn(stim_seg, start, weight):
    # nmda params from Lajeunesse et al 2013
    syn = h.Exp2Syn(stim_seg)
    syn.tau1 = 0.5
    syn.tau2 = 13
    syn.e = 0
    
    stim = h.NetStim()
    stim.number = 1
    stim.start = start
    
    con = h.NetCon(stim, syn)
    con.weight[0] = weight

    i_vec = h.Vector()
    i_vec.record(syn._ref_i)

    return i_vec, con, syn, stim

def createAMPAsyn(stim_seg, start, weight):
    # ampa params from Lajeunesse et al 2013
    syn = h.Exp2Syn(stim_seg)
    syn.tau1 = 0.1
    syn.tau2 = 1.4
    syn.e = 0
    
    stim = h.NetStim()
    stim.number = 1
    stim.start = start
    
    con = h.NetCon(stim, syn)
    con.weight[0] = weight

    i_vec = h.Vector()
    i_vec.record(syn._ref_i)

    return i_vec, con, syn, stim

def setupRecordings(stim_seg, soma_seg):
    # basic recording vectors
    v_soma = h.Vector()
    t_vec = h.Vector()
    v_stim = h.Vector()
    v_soma.record(soma_seg._ref_v)
    v_stim.record(stim_seg._ref_v)
    t_vec.record(h._ref_t)
    return t_vec, v_stim, v_soma

def setupCurrentRecordings_hay(seg):
    # currents found in apical segments of hay cell
    currents = {}
    currents['i_hcn'] = h.Vector()
    currents['i_hcn'].record(seg.Ih._ref_ihcn)
    currents['i_ca_lvast'] = h.Vector()
    currents['i_ca_lvast'].record(seg.Ca_LVAst._ref_ica)
    currents['i_im'] = h.Vector()
    currents['i_im'].record(seg.Im._ref_ik)
    currents['i_ca_hva'] = h.Vector()
    currents['i_ca_hva'].record(seg.Ca_HVA._ref_ica)
    currents['i_nata'] = h.Vector()
    currents['i_nata'].record(seg.NaTa_t._ref_ina)
    currents['i_ske2'] = h.Vector()
    currents['i_ske2'].record(seg.SK_E2._ref_ik)
    currents['i_skv3'] = h.Vector()
    currents['i_skv3'].record(seg.SKv3_1._ref_ik)
    return currents

def conditionAndTest(stim_seg, soma_seg, Sc0, St0, dSt, start, lag, synType='AMPA'):
    # setup recordings
    t_vec, v_stim, v_soma = setupRecordings(stim_seg, soma_seg)
    
    # condition stim 
    if synType == 'AMPA':
        cond_i, condCon, condSyn, condStim = createAMPAsyn(stim_seg, start, Sc0)
        test_i, testCon, testSyn, testStim = createAMPAsyn(stim_seg, start + lag, St0)
    else:
        cond_i, condCon, condSyn, condStim = createNMDAsyn(stim_seg, start, Sc0)
        test_i, testCon, testSyn, testStim = createNMDAsyn(stim_seg, start + lag, St0)

    out_vecs = setupCurrentRecordings_hay(stim_seg)

    # time
    h.tstop = start + 300

    # find first St that generates spike
    didSpike = False 
    while not didSpike:
        testCon.weight[0] = St0
        print(str(St0))
        h.run()
        ## check for spike
        if np.max(v_soma.as_numpy()) > 10:
            didSpike = True
        else:
            ## increment weight by 10%
            St0 = St0 + dSt

    # fill out output structure with traces
    out_vecs['t_vec'] = t_vec
    out_vecs['v_stim'] = v_stim
    out_vecs['v_soma'] = v_soma
    out_vecs['cond_i'] = cond_i
    out_vecs['test_i'] = test_i

    return St0, out_vecs

def findSc(stim_seg, soma_seg, start, sc, dWeight, synType='AMPA'):
    # setup recordings
    t_vec, v_stim, v_soma = setupRecordings(stim_seg, soma_seg)

    # condition stim 
    if synType == 'AMPA':
        i_vec, condCon, condSyn, condStim = createAMPAsyn(stim_seg, start, sc)
    else:
        i_vec, condCon, condSyn, condStim = createNMDAsyn(stim_seg, start, sc)

    h.tstop = start + 300

    # first pass, make sure it does produce spike
    h.run()
    if np.max(v_soma.as_numpy()) > 10:
        didSpike = True
        sc = sc - dWeight
        ## decrement weight until no spike
        while didSpike:
            print(str(sc))
            condCon.weight[0] = sc
            h.run()
            ## check for spikes
            if np.max(v_soma.as_numpy()) < 10:
                didSpike = False
                ### back to suprathreshold weight
                sc = sc + dWeight
            else:
                sc = sc - dWeight
        return sc
    else:
        print("Error: started with a subthreshold weight")

def getTp(stim_seg, soma_seg, start, sc, synType='AMPA'):
    # setup recordings
    t_vec, v_stim, v_soma = setupRecordings(stim_seg, soma_seg)

    # condition stim 
    if synType == 'AMPA':
        i_vec, condCon, condSyn, condStim = createAMPAsyn(stim_seg, start, sc)
    else:
        i_vec, condCon, condSyn, condStim = createNMDAsyn(stim_seg, start, sc)
    
    # run sim
    h.tstop = start + 300
    h.run()

    # find where membrane potential returns to rest
    restVm = v_stim.as_numpy()[int(start*(1/h.dt) - 25*(1/h.dt))]
    a = v_stim.as_numpy()
    b = a[a > restVm - 0.1]
    c = b[b < restVm + 0.1]
    t = t_vec.as_numpy()
    t1 = t[a > restVm - 0.1]
    t2 = t1[b < restVm + 0.1]

    ## working backwards from end of sim see where stops being restVm
    diff = 0.02
    ind = -2
    while diff < 0.026:
        diff = t2[ind+1] - t2[ind]
        ind = ind - 1

    Tp = t2[ind+2] - start

    # same for soma  
    restVm_soma = v_soma.as_numpy()[int(start*(1/h.dt) - 25*(1/h.dt))]
    a = v_soma.as_numpy()
    b = a[a > restVm_soma - 0.1]
    c = b[b < restVm_soma + 0.1]
    t1 = t[a > restVm_soma - 0.1]
    t2 = t1[b < restVm_soma + 0.1]

    ## working backwards from end of sim see where stops being restVm
    diff = 0.02
    ind = -2
    while diff < 0.026:
        diff = t2[ind+1] - t2[ind]
        ind = ind - 1

    Tp_soma = t2[ind+2] - start

    return Tp, Tp_soma

def sweepLags(stim_seg, soma_seg, Sc0, St0, dSt, start, tP, dLag, synType='AMPA', outpath=None):
    # setup
    lag = 0
    testWeights = []
    lags = []

    # main loop
    while (start + lag) <= (start + tP):
        lags.append(lag)
        if synType == 'AMPA':
            S, traces = conditionAndTest(stim_seg, soma_seg, Sc0, St0, dSt, start, lag)
        else:
            S, traces = conditionAndTest(stim_seg, soma_seg, Sc0, St0, dSt, start, lag, synType='NMDA')
        trace_lists = {}
        for key in traces.keys():
            trace_lists[key] = traces[key].to_python()
        ## save output traces
        trace_file = outpath + str(stim_seg.sec) + '_lag' + str(np.round(lag,1)) + '_w' + str(np.round(S,3)) + '_traces.json'
        with open(trace_file, 'w') as fileObj:
            json.dump(trace_lists, fileObj)
        lag = lag + dLag
        testWeights.append(S)
        

    # output
    if outpath == None:
        return lags, testWeights 
    else:
        outfile = outpath + str(stim_seg.sec) + '_lagSweep.json'
        out = {'lags' : lags, 'weights' : testWeights, 'stim_seg' : str(stim_seg), 'Sc0' : Sc0}
        with open(outfile, 'w') as fileObj:
            json.dump(out, fileObj)

def conditionAndTestMulti(data):
    sec_num, sec_loc, Sc0, St0, dSt, start, lag, outpath = data
    from getCells import HayCell
    cell = HayCell()
    stim_seg = cell.apic[sec_num](sec_loc)
    soma_seg = cell.soma[0](0.5)
    print(str(stim_seg))
    print('starting lag: ' + str(np.round(lag,1)))
    S, traces = conditionAndTest(stim_seg, soma_seg, Sc0, St0, dSt, start, lag)
    trace_lists = {}
    for key in traces.keys():
        trace_lists[key] = traces[key].to_python()
    trace_lists['S'] = S
    trace_file = outpath + str(stim_seg.sec) + '_lag' + str(np.round(lag,1)) + '_w' + str(np.round(S,3)) + '_traces.json'
    with open(trace_file, 'w') as fileObj:
        json.dump(trace_lists, fileObj)
    print('DONE lag: ' + str(np.round(lag,1)))
    return S

def getLagData(sec_num, sec_loc, Sc0, St0, dSt, start, tP, dLag, outpath):
    data = []
    lag = 0
    while (start + lag) <= (start + tP):
        data_list = [sec_num, sec_loc, Sc0, St0, dSt, start, lag, outpath]
        data.append(data_list)
        lag = lag + dLag
    return data
