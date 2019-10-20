import json, hashlib, os
from ..python_interaction.modules import typopath
from ..python_interaction.modules import init
from ..python_interaction.modules._core import _get

environment = {
    'PATH': '::sys/exec/shell|::sys/exec/other|::apps',
    'EXEC_EX': '.sys|.hap'
}
calculated_environment = {}

def calculate_environment():
    for (var, val) in environment.items():
        calculated_environment[var] = val.split(typopath.pathsep)

def shell(user):
    curdir = ''
    while True:
        path = input('%s> ' % curdir)
        calculate_environment()
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
    ex = typopath.splitext(file)[1]
    if not ex:
        for ex in calculated_environment['EXEC_EX']:
            value = run_file(file + ex)
            if value:
                return value
    if ex in calculated_environment['EXEC_EX']:
        if not typopath.isabs(file):
            for folder in calculated_environment['PATH']:
                file = typopath.join(folder, file)
                if os.path.exists(os.path.join(_get('fsroot'), file)):
                    break
        if ex == '.sys':
            return run_sys(file)

def run_sys(file):
    return os.path.splitext(os.path.basename(file))[0]

def main(settings_file='../settings.json'):
    sf = open(settings_file, 'r+')
    _settings = json.load(sf)
    settings = _settings['system']
    while True:
        if not settings['installed']:
            from .install import install
            curuser = install(settings)
            sf.seek(0)
            sf.truncate(0)
            json.dump(_settings, sf)
        else:
            curuser = login_page(settings['users'])
        exit_command = shell(curuser)
        if exit_command == 'logout': continue
        elif exit_command == 'shutdown': break
        elif exit_command == 'reboot': break
    sf.seek(0)
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