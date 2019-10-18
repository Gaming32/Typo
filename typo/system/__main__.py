import json, hashlib, os
from ..python_interaction.modules import typopath

def shell(user):
    curdir = ''
    while True:
        path = input('%s> ' % curdir)
        value = run_file(path)
        if value is not None: break
    if value == 'shutdown':
        return 'shutdown'
    elif value == 'reboot':
        return 'reboot'
    elif value == 'logout':
        return 'logout'
    return 'logout'

def run_file(file):
    if file.endswith('.sys'):
        return run_sys(file)

def run_sys(file):
    if file.startswith('sys/exec'):
        return os.path.splitext(os.path.basename(file))[0]

def main(settings_file='../settings.json'):
    sf = open(settings_file, 'r+')
    _settings = json.load(sf)
    settings = _settings['system']
    while True:
        if not settings['installed']:
            from .install import install
            curuser = install(settings)
        else:
            curuser = login_page(settings['users'])
        exit_command = shell(curuser)
        if exit_command == 'logout': continue
        elif exit_command == 'shutdown': break
        elif exit_command == 'reboot': break
    sf.truncate(0)
    json.dump(_settings, sf)
    if exit_command == 'reboot':
        return False
    else:
        return True

username_prompt = """
    LOGIN PAGE:

        USERNAME: 
"""[1:-1]
invalid_password_prompt = """
    LOGIN PAGE (INVALID PASSWORD):

        USERNAME: 
"""[1:-1]
password_prompt = """
        PASSWORD: 

"""[1:-1]

def login_page(users):
    print('='*20)
    username = input(username_prompt)
    while True:
        user = users[username]
        password = input(password_prompt)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == user['password']:
            break
        username = input(invalid_password_prompt)
    os.chdir(os.path.join('users', username))
    return username

if __name__ == '__main__': main()