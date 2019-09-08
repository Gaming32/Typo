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

def remove_sims(opt1, opt2):
    self = d[ARGS]
    if opt1 in self or opt2 in self:
        self.discard(opt1)
        self.discard(opt2)
        self.add(opt1)

for arg in sys.argv[1:]:
    if not d[SCRIPT] and arg[0] == '-':
        d[ARGS].add(arg)
    elif not d[SCRIPT]: d[SCRIPT] = arg
    else: d[SCRIPT_ARGS].append(arg)
remove_sims('-v', '--verbose')
if d[SCRIPT]:
    run_script(d[SCRIPT], d[SCRIPT_ARGS], '-v' in d[ARGS])
else:
    interactive_session('-v' in d[ARGS], d[ARGS])