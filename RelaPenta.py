#coding: utf-8

from ase import Atoms
from ase.io  import  read 
from ase.visualize.plot import plot_atoms
from gpaw import GPAW,PW,FermiDirac
from math import sqrt
import numpy as np
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter

penta = read("penta.cif")
calc = GPAW(mode=PW(750),
            xc='PBE',
            kpts=(4,4, 1),
            occupations=FermiDirac(0.01),
            txt='Penta_relaxed.log')

penta.calc = calc
#---------------------------------------
# relajacion
#---------------------------------------

Scell = ExpCellFilter(penta,mask=[1,1,0,0,0,1])
relax = BFGS(Scell)
relax.run(fmax=0.04)
penta.write("Penta_relaxed.cif")

