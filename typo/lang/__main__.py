import sys
try: from ._core import *
except ImportError: from typo.lang import *
set_verbose('-v' in sys.argv)
#set_excepthook()
run_script(sys.argv[1])