#! /usr/bin/env python

from distutils.core import setup

setup(
    name = 'ELF-Esteem',
    version = '0.1',    
    packages=['elfesteem'],
    scripts = ['elfcli'],
    # Metadata
    author = 'Philippe BIONDI',
    author_email = 'phil(at)secdev.org',
    description = 'ELF-Esteem: ELF file manipulation library',
    license = 'GPLv2',
    # keywords = '',
    # url = '',
)
