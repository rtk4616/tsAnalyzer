__author__ = 'Angel'

from distutils.core import setup
from setuptools import find_packages
from glob import glob
import py2exe

__name__ = 'tsAnalyzer'
__version__ ='0.0.1'

setup(
    name = __name__,
    version = __version__,
    description='A transport stream analyzer',
    author='Angel Campo',
    author_email='nagel81@gmail.com',
    packages=find_packages(),
    options = {'py2exe': {
                            "packages" : ["src"],
                            "bundle_files" :  "1",
                            "optimize" : "1",
                            "dll_excludes" :"w9xpopen.exe"
                        }},
    console =[{
                "script": "./src/main.py",
                "dest_base" : "tsAnalyzer-" + __version__
              }],
    zipfile = None
    )