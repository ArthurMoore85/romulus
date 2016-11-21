"""
:module: network_utils.py
:description: Utilities for networking

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 19/11/16
"""
from __future__ import unicode_literals
import os
import socket

__author__ = 'arthur'


def get_local_ip():
    """
    Returns current local IP
    :return: User IP (string)
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        user_ip = s.getsockname()[0]
        return user_ip
    except Exception:
        pass
    return ''


def is_online(ip):
    """
    Checks to see if an IP address is online or not
    :return: Boolean
    """
    cmd = 'ping -c 1 {0}'.format(ip)
    response = os.system(cmd)
    if response == 0:
        return True
    else:
        return False


def is_online_string(ip):
    """
    Checks to see if an IP address is online or not
    :return: String
    """
    cmd = 'ping -c 1 {0}'.format(ip)
    response = os.system(cmd)
    if response == 0:
        return "Online"
    else:
        return "Offline"