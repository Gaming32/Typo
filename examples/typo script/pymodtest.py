from typo.lang import register_import
def something():
    print('To be or not to be...')
    return '...that is the question'
def withargs(*args):
    print(*args)
    print('vars are', register_import.vars)
    print('funcs are', register_import.funcs)
register_import.register('somefunc', something, 0)
register_import.register('print', withargs, 0, 1000)
register_import.register_var('name', 'value')