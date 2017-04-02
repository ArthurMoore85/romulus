"""
:module: initial_declaration.py
:description: Creates initial database entries

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 19/11/16
"""
from __future__ import unicode_literals
import os
import datetime
from data.database import Settings, session, Product, RetropieSettings
from data.settings import VERSION, RELEASE_DATE
from network.discovery import PiDiscovery
from network.network_utils import get_local_ip

__author__ = 'arthur'


def product_settings():
    """
    Declares product details
    """
    version = VERSION.split('.')
    release_date = datetime.datetime.strptime(RELEASE_DATE, '%Y-%m-%d')
    _product = Product(
        version_major=version[0],
        version_minor=version[1],
        version_patch=version[2],
        release_date=release_date
    )
    return _product


def retropie_settings():
    """
    Declares default retropie settings
    """
    rasp = PiDiscovery()
    ip = rasp.rapberry_ip
    username, password = 'pi', 'raspberry'
    _retropie = RetropieSettings(
        last_known_ip=ip,
        username=username,
        password=password
    )
    return _retropie


class InitialData(object):
    """
    Creates initial data
    """
    def __init__(self):
        settings = session()
        self.user_dir = os.path.expanduser('~')
        self.download_loc = os.path.join(self.user_dir, 'romulus', 'downloads')
        ser_loc = os.path.join(os.getcwd(), 'services')
        services = [
            name.capitalize() for name in os.listdir(
                ser_loc) if os.path.isdir(
                os.path.join(ser_loc, name))
            ][0].lower()
        self.default_service = os.path.join(ser_loc, services)
        setting = Settings(
            download_location=self.download_loc,
            selected_service=self.default_service,
            local_ip=get_local_ip(),
            theme='light'
        )
        settings.add(setting)
        settings.add(product_settings())
        settings.add(retropie_settings())
        settings.commit()
