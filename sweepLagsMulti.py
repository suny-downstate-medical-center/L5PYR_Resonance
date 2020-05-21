import multiprocessing
from getCells import HayCell
cell = HayCell()
from synUtils import getLagData, getTp, conditionAndTestMulti
import sys

if sys.argv[-1] == '2':
    stim_seg = cell.apic[2](0.5)
    soma_seg = cell.soma[0](0.5)
    weight = 0.125
    start = 200
    factor = 4
    Sc0 = weight / factor
    St0 = weight / (factor*5)
    dSt = weight / (factor*10)
    Tp, _ = getTp(stim_seg, soma_seg, start, Sc0)

    data = getLagData(2, 0.5, Sc0, St0, dSt, start, Tp, 1, '/u/craig/L5PYR_Resonance/timeDomainOutput/HayApic2/')
    data = tuple(data)

elif sys.argv[-1] == '36':
    stim_seg = cell.apic[36](0.8)
    soma_seg = cell.soma[0](0.5)
    weight = 0.065
    start = 200
    factor = 4
    Sc0 = weight / factor
    St0 = weight / (factor*5)
    dSt = weight / (factor*10)
    Tp, _ = getTp(stim_seg, soma_seg, start, Sc0)

    data = getLagData(36, 0.8, Sc0, St0, dSt, start, Tp, 1, '/u/craig/L5PYR_Resonance/timeDomainOutput/HayApic36/')
    data = tuple(data)

elif sys.argv[-1] == '14':
    stim_seg = cell.apic[14](0.5)
    soma_seg = cell.soma[0](0.5)
    weight = 0.14
    start = 200
    factor = 4
    Sc0 = weight / factor
    St0 = weight / (factor*5)
    dSt = weight / (factor*10)
    Tp, _ = getTp(stim_seg, soma_seg, start, Sc0)

    data = getLagData(14, 0.5, Sc0, St0, dSt, start, Tp, 1, '/u/craig/L5PYR_Resonance/timeDomainOutput/HayApic14/')
    data = tuple(data)

# data = (data1 + data2 + data3)

def mp_handler():
    p = multiprocessing.Pool(6)
    p.map(conditionAndTestMulti, data)

if __name__ == '__main__':
    mp_handler()