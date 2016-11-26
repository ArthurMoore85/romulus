"""
Sync module
"""
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