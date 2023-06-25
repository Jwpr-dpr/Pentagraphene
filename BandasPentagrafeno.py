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


st_relax = read("Penta_relaxed.cif")
calc = GPAW(mode=PW(750),
            xc='PBE',
            kpts=(4,4, 1),
            occupations=FermiDirac(0.01),
            txt='Penta_gs.log')
#st_relax.calc =calc
#st_relax.get_potential_energy()
#calc.write("Penta_gs.gpw")
print("ok")

calc_bands =GPAW('Penta_gs.gpw').fixed_density(
    nbands='nao',
    symmetry='off',
    kpts={'path': 'GXG', 'npoints': 60},
    convergence={'bands': 16},
    txt='pentagraphene-bs.log')
#calc = GPAW('Penta_gs.gpw',fixdensity=True,
#            nbands='nao',
#            symmetry='off',
#            kpts={'path':'GX','npoints':100},
#            convergence={'bands': 24},
#            txt='pentagraphene-bs.log')
#---------------------------------------
#  run 
#---------------------------------------
calc_bands.get_potential_energy()
print("Ok, get  energy")
bs = calc_bands.band_structure()
bs.plot(filename='bandstructure.png', show=False, emax=10.0)

