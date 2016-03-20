import os
from setuptools import setup
from pip.req import parse_requirements

# Utility function to read the README file.
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
requirements_path = os.path.join(base_dir, 'requirements.txt')

install_reqs = parse_requirements(requirements_path, session=False)

requirements = [str(ir.req) for ir in install_reqs]

setup(
    name="bassa",
    version="0.0.1",
    author="SCoRe Community",
    author_email="community@scorelab.org",
    description="Automated Download Queue for Enterprise to take the best use of Internet bandwidth",
    license="GPL",
    keywords="bassa download queue",
    url="https://github.com/scorelab/Bassa",
    packages=['tests'],
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
