from __future__ import absolute_import

# Enable importing modules from parent directory (web root directory)
from os.path import dirname, realpath
parentdir = dirname(dirname(dirname(realpath(__file__))))
import os
os.sys.path.insert(0, parentdir)


from unittest import TestCase

