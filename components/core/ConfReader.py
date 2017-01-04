import os
import inspect
import json
import sys
import platform


if platform.system() == 'Linux':
    configdir = os.path.expanduser('~') + '/.config/bassa/'
elif platform.system() == 'Windows':
    configdir = os.path.expanduser('~') + '/%app_data%/bassa/'
elif platform.system() == 'Darwin':
    configdir = os.path.expanduser('~') + '/.config/bassa/'


def check_conf_availability():
    """Checks whether the conf files have been properly set. Exits otherwise"""
    dlConf = get_conf_reader('dl.conf')
    emailConf = get_conf_reader('email.conf')

    if any(val == '' for val in dlConf.values()):
        sys.exit("Please set all the values in dl.conf")
    if any(val == '' for val in emailConf.values()):
        sys.exit("Please set all the values in email.conf")


def get_conf_reader(confFile):
    f = open(configdir + confFile)

    try:
        txt = ""
        for line in f:
            txt += line.strip()
        return json.loads(txt)
    finally:
        f.close()
