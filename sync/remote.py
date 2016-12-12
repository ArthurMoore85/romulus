"""
Sync module
"""
import os
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException

GAMES_CLEAN = {
    'amstradpc': 'Amstrad',
    'arcade': 'Arcade',
    'atari2600': 'Atari 2600',
    'atari7800': 'Atari 7800',
    'atarilynx': 'Atari Lynx',
    'fba': 'FireBurn Alpha',
    'fds': 'Famicom Disk System',
    'gamegear': 'GameGear',
    'gb': 'GameBoy',
    'gba': 'GameBoy Advance',
    'gbc': 'GameBoy Color',
    'genesis': 'Sega Genesis (USA)',
    'mame-libretro': 'Mame (libretro)',
    'mame-mame4all': 'Mame (mame4all)',
    'mastersystem': 'Sega Master System',
    'megadrive': 'Sega Mega Drive (EU)',
    'msx': 'MSX',
    'n64': 'Nintendo 64',
    'neogeo': 'Neo Geo',
    'nes': 'Nintendo Entertainment System',
    'ngp': 'Neo Geo Pocket',
    'ngpc': 'Neo Geo Pocket Color',
    'pcengine': 'PC Engine',
    'psp': 'Playstation Portable (PSP)',
    'psx': 'Playstation',
    'sega32x': 'Sega 32X',
    'segacd': 'Sega CD',
    'sg-1000': 'SG 1000',
    'snes': 'Super Nintendo (SNES)',
    'vectrex': 'Vectrex',
    'zxspectrum': 'ZX Spectrum'
}


class Sync(object):
    """
    Syncs with the Raspberry Pi
    """
    def __init__(self, pi_settings):
        self.ip = pi_settings.last_known_ip
        self.username = pi_settings.username
        self.password = pi_settings.password
        self.status = False
        self.sftp = None
        self.sftp_open = False

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.ssh.connect(
                self.ip,
                username=self.username,
                password=self.password
            )
            self.status = True
        except NoValidConnectionsError:
            self.status = False
            self.status_message = 'Could not connect to Retropie'
        except AuthenticationException:
            self.status = False
            self.status_message = 'Incorrect username/password for Retropie'

    @property
    def remote_library(self):
        """
        Returns the remote library of games
        """
        library = {}
        stdin, stdout, stderr = self.ssh.exec_command('ls RetroPie/roms')
        all_directories = stdout.readlines()
        for directory in all_directories:
            stdin, stdout, stderr = self.ssh.exec_command('ls RetroPie/roms/{0}'.format(directory))
            files = stdout.readlines()
            if files:
                directory = directory.rstrip()
                library[GAMES_CLEAN[directory]] = files
        return library

    def transfer(self, local_dir, games_dict):
        """
        Transfers local roms to Retropie
        """
        base_pi_dir = '/home/pi/RetroPie/roms'
        all_games = games_dict
        transport = paramiko.Transport((self.ip, 22))
        transport.connect(username=self.username, password=self.password)
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(transport)
            self.sftp_open = True
        for k, v in all_games.iteritems():
            sys_dir = GAMES_CLEAN.keys()[GAMES_CLEAN.values().index(k)]
            for rom in v:
                tmp_remote = '{0}/{1}/{2}'.format(base_pi_dir, sys_dir, rom)
                tmp_local = os.path.join(local_dir, sys_dir, rom)
                self.sftp.put(tmp_local, tmp_remote)
        self.close_connection()
        transport.close()

    def close_connection(self):
        """
        Closes transfer
        """
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
