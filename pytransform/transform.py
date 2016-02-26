# -*- coding: utf-8 -*-

"""pytransform.pytransform: provides entry point main()."""

__version__ = "0.1.1"

import sys
import argparse
from pytransform.utils import Transformation

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-pdb1", "--PDB1", help="first PDB Id")
    parser.add_argument("-chain1", "--CHAIN1", help="chain id for first PDB")
    parser.add_argument("-pdb2", "--PDB2", help="second PDB Id")
    parser.add_argument("-chain2", "--CHAIN2", help="chain id for second PDB")
    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)
    a = Transformation(args.PDB1, args.CHAIN1, args.PDB2, args.CHAIN2)
    a.transform()

if __name__ == '__main__':
    sys.exit(main())
