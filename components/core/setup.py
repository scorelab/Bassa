import os
import shutil
import inspect
import platform
from setuptools import setup
import setuptools
try:
    from pip.req import parse_requirements
except ImportError:
    from pip._internal.req import parse_requirements

EMAIL_CONF = 'email.conf'
DL_CONF = 'dl.conf'
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
shutil.copyfile(email_conf_location, configdir + EMAIL_CONF)
shutil.copyfile(dl_conf_location, configdir + DL_CONF)

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
