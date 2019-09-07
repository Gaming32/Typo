import sys, os
try:
    from .__init__ import *
    del run_script
    from .__init__ import run_script as _run_script
    from . import register_import
except ImportError:
    from typo.lang import *
    del run_script
    from typo.lang import run_script as _run_script
    from typo.lang import register_import

def run_script(path, scriptargs=[], isverbose=False):
    set_verbose(isverbose)
    set_excepthook()
    # try: set_excepthook()
    # except NameError:
    #     from ._core import *
    #     set_excepthook()
    _run_script(path, scriptargs)

def interactive_session(isverbose=False):
    set_verbose(isverbose)
    tkn = TokenGet(outsidevarref=True)
    prs = Parse(tkn)
    register_import.quitted = False
    prs.run('importfile', os.path.join(os.path.dirname(__file__), '_quits.py'))
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
        except:
            print_error(*sys.exc_info())