"""
:module: settings.py
:description: Base settings

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 19/11/16
"""
from __future__ import unicode_literals
from data.database import Settings, session

__author__ = 'arthur'

ses = session()


VERSION = '1.0.0'
RELEASE_DATE = '2016-11-19'
SUPPORTED_PLATFORMS = [
    'All',
    'Nintendo Entertainment System (NES)',
    'Super Nintendo Entertainment System (SNES)',
    'Sega Master System',
    'Sega Megadrive/Genesis',
    'PlayStation',
]
try:
    USER_IP = ses.query(Settings).first().local_ip
except AttributeError:
    USER_IP = '192.168.0.1'
