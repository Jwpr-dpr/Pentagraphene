#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ase import Atoms
from ase.io  import  read 
from ase.visualize.plot import plot_atoms
from gpaw import GPAW,PW,FermiDirac
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter

label = 'PW_'
calc = GPAW('PW_Penta_gs.gpw',fixdensity=True,
            nbands=24,
            symmetry='off',
            kpts={'path':'GMXG','npoints':300},
            parallel={'sl_auto':True},
            txt=label+'pentagraphene-bs.log')
#---------------------------------------
#  run 
#---------------------------------------
calc.get_potential_energy()
bs = calc.band_structure()
bs.plot(filename=label+'bandstructurePentagrafeno.png', show=False, emax=10.0)


