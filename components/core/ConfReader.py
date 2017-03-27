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
    conf = get_conf_reader('main.conf')

    if any(val == '' for val in conf['user'].values()):
        sys.exit("Please set all the values for user in main.conf")
    elif any(val == '' for val in conf['dl'].values()):
        sys.exit("Please set all the values for dl in main.conf")
    elif conf['db']['u_name'] == "":
        sys.exit("Please set the value for db username in main.conf")


def get_conf_reader(confFile):
    f = open(configdir + confFile)

    try:
        txt = ""
        for line in f:
            txt += line.strip()
        return json.loads(txt)
    finally:
        f.close()
