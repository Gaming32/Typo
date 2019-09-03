import sys
try: from .__init__ import *
except ImportError: from typo.lang import *
set_verbose('-v' in sys.argv)
# set_excepthook()
# try: set_excepthook()
# except NameError:
#     from ._core import *
#     set_excepthook()
run_script(sys.argv[1])