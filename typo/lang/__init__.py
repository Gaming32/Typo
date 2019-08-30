class typo_error(Exception):
    "Common base class for all Typo Script exceptions"
    name = 'Error'
class unknown_error(typo_error): name = 'UnknownError'
import sys
if '-v' in sys.argv:
    verbose = print
else:
    verbose = (lambda *p, **k: None)
try:
    from .token import TokenGet
    from .parse import Parse
except ImportError: pass
def run_script(path):
    file = open(path)
    tkn = TokenGet()
    prs = Parse(tkn)
    for line in file:
        tkn.reset(line)
        tkn.scan()
        if not tkn.nextline: prs.run()
    return tkn, prs
def run_line(line, vars={}, funcs={}):
    return Parse(TokenGet(line).scan(), vars, funcs).run()
def run_lines(lines, vars={}, funcs={}):
    tkn = TokenGet()
    prs = Parse(tkn)
    for line in lines.splitlines():
        tkn.reset(line)
        tkn.scan()
        if not tkn.nextline: prs.run()
    vars.update(prs.vars)
    funcs.update(prs.funcs)
    return tkn, prs