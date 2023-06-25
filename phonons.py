#!/usr/bin/env python
# coding: utf-8

from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase import Atoms
from gpaw import GPAW,PW,FermiDirac
from ase.io  import  read, write
import matplotlib.pyplot as plt


atoms = read("Penta_relaxed.cif")
calc = GPAW(mode=PW(650),xc = 'PBE',kpts={'size':(3,3,1),'gamma':True},symmetry = 'off',
	    occupations=FermiDirac(0.01))

ph = Phonons(atoms,calc,supercell=(5,5,1),delta=0.02)
ph.run()
ph.read(method='frederiksen',acoustic=True)
path = atoms.cell.bandpath('GMXG', npoints=200)
bs = ph.get_band_structure(path)
dos = ph.get_dos(kpts=(20,20,20)).sample_grid(npts=100,width=1e-3)

fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])

emax = 0.035
bs.plot(ax=ax, emin=0.0, emax=emax)

dosax = fig.add_axes([.8, .07, .17, .85])
dosax.fill_between(dos.get_weights(), dos.get_energies(), y2=0, color='grey',
                   edgecolor='k', lw=1)

dosax.set_ylim(0, emax)
dosax.set_yticks([])
dosax.set_xticks([])
dosax.set_xlabel("DOS", fontsize=18)

fig.savefig('pg_phonon.png')

