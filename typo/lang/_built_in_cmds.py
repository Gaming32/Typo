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

register_import.register_func('explodelist', do_explodelist, 2)
register_import.register_func('explodedict', do_explodedict, 2)