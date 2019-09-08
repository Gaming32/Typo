version = '0.8'
import platform, sys
def get_info_header():
    return '''Typo Script version %s running on %s %s (%s)''' % (
        version, platform.system(), platform.release(), sys.platform)