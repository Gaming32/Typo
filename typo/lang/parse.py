import sys, os
try: from .__init__ import typo_error, verbose
except ImportError: pass
from . import __init__
from .token import TokenGet
from ._import import *
import string

class parse_error(typo_error): name = 'CommandError'

def _parse_equation(equ, key):
    equ = equ.replace('^', '**')
    for (name, replace) in key.items():
        equ = equ.replace(name, repr(replace))
    return eval(equ)

class Parse:
    def __init__(self, tokener:TokenGet):
        self.tokener = tokener
        self.assigner = None
        self.cmd = None
        self.args = None
        self.funcs = {}
        self.vars = {}
        self.modsearchlist = import_dirs[:] + [os.path.dirname(sys.argv[1])]

        for (i, arg) in enumerate(sys.argv[1:]):
            self.vars['arg%i'%i] = arg
        self.vars['argcount'] = str(len(sys.argv[1:]))
    def startrun(self):
        if isinstance(self.cmd, tuple) and self.cmd[0] == 'varassign':
            self.assigner = self.cmd[1]
            self.cmd = self.args[0]
            del self.args[0]
        for (i, arg) in enumerate(self.args):
            if isinstance(arg, tuple):
                if arg[0] == 'varget':
                    self.args[i] = self.vars[arg[1]]
                elif arg[0] == 'num':
                    self.args[i] = float(arg[1])
                else: raise parse_error('invalid command directive %s' % arg[0])
    def check_argcount(self, argcount_min, argcount_max=None, *defs):
        if argcount_max is None: argcount_max = argcount_min
        l = len(self.args)
        if l < argcount_min or l > argcount_max: raise parse_error('invalid arg count %i for cmd %s' % (len(self.args), self.cmd))
        else:
            for def_ in defs:
                self.args.append(def_)
    def return_(self, val):
        if self.assigner is not None:
            self.vars[self.assigner] = val
            self.assigner = None
    def run(self):
        verbose('raw command is', self.tokener.cmd)
        try: self.cmd, *self.args = self.tokener.cmd
        except ValueError: return
        verbose('args are', self.args)
        self.startrun()
        verbose('fixed args are', self.args)
        if self.cmd is None: return
        elif self.cmd == 'out':
            self.check_argcount(1)
            sys.stdout.write(str(self.args[0]))
        elif self.cmd == 'in':
            self.check_argcount(0, 1, '')
            val = input(self.args[0])
            self.return_(val)
        elif self.cmd == 'err':
            self.check_argcount(1)
            sys.stderr.write(self.args[0])
        elif self.cmd == 'format':
            val = self.args[0] % tuple(self.args[1:])
            self.return_(val)
        elif self.cmd == 'math':
            key = []
            cur = None
            for (i, var) in enumerate(self.args[1:]):
                if i % 2:
                    key.append((cur, var))
                    cur = None
                else: cur = var
            val = _parse_equation(self.args[0], dict(key))
            self.return_(val)
        elif self.cmd == 'assignment':
            self.check_argcount(2)
            self.vars[self.args[0]] = self.args[1]
        elif self.cmd == 'importfile':
            self.check_argcount(1)
            import_file(self, self.args[0])
        elif self.cmd == 'import': import_(self)
        else:
            if self.cmd in self.funcs:
                func = self.funcs[self.cmd]
                self.check_argcount(func['minargcount'], func['maxargcount'], *func['defaults'])
                register_import.funcs = self.funcs
                register_import.vars = self.vars
                ret = func['func'](*self.args)
                register_import.funcs = {}
                register_import.vars = {}
                if ret is not None: self.return_(ret)
            else: raise parse_error('invalid cmd %s' % self.cmd)

from . import _import
_import.TokenGet = TokenGet
_import.Parse = Parse
_import.parse_error = parse_error