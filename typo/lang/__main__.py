import sys
try:
    from ._core import *
except ImportError: from typo.lang import *
run_script(sys.argv[1])