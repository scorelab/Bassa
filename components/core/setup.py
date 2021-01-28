import os
import shutil
import inspect
import platform
import json
from setuptools import setup
import setuptools
try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements

EMAIL_CONF = 'email.conf'
DL_CONF = 'dl.conf'
DB_CONF = 'db.config.json'
USER_DB_CONF = 'user.db.config.json'

LINUX_CONFDIR = os.path.expanduser('~') + '/.config/bassa/'
WIN_CONFDIR = os.path.expanduser('~') + '/%app_data%/bassa/'
OSX_CONFDIR  = os.path.expanduser('~') + '/.config/bassa/'

# Utility function to read the README file.
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

base_dir = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(base_dir, 'requirements.txt')

install_reqs = parse_requirements(requirements_path, session=False)

try:
    requirements = [str(ir.req) for ir in install_reqs]
except:
    requirements = [str(ir.requirement) for ir in install_reqs]


### Set configs ###
if platform.system() == 'Linux':
    configdir = LINUX_CONFDIR
elif platform.system() == 'Windows':
    configdir = WIN_CONFDIR
elif platform.system() == 'Darwin':
    configdir = OSX_CONFDIR
if not os.path.exists(configdir):
    os.makedirs(configdir)

email_conf_location = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + EMAIL_CONF
dl_conf_location = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + DL_CONF
db_conf_location = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + DB_CONF
user_db_conf_location = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + USER_DB_CONF
shutil.copyfile(email_conf_location, configdir + EMAIL_CONF)
shutil.copyfile(dl_conf_location, configdir + DL_CONF)
shutil.copyfile(db_conf_location, configdir + DB_CONF)
## merge db configs if user config exist
if os.path.exists(user_db_conf_location):
    # userDbConf, defaultDbConf
    with open(user_db_conf_location) as user_db_conf:
        userDbConf = json.load(user_db_conf)
    with open(configdir + DB_CONF) as default_db_conf:
        defaultDbConf = json.load(default_db_conf)
    for key in userDbConf:
        defaultDbConf[key] = userDbConf[key]
    with open(configdir + DB_CONF, 'w') as default_db_conf:
        json.dump(defaultDbConf, default_db_conf, indent=4)

###/ Set configs ###

setup(
    name="bassa",
    version="0.0.1",
    author="SCoRe Community",
    author_email="community@scorelab.org",
    description="Automated Download Queue for Enterprise to take the best use of Internet bandwidth",
    license="GPL",
    keywords="bassa download queue",
    url="https://github.com/scorelab/Bassa",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Framework :: Flask",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    entry_points={
        'console_scripts': [
            'bassa = Main:main'
        ]
    },
)
