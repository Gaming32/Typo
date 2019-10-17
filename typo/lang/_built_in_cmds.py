from typo.lang import register_import
def _call_typo_func(*cmd): pass

# def do_checkstate(): pass
def do_explodelist(iterable, name):
    _call_typo_func('assignment', '%scount'%name, len(iterable))
    for (i, item) in enumerate(iterable):
        _call_typo_func('assignment', '%s%i'%(name, i), item)
def do_explodedict(dictionary, name):
    _call_typo_func('assignment', '%scount'%name, len(dictionary))
    for (i, item) in dictionary.items():
        _call_typo_func('assignment', '%s %s'%(name, i), item)
def do_openfile(name, mode):
    return open(name, mode)
def do_filewrite(file, data, location=None):
    if 'b' in file.mode:
        data = bytes(data)
    if location is not None:
        file.seek(location)
    file.write(data)
def do_fileseek(file, location, from_=0):
    file.seek(location, from_)

register_import.register_func('explodelist', do_explodelist, 2)
register_import.register_func('explodedict', do_explodedict, 2)
register_import.register_func('file open', do_openfile, 1, 2, 'r')