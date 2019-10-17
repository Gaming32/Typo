import zipfile, json
try:
    from ._core import *
except ImportError:
    from typo.emulator._core import *

def install():
    os.makedirs(EMULATOR_ROOT)
    settings = {
        'installed': False
    }
    fsroot = os.path.join(EMULATOR_ROOT, 'fsroot')
    os.mkdir(fsroot)
    zipfile.ZipFile('typo/emulator/data/fs.zip', 'r', zipfile.ZIP_DEFLATED).extractall(fsroot)
    os.mkdir(os.path.join(fsroot, 'users'))
    settings['installed'] = True
    json.dump(settings, open(os.path.join(EMULATOR_ROOT, 'settings.json'), 'w'))

if __name__ == '__main__': install()