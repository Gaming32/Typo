from typo.lang import register_import
def doquit():
    register_import.quitted = True
register_import.register_func('exit', doquit, 0)
register_import.register_func('quit', doquit, 0)