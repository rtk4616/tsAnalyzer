tsAnalyzer
==========

A transport stream analyzer that currently outputs the transport stream id of a transport stream recording

Requirements
------------

python (2.7):

        https://www.python.org/downloads/

Tests
-----

    nosetests --with-coverage --cover-package=.

Run
---
    python -m src.main



Release process
---------------

Windows
-------

Using py2exe:

    python setup.py py2exe

