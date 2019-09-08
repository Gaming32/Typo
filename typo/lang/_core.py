import sys
import traceback
from ._info import *
def print_error(exctype, value, tb):
    # print('temp notification')
    verbose('Python exception was:')
    verbose(''.join(traceback.format_exception(exctype, value, tb)))

    if not issubclass(exctype, typo_error):
        exctype = unknown_error
    print(exctype.name, ':', value.args[0])
    display = exctype.display(value.args)
    if display is not None: print(display)
def set_excepthook(): sys.excepthook = print_error
class typo_error(Exception):
    "Common base class for all Typo Script exceptions"
    name = 'Error'
    @staticmethod
    def display(args): return None
class unknown_error(typo_error): name = 'UnknownError'
_verbose = (lambda *p, **k: None)
def set_verbose(do_verbose_log):
    global _verbose
    if do_verbose_log:
        _verbose = print
    else:
        _verbose = (lambda *p, **k: None)
verbose = (lambda *p, **k: _verbose(*p, **k))
def run_script(path, args=[]):
    vars = {}
    args.insert(0, path)
    for (i, arg) in enumerate(args):
        vars['arg%i'%i] = arg
    vars['argcount'] = len(args)
    file = open(path)
    tkn = TokenGet()
    prs = Parse(tkn, vars)
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