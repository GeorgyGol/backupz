#from distutils.core import setup
from setuptools import setup, find_packages
import cmdl_backpz
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='backupz',
    version=cmdl_backpz.__version__,
    packages=['cmdl_backpz',],
    scripts=['cmdl_backpz/backupz.py',],
    entry_points={'console_scripts': ['backupz = cmdl_backpz.backupz:main']},
    url='',
    license='',
    author='G. Golyshev',
    author_email='g.golyshev@gmail.com',
    description='backup, full or inc, and copy work',
    #long_description=read('README'),
    # install_requires=[
    #     're >= 2.2', 'pandas >= 0.22.0', 'argparse >=1.1', 'numpy>=1.1', 'python_dateutil>=2.5'
    # ],
    # python_requires='>=3.3'
)
