import sys, os
try:
    from .__init__ import *
    del run_script
    from .__init__ import run_script as _run_script
    from . import register_import, _info, _import
except ImportError:
    from typo.lang import *
    del run_script
    from typo.lang import run_script as _run_script
    from typo.lang import register_import, _info, _import

def run_script(path, scriptargs=[], isverbose=False):
    set_verbose(isverbose)
    set_excepthook()
    # try: set_excepthook()
    # except NameError:
    #     from ._core import *
    #     set_excepthook()
    _run_script(path, scriptargs)

def interactive_session(isverbose=False, args=[]):
    set_verbose(isverbose)
    print(_info.get_info_header())
    vars = {}
    for (i, arg) in enumerate(args):
        vars['arg%i'%i] = arg
    vars['argcount'] = len(args)
    tkn = TokenGet(outsidevarref=True)
    prs = Parse(tkn, vars)
    register_import.quitted = False
    # prs.run('importfile', os.path.join(os.path.dirname(__file__), '_quits.py'))
    _import.import_file(prs, os.path.join(os.path.dirname(__file__), '_quits.py'))
    while not register_import.quitted:
        try:
            data = input('>>> ')
            tkn.reset(data)
            tkn.scan()
            while tkn.nextline:
                newdata = input('... ')
                tkn.reset(newdata)
                tkn.scan()
            prs.run()
            if '__outsidevarref__' in prs.vars:
                print(prs.vars['__outsidevarref__'])
                del prs.vars['__outsidevarref__']
        except:
            print_error(*sys.exc_info())