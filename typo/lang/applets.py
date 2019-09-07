try:
    from .__init__ import *
    del run_script
    from .__init__ import run_script as _run_script
except ImportError:
    from typo.lang import *
    del run_script
    from typo.lang import run_script as _run_script

def run_script(path, scriptargs=[], isverbose=False):
    set_verbose(isverbose)
    set_excepthook()
    # try: set_excepthook()
    # except NameError:
    #     from ._core import *
    #     set_excepthook()
    _run_script(path, scriptargs)

def interactive_session():
    pass