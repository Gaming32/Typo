import sys
try: from .applets import *
except ImportError: from typo.lang.applets import *

ARGS = 'args'
SCRIPT = 'script'
SCRIPT_ARGS = 'script_args'
d = {
    ARGS : set(),
    SCRIPT : '',
    SCRIPT_ARGS : []
}

for arg in sys.argv[1:]:
    if arg[0] == '-':
        d[ARGS].add(arg)
    elif not d[SCRIPT]: d[SCRIPT] = arg
    else: d[SCRIPT_ARGS].append(arg)
if d[SCRIPT]:
    run_script(d[SCRIPT], d[SCRIPT_ARGS], '-v' in d[ARGS])
else:
    interactive_session()