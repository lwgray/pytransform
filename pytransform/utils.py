# -*- coding: utf-8 -*-

"""pyTransform.stuff: module within the pyTransform package."""

import MDAnalysis
import numpy as np
import csv
import warnings


warnings.filterwarnings("ignore")

class Transformation(object):
    def __init__(self, pdb1, chain1, pdb2, chain2):
        self.pdb1 = pdb1
        self.pdb2 = pdb2
        self.chain1 = chain1
        self.chain2 = chain2
        self.struc1 = "pdb" + pdb1.lower() + ".ent"
        self.struc2 = "pdb" + pdb2.lower() + ".ent"
        pass 
    
    def transform(self):
        ref = MDAnalysis.Universe(self.struc1, format='pdb', permissive=False)
        mobile = MDAnalysis.Universe(self.struc2, format='pdb', permissive=False)
        ref = ref.selectAtoms("segid {0}".format(self.chain1.upper()))
        mobile = mobile.selectAtoms("segid {0}".format(self.chain2.upper()))
        tr1 = None
        tr2 = None
        rot = None
        data = []
        pdb1 = self.pdb1.upper()
        pdb2 = self.pdb2.upper()
        myfile = "{0}_{1}.Tf".format(pdb1, pdb2)
        with open(myfile, 'r') as input:
            reader = csv.reader(input, delimiter=",")
            for line in reader:
                data.append(line[0])
        tr1 = np.array([float(data[0]), float(data[1]), float(data[2])])
        tr2 = np.array([float(data[3]), float(data[4]), float(data[5])])
        rot = np.matrixlib.defmatrix.matrix([[float(data[6]), float(data[7]), float(data[8])],
                                             [float(data[9]), float(data[10]), float(data[11])],
                                             [float(data[12]), float(data[13]), float(data[14])]])
        ref.atoms.translate(-tr1)
        ref.atoms.rotate(rot)
        mobile.atoms.translate(-tr2)
        final = MDAnalysis.Merge(ref, mobile)
        final.atoms.write("{0}_{1}.pdb".format(pdb1, pdb2))
