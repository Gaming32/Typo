import sys
traceback = None
def _excepthook(exctype, value, tb):
    print('temp notification')
    verbose('Python exception was:')
    verbose('\t'+traceback.format_exc().replace('\n', '\n\t'))
def set_excepthook():
    global traceback
    # __import__('pprint').pprint(list(sys.modules))
    import traceback
    sys.excepthook = _excepthook
class typo_error(Exception):
    "Common base class for all Typo Script exceptions"
    name = 'Error'
class unknown_error(typo_error): name = 'UnknownError'
_verbose = (lambda *p, **k: None)
def set_verbose(do_verbose_log):
    global _verbose
    if do_verbose_log:
        _verbose = print
    else:
        _verbose = (lambda *p, **k: None)
verbose = (lambda *p, **k: _verbose(*p, **k))
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