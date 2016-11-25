"""
Sync module
"""
import paramiko


class Sync(object):
    """
    Syncs with the Raspberry Pi
    """
    def __init__(self, pi_settings):
        self.ip = pi_settings.get('ip', None)
        self.username = pi_settings.get('username', None)
        self.password = pi_settings.get('password', None)

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(
            self.ip,
            username=self.username,
            password=self.password
        )

    @property
    def remote_library(self):
        """
        Returns the remote library of games
        """
