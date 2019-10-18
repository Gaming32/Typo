import os
import getpass, hashlib

def install(settings):
    print('='*20)
    username = input('New user name: ')
    password = getpass.getpass('%s\'s Password: ' % username)
    print('Setting up...')
    settings['users'][username] = {}; print('=', end='')
    settings['users'][username]['password'] = hashlib.sha256(password.encode()).hexdigest(); print('=', end='')
    settings['users'][username]['permission_level'] = 2; print('=', end='')
    os.mkdir('users'); print('=', end='')
    home = os.path.join('users', username); print('=', end='')
    os.mkdir(home); print('=', end='')
    os.chdir(home); print('=', end='')
    print('Done.')
    return username