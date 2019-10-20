try:
    from ._core import *
except ImportError:
    from typo.emulator._core import *

def main():
    if not isinstalled():
        from typo.emulator.install import install
        install()
    os.chdir(os.path.join(EMULATOR_ROOT, 'fsroot'))
    from typo.system import __main__
    while not __main__.main():
        os.chdir(os.path.join(EMULATOR_ROOT, 'fsroot'))

if __name__ == '__main__': main()