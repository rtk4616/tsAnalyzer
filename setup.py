__author__ = 'Angel'

from distutils.core import setup
from setuptools import find_packages

__name__ = 'tsAnalyzer'
__version__ ='0.0.2'

setup(
    name = __name__,
    version = __version__,
    description='A transport stream analyzer',
    author='Angel Campo',
    author_email='nagel81@gmail.com',
    packages=find_packages(),
    options = {'py2exe': {
                            "packages" : ["src", "src.model"],
                            "bundle_files" :  "1",
                            "optimize" : "1",
                            "excludes": ["test", "test.model", "test.data"],
                            "dll_excludes" :"w9xpopen.exe"
                        }},
    console =[{
                "script": "./src/main.py",
                "dest_base" : "tsAnalyzer-" + __version__
              }],
    zipfile = None
    )