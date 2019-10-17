import genericpath

curdir = '.'
pardir = '..'
extsep = '.'
sep = '/'
pathsep = '|'
altsep = '\\'
defpath = '.|::bin'

def basename(path):
    """Return a normalized absolutized version of the pathname path. On most platforms, this is equivalent to
calling the function normpath() as follows: normpath(join(os.getcwd(), path))."""
    return split(path)[1]

def dirname(path):
    """Return the base name of pathname path. This is the second element of the pair returned by passing path to
the function split(). Note that the result of this function is different from the Unix basename program;
where basename for '/foo/bar/' returns 'bar', the basename() function returns an empty string ('')."""
    return split(path)[0]

def isabs(path):
    return path.startswith('::') or path.startswith(sep) or path.startswith(altsep)

def join(path, *paths):
    """Join one or more path components intelligently. The return value is the concatenation of path and any
members of *paths with exactly one directory separator (os.sep) following each non-empty part except the
last, meaning that the result will only end in a separator if the last part is empty. If a component is an
absolute path, all previous components are thrown away and joining continues from the absolute path component."""
    res = path
    for sub in paths:
        if isabs(sub): res = sub
        else: res += sep + sub
    return res

def normcase(path):
    return path.replace('\\', '/')

def split(path):
    """Split the pathname path into a pair, (head, tail) where tail is the last pathname component and head is
everything leading up to that. The tail part will never contain a slash; if path ends in a slash, tail will be empty.
If there is no slash in path, head will be empty. If path is empty, both head and tail are empty. Trailing slashes
are stripped from head unless it is the root (one or more slashes only). In all cases, join(head, tail)
returns a path to the same location as path (but the strings may differ). Also see the functions dirname()
and basename()."""
    partway = path.rsplit(sep, 1)
    if len(partway) < 2:
        partway = path.rsplit(altsep, 1)
    return partway

def splitdrive(path):
    """Split the pathname path into a pair (drive, tail) where drive is either a mount point or the empty string.
On systems which do not use drive specifications, drive will always be the empty string. In all cases, drive
+ tail will be the same as path."""
    if ':' in path:
        partway = path.split(':', 2) # ('', drive_name, tail)
        return ':%s:' % partway[1], partway[2]
    elif isabs(path):
        return '::', path[1:]
    else:
        return '', path

def splitext(path):
    """Split the pathname path into a pair (root, ext) such that root + ext == path, and ext is empty or begins
with a period and contains at most one period. Leading periods on the basename are ignored;
splitext('.cshrc') returns ('.cshrc', '')."""
    if basename(path)[0] == '.':
        return path, ''
    else:
        partway = path.rsplit(extsep, 1) # (file_name, ext_name)
        return partway[0], '.' + partway[1]