import sys, os
import json

# EMULATOR_ROOT = ...
if sys.platform == 'win32':
    EMULATOR_ROOT = '%APPDATA%\\Gaming32\\Typo'
elif sys.platform == 'darwin':
    EMULATOR_ROOT = '~/Library/Application Support/Gaming32/Typo'
else:
    EMULATOR_ROOT = '~/.typo'

EMULATOR_ROOT = os.path.expandvars(EMULATOR_ROOT)
EMULATOR_ROOT = os.path.expanduser(EMULATOR_ROOT)

def isinstalled():
    fpath = os.path.join(EMULATOR_ROOT, 'settings.py')
    try: fp = open(fpath, 'r')
    except FileNotFoundError:
        return False
    else:
        data = json.load(fp)
        return data['installed']