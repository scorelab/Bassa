import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "bassa",
    version = "0.0.1",
    author = "SCoRe Community",
    author_email = "community@scorelab.org",
    description = ("Automated Download Queue for Enterprise to take the best use of Internet bandwidth"),
    license = "GPL",
    keywords = "bassa download queue",
    url = "https://github.com/scorelab/Bassa",
    packages=['tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
	"Framework :: Flask"
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    entry_points={
        'console_scripts': [
            'bassa = Main:main'
        ]
    },
    namespace_packages = ['bassa']
)
