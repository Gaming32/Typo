import os
from ...emulator._core import EMULATOR_ROOT
fsroot = os.path.join(EMULATOR_ROOT, 'fsroot')

def init(fsroot_):
    global fsroot
    fsroot = fsroot_

def _get(obj):
    return eval(obj)