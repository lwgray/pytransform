# -*- coding: utf-8 -*-

"""pytransform.pytransform: provides entry point main()."""

__version__ = "0.1.0"

import sys
from .stuff import Transformation

def main():
    print("Executing pyTransform version %s." % __version__)
    # a = Transformation(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    # a.transform()
