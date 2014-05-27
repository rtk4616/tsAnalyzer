__author__ = 'Angel'

from distutils.core import setup
import py2exe

ApplicationName = 'tsAnalyzer'
ApplicationVersion ='0.0.1'

setup(
    name = ApplicationName,
    version = ApplicationVersion,
    description='A transport stream analyzer',
    author='Angel Campo',
    author_email='nagel81@gmail.com',
    packages=['src'],
    options = {'py2exe': {
                            "packages" : "src",
                            "bundle_files" :  "1",
                            "optimize" : "1",
                            "dll_excludes" :"w9xpopen.exe"
                        }},
    console =[{
                "script": "./src/main.py",
                "dest_base" : "tsAnalyzer-" + ApplicationVersion
              }],
    zipfile = None
    )