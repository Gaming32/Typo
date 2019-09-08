# try: from ._core import typo_error, verbose
# except ImportError: pass
from ._core import typo_error, verbose
import string
class token_error(typo_error):
    name = 'SyntaxError'
    @staticmethod
    def display(args):
        line = args[1]
        index = args[2]
        string = ''
        string += line
        string += '\n'
        string += ' ' * index
        string += '^'
        return string

class TokenGet:
    def __init__(self, string='', outsidevarref=False):
        self.nextline = False
        self.reset(string)
        self.outsidevarref = outsidevarref
    def reset(self, string):
        string = string.strip()
        self.index = 0
        if not self.nextline:
            self.data = ''
            self.cmd = []

            self.incmd = False
            self.indat = False
            self.invar = 0
            self.instr = False
            self.instresc = False
            self.innum = False
        self.string = string
        self.nextline = False
    def scan(self):
        for (self.index, char) in enumerate(self.string):
            if char == '#':
                if not self.instr:
                    if not self.cmd: self.cmd = [None]
                    verbose('comment reached')
                    return
            elif char == '[' and not self.instr:
                self.incmd = True
                if self.invar == 2:
                    var = self.cmd[1]
                    self.cmd = []
                    self.cmd.append(('varassign', var))
                elif self.outsidevarref:
                    self.cmd.append(('varassign', '__outsidevarref__'))
            elif char == ']' and not self.instr:
                self.incmd = False
                self.cmd.append(self.data)
                self.data = ''
            elif char == '{' and not self.instr:
                self.indat = True
            elif char == '}' and not self.instr:
                if self.invar == 1:
                    self.cmd.append(('varget', self.data))
                    self.invar = 0
                self.indat = False
            elif char == '&' and self.indat and not self.instr:
                if self.invar == 1:
                    self.cmd.append(('varget', self.data))
                    self.invar = 0
                self.data = ''
            elif char == '"' and not self.instresc:
                self.instr = not self.instr
                if not self.instr:
                    self.cmd.append(self.data)
                    self.data = ''
            elif char == '|' and not self.instr:
                self.innum = not self.innum
                if not self.innum:
                    self.cmd.append(('num', self.data))
                    self.data = ''
            elif self.invar == 1 and char == '=' and not self.instr:
                self.invar = 2
                self.cmd.append('assignment')
                self.cmd.append(self.data)
                self.data = ''
            elif char == '\\' and not self.instr:
                self.nextline = True
            elif char in string.printable:
                if self.incmd:
                    self.data += char
                elif self.instr:
                    if char == '\\':
                        if not self.instresc:
                            self.instresc = True
                        else:
                            self.data += char
                            self.instresc = False
                    elif self.instresc:
                        if char == 'n':
                            self.data += '\n'
                            self.instresc = False
                        elif char == '"':
                            self.data += '"'
                            self.instresc = False
                        elif char == 'c':
                            self.nextline = True
                        else:
                            self.data += char
                            self.instresc = False
                    else:
                        self.data += char
                elif self.innum:
                    self.data += char
                else:
                    self.data += char
                    self.invar = 1
            else: raise token_error('unexpected character "%s"'%char, self.string, self.index)
        if (not self.nextline) and (self.incmd or self.indat or
        (self.invar==1 and not self.outsidevarref) or self.instr or
        self.instresc or self.innum):
            raise token_error('line terminated unexpectedly', self.string, self.index)
        elif self.invar==1 and self.outsidevarref:
            # self.cmd.append(('varassign', '__outsidevarref__'))
            self.cmd.extend(['assignment', '__outsidevarref__', ('varget', self.data)])
        return self