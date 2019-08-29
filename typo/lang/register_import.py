funcs = {}
vars = {}
def register(name, func, minargcount, maxargcount=None, *defaults):
    funcs[name] = dict(
        func=func,
        minargcount=minargcount,
        maxargcount=maxargcount,
        defaults=defaults
    )
def register_var(name, value):
    vars[name] = value