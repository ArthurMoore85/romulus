import os
from threading import Thread
from PyQt4 import QtGui
from PyQt4.QtGui import QHeaderView
from PyQt4.QtCore import pyqtSignal
import re

from piWindow import Ui_PiWindow


class PiWindow(QtGui.QMainWindow, Ui_PiWindow):
    status = pyqtSignal()
    status_signal = pyqtSignal(str)

    def __init__(self, sync_obj, settings_obj, games_dict, local_library, parent=None):
        """
        Controller for the Pi Control Center window
        """
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.local_lib = local_library
        self.settings_obj = settings_obj
        self.games_dict = games_dict
        self.sync_obj = sync_obj
        if not self.sync_obj.status:
            self.lblPiStatus.setText('<h2>{0}</h2>'.format(self.sync_obj.status_message))
        self.games = self.sync_obj.remote_library
        self.comboFilter.addItem('All')
        self.pi_header = None
        self.pi_headers = None
        self.comboFilter.addItems(self.games.keys())
        self._default_settings()

        # Triggers
        self.comboFilter.activated.connect(self._filter_results)
        self.btnSync.clicked.connect(self._thread_sync)
        self.status_signal.connect(self.set_status)

    def set_status(self, text):
        """
        Sets a status message
        """
        self.label.setText('<h2>Status:</h2>')
        self.lblPiStatus.setText('<h2>{0}</h2>'.format(text))

    def compare_local_remote(self):
        """
        Compares local and remote libraries.
        This creates a dictionary of games currently available locally but not remotely,
        ready for syncing. This makes sync efficient and non-repetitive.
        """
        to_add = {}
        for system, roms in self.local_lib.iteritems():
            system_games = []
            for game in roms:
                found = 0
                clean_game = self.clean_game_name(game)
                r_system = self.games[system]
                for r_game in r_system:
                    clean_r_game = self.clean_game_name(r_game)
                    if clean_r_game == clean_game:
                        found = 1
                        break
                if found == 0:
                    system_games.append(game)
            if system_games:
                to_add[system] = system_games
        return to_add

    def clean_game_name(self, game):
        """
        Cleans ROM names.
        This removes regions, changes possible dots to spaces, and removes extensions.
        The reason for this is to increase the chances of finding matches and reducing the chance of duplicates
        making their way into the system if they differ in ways upon first glance.
        """
        game = os.path.splitext(game)[0]
        game = game.upper()
        game_region_str = '({0})'.format(self.region_detect(game))
        game = game.replace('.', ' ')
        game = game.replace('[!]', '')
        game = game.replace(game_region_str, '')
        game = game.strip()
        return game

    def region_detect(self, game):
        """
        Detects the region of a particular ROM
        """
        r_detect = None
        regex_str = r"\(([UEJSA)]+)\)"
        region = re.compile(regex_str).findall(game)
        if region:
            region = region[0]
            r_detect = region
        return r_detect

    def _thread_sync(self):
        """
        Runs syncing in a thread
        """
        th = Thread(target=self.sync_roms)
        th.setDaemon(True)
        th.start()

    def _default_settings(self):
        """
        Sets default settings
        """
        self.label.setText('<h2>Pi Status:</h2>')
        self.lblPiStatus.setText('<h2>Idle</h2>')
        self.pi_headers = ['Title', 'Platform']
        self.tableLibrary.setColumnCount(2)
        self.tableLibrary.setHorizontalHeaderLabels(self.pi_headers)
        self.pi_header = self.tableLibrary.horizontalHeader()
        self._default_table()

    def sync_roms(self):
        """
        Transfers local roms to Retropie
        """
        self.status_signal.emit('Syncing with Retropie')
        games = self.compare_local_remote()
        systems = len(games.keys())
        games_len = sum(len(v) for v in games.itervalues())
        self.status_signal.emit('Sending {0} games for {1} systems'.format(games_len, systems))
        self.sync_obj.transfer(self.settings_obj.download_location, games)
        self.status_signal.emit('Complete')

    def _default_table(self):
        """
        Sets default table data
        """
        self.tableLibrary.clear()
        results = 0
        for k, v in self.games.iteritems():
            for x in v:
                results += 1
        self.tableLibrary.setRowCount(results)
        self.pi_header.setStretchLastSection(False)
        self.pi_header.setResizeMode(0, QHeaderView.Stretch)
        self.tableLibrary.setHorizontalHeaderLabels(self.pi_headers)
        row = 0
        for platform, games in self.games.iteritems():
            for game in games:
                self.tableLibrary.setItem(row, 0, QtGui.QTableWidgetItem(game))
                self.tableLibrary.setItem(row, 1, QtGui.QTableWidgetItem(platform))
                row += 1
        self.comboFilter.addItem('All')
        self.comboFilter.addItems(self.games.keys())

    def _filter_results(self):
        """
        Shows only results based on combobox selection
        """
        combo_selection = str(self.comboFilter.currentText())
        if combo_selection == 'All':
            self._default_table()
        else:
            self.pi_header.setStretchLastSection(False)
            self.pi_header.setResizeMode(0, QHeaderView.Stretch)
            self.tableLibrary.setHorizontalHeaderLabels(self.pi_headers)
            results = self.games[combo_selection]
            self.comboFilter.clear()
            self.tableLibrary.setRowCount(len(results))
            row = 0
            for game in results:
                self.tableLibrary.setItem(row, 0, QtGui.QTableWidgetItem(game))
                self.tableLibrary.setItem(row, 1, QtGui.QTableWidgetItem(combo_selection))
                row += 1
        self.comboFilter.addItem('All')
        self.comboFilter.addItems(self.games.keys())
