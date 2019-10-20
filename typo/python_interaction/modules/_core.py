import os
from ...emulator._core import EMULATOR_ROOT
fsroot = os.path.joint(EMULATOR_ROOT, 'fsroot')

def init(fsroot_):
    global fsroot
    fsroot = fsroot_