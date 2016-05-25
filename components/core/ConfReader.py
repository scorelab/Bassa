import os
import inspect
import json
import sys

def check_conf_availability():
    """Checks whether the conf files have been properly set. Exits otherwise"""
    dlConf = get_conf_reader('dl.conf')
    emailConf = get_conf_reader('email.conf')

    if any(val == '' for val in dlConf.values()):
        sys.exit("Please set all the values in dl.conf")
    if any(val == '' for val in emailConf.values()):
        sys.exit("Please set all the values in email.conf")


def get_conf_reader(confFile):
    f = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + confFile)

    try:
        txt = ""
        for line in f:
            txt += line.strip()
        return json.loads(txt)
    finally:
        f.close()
