# Introduction
This package contains code used in  
[Effects of Ih and TASK-like shunting current on dendritic impedance in layer 5 pyramidal-tract type neurons](https://www.biorxiv.org/content/10.1101/2021.01.08.425962v1) (Kelley et al. 2020).  

This includes generalizable tools for computing neuronal impedance, 
standalone versions of pyramidal tract neuron models previously 
implemented in other studies, and scripts for batch processing and analysis.

# Basic Use
Make sure you have installed [NEURON](https://www.neuron.yale.edu/neuron/) and [NETPYNE](http://netpyne.org/).

Clone this repository using 'git'
```
git clone https://github.com/suny-downstate-medical-center/L5PYR_Resonance.git
```

Compile .mod files for the cell model(s) you want to use.  To run *init.py*, you
need to compile the .mod files from Dura-Bernal et al. 2019 in './models/DuraBernal'.
```
cd L5PYR_Resonance/models/DuraBernal/
nrnivmodl mod
cd ../../
```
To run an example simulation and compute impedance profiles for a single dendritic
compartment:
```
python -i init.py
```

# Code
## init.py 
Example simulation of chirp current stimulation of the apical trunk and computation
of transfer impedance between stimulated dendrite and the soma.  The chirp stimulus
provides sinusoidal current stimultion with instantaneous frequency linearly
increasing from 0.5-10Hz in 10s. Transfer impedance is computed from the resulting
somatic membrane potential waveforms.

## getCells.py
Contains functions for loading stand-alone versions of 
pyramidal-tract type neurons used in the manuscript. 
There are also functions for automatically downloading and instantiating models
from the [Allen Brain Atlas](https://portal.brain-map.org/).

## chirpUtils.py
Contains functions for simulating chirp current stimulation and
computing neuronal impedance.  

## ./models/
Contains folders with each of the cell models studied in the 
manuscript.  Each of those folders contains .mod files that must be compiled prior
to runtime. Also includes simplified model presented in the paper that was built with
NEURON's LinearCircuitBuilder: 'cellwithL.ses'. This model can be used interactively 
by running:
```
from neuron import h, gui
h.load_file('models/cellwithL.ses')
```
Note that circuit elements will not be recognized by NEURON unless the 'Simulate'
button is selected on the LinearCircuit window.

## ./simcode/ 
Contains scripts used to run the batch simulations and analyses used in the study. 
Many of these are machine specific and weren't intended for general use. 