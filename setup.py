from __future__ import unicode_literals
import re
from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='RITSEC Music Server',
    version = get_version('music_server/__init__.py'),
    url = 'https://github.com/emmaunel/RITSEC-Music-Server',
    author = 'Ayobami Emmanuel Adewale',
    author_email='aea8506@g.rit.edu',
    description = 'Mopidy music streaming server for the sec lab',
    packages = find_packages(),
    zip_safe = False,
    include_package_data = True,
    install_requires = [
        'Mopidy >= 1.1.0',
        'setuptools'
    ],

    entry_points={
        'mopidy.ext' : [
            'music_server = music_server:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)