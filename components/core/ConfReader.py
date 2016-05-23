import os
import inspect
import json

def conf_reader(confFile):
    f = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + confFile)
    txt = ""
    for line in f:
        txt += line.strip()
    return json.loads(txt)
