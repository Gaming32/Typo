try:
    from ._core import *
except ImportError:
    from typo.emulator._core import *

def main():
    if not isinstalled():
        from typo.emulator.install import install
        install()
    from typo.system import __main__
    __main__.main()

if __name__ == '__main__': main()