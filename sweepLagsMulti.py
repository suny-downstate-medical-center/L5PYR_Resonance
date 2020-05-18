import multiprocessing
from getCells import HayCell
cell = HayCell()
from synUtils import getLagData, getTp, conditionAndTestMulti

stim_seg = cell.apic[2](0.5)
soma_seg = cell.soma[0](0.5)
weight = 0.125
start = 200
factor = 4
Sc0 = weight / 2
St0 = weight / 4
dSt = weight / 10
Tp, _ = getTp(stim_seg, soma_seg, start, Sc0)

data = getLagData(Sc0, St0, dSt, start, Tp, 25, '/u/craig/L5PYR_Resonance/MultiTestData/')
data = tuple(data)

def mp_handler():
    p = multiprocessing.Pool(4)
    p.map(conditionAndTestMulti, data)

if __name__ == '__main__':
    mp_handler()