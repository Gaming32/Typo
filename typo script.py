# try: import typo.lang.__main__
# except Exception:
import sys, os, subprocess
if '-v' in sys.argv:
    verbose = print
else:
    verbose = (lambda *p, **k: None)

# verbose('execute fallback required')
path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'typo/lang/__main__.py'))
verbose('typo path is', path)
verbose('executable path is', sys.executable)
ret = subprocess.call([sys.executable, path] + sys.argv[1:])
verbose('return code was', ret)
# ret = os.system('"%s" "%s" "%s"' % (sys.executable, path, '" "'.join(sys.argv[1:])))
#if ret: print('An error occured internally.')
sys.exit(ret)