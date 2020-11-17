**Introduction**
This package contains code used in Kelley et al. 2020 
[Effects of I$_h$ and TASK-like shunting current on dendritic impedance in layer 5 pyramidal-tract type neurons][https://www.biorxiv.org/].  
This includes standalone versions of pyramidal tract neuron models previously 
implemented in other studies, generalizable tools for computing neuronal impedance,
and scripts for batch processing and analysis.

**Basic Use**
Make sure you have installed [NEURON][https://www.neuron.yale.edu/neuron/] and [NETPYNE][http://netpyne.org/].

Clone this repository using 'git'.
> git clone https://github.com/suny-downstate-medical-center/L5PYR_Resonance.git

Compile .mod files for the cell models you want to use.  To run *init.py*, you
need to compile the .mod files from Dura-Bernal et al. 2019 in './M1_PTcell'.
> cd L5PYR_Resonance/M1_PTcell/
> nrnivmodl mod
> cd ../

To run an example simulation and compute impedance profiles for a single dendritic
compartment:
> python -i init.py

**Structure**
