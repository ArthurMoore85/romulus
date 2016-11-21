"""
:module: discovery.py
:description: Discovers Raspberry Pi on a network

:author: Arthur Moore <arthur.moore85@gmail.com>
:date: 19/11/16
"""
from __future__ import unicode_literals
import subprocess
from data.settings import USER_IP
from data.database import session, RetropieSettings

__author__ = 'arthur'


class PiDiscovery(object):
    """
    Class to discover IP of Raspberry Pi connected
    to a network.
    """
    def __init__(self):
        self.session = session()
        IP_RANGE = ".".join(USER_IP.split('.')[:3]) + '.2-255'
        self.cmd = '/usr/bin/pkexec nmap -sP {0}'.format(IP_RANGE)
        self._proc = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE)
        self.ip_table = self._proc.communicate()[0].split('\n')

    @property
    def rapberry_ip(self):
        r_loc = 0
        try:
            for ip in self.ip_table:
                if 'Raspberry' in ip:
                    r = str(self.ip_table[r_loc - 2].split()[-1])
                    return r
                r_loc += 1
        except AttributeError:
            pass

    def set_new_ip(self):
        """
        Sets new IP in database
        """
        r = self.session.query(RetropieSettings).first()
        r.last_know_ip = self.rapberry_ip
        self.session.commit()
