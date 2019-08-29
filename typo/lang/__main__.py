import sys
try:
    from .__init__ import *
    from . import __init__
    if not hasattr(__init__, 'TokenGet'):
        from .token import TokenGet
        __init__.TokenGet = TokenGet
    if not hasattr(__init__, 'Parse'):
        from .parse import Parse
        __init__.Parse = Parse
except ImportError: from typo.lang import *
run_script(sys.argv[1])