"""
Romulus.
A manager for easy downloading of ROMs for your Retropie.

Author: Arthur Moore <arthur.moore85@gmail.com>
Date: 2016-11-19
License: GPLv2
"""
from __future__ import unicode_literals
import os
from threading import Thread
from PyQt4 import QtGui
from PyQt4.QtCore import *
import time
from PyQt4.QtGui import QHeaderView
from data.initial_declaration import InitialData
from io_utils.directory_utils import Directories
from sync.remote import Sync, GAMES_CLEAN
from ui.pi_controller import PiWindow
from scraping.scraper import Scraper
from ui.mainWindow import Ui_MainWindow
from data.database import *
from ui.settings_controller import SettingsWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    search_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Main window controller
        """
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.session = session()
        if self.session.query(Settings).count() <= 0:
            InitialData()
        self.search = None
        self.settings_obj = self.session.query(Settings).first()
        self.product_obj = self.session.query(Product).first()
        self._set_defaults()
        self.live_url = None
        self.dirs_obj = Directories()
        self.settings_window = None
        self.sync_window = None
        self.results = None
        self.rasp_ip = self.session.query(RetropieSettings).first().last_known_ip
        self.retro_settings = self.session.query(RetropieSettings).first()
        self.sync_obj = None
        self.local_library = None
        self.games_dict = GAMES_CLEAN

        # Triggers
        self.actionQuit.triggered.connect(self._quit_romulus)
        self.actionSettings.triggered.connect(self._settings)
        self.btnSearch.clicked.connect(self.search_thread)
        self.search_signal.connect(self.set_status)
        self.status_signal.connect(self.set_status)
        self.tableSearchResults.cellClicked.connect(self.selected_rom)
        self.btnDownloadSelected.clicked.connect(self._download_thread)
        self.actionSync_Library.triggered.connect(self._pi_window)
        self.comboLocalFilter.activated.connect(self.filter_local_library)

    def _download_thread(self):
        """
        Starts a thread for the download
        """
        th = Thread(target=self.download_rom)
        th.setDaemon(True)
        th.start()

    def download_rom(self):
        """
        Downloads selected ROM
        """
        url = self.live_url
        platform = " ".join(url.split('/')[-3].replace('_', ' ').split()[:-1])
        target = self.dirs_obj.target_directory(self.settings_obj.download_location, platform)
        self.search.download(url, target)

    def selected_rom(self):
        """
        Fetches selected ROM details
        """
        row_selected = self.tableSearchResults.currentRow()
        rom = self.results[row_selected]
        result = self.search.get_link(rom)
        self.live_url = result
        description = self.search.get_description(result)
        self.lblSearchDescriptionSelected.setText(description)
        self.btnDownloadSelected.setEnabled(True)

    def fetch_local_collection(self):
        """
        Returns local games collection as a dictionary
        """
        games_loc = self.settings_obj.download_location
        library = {}
        if not os.path.exists(games_loc):
            os.makedirs(games_loc)
        dirs = [dirs for root, dirs, files in os.walk(games_loc)][0]
        for rom in dirs:
            library[GAMES_CLEAN[rom]] = [games for root, dirs, games in os.walk(os.path.join(games_loc, rom))][0]
        return library

    def set_status(self, text):
        """
        Sets status due to signal
        """
        status = '<h2>Status: {0}</h2>'.format(text)
        self.lblStatus.setText(status)

    def search_thread(self):
        """
        Sets a search thread
        """
        self.lblStatus.setText('<h2>Status: Searching...</h2>')
        th = Thread(target=self.search_rom)
        th.setDaemon(True)
        th.start()

    def search_rom(self):
        """
        Searches for the entered ROM
        """
        rom = str(self.editSearchTitle.text())
        self.search = Scraper(rom, parent=self)
        result = self.search.fill_in_form()
        self.set_results(result)
        self.search_signal.emit('Completed')
        time.sleep(3)
        self.search_signal.emit('Idle')

    def set_results(self, results):
        """
        Sets the results from a search query
        """
        self.tableSearchResults.clear()
        search_headers = ['Title']
        self.tableSearchResults.setColumnCount(1)
        self.tableSearchResults.setHorizontalHeaderLabels(search_headers)
        self.tableSearchResults.setRowCount(len(results))
        self.results = results
        row = 0
        for item in results:
            self.tableSearchResults.setItem(row, 0, QtGui.QTableWidgetItem(item.text))
            row += 1

    def _quit_romulus(self):
        """
        Closes Romulus
        """
        self.close()

    def _settings(self):
        """
        Initialize Settings window
        """
        if self.settings_window is None:
            self.settings_window = SettingsWindow(self.rasp_ip)
        self.settings_window.show()

    def _pi_window(self):
        """
        Starts Pi Controller in separate thread
        """
        self.set_status('Connecting to Retropie')
        self._sync()

    def _sync(self):
        """
        Initialize Pi Control Centre window
        """
        self.status_signal.emit('Connecting to Retropie')
        if self.sync_window is None:
            if self.sync_obj is None:
                self.sync_obj = Sync(self.retro_settings)
            self.sync_window = PiWindow(self.sync_obj, self.settings_obj, self.games_dict)
        self.status_signal.emit('Idle')
        self.sync_window.show()

    def _set_defaults(self):
        """
        Set default visuals
        """
        search_headers = ['Title']

        self.tableSearchResults.setColumnCount(1)
        self.tableSearchResults.setHorizontalHeaderLabels(search_headers)
        search_header = self.tableSearchResults.horizontalHeader()
        search_header.setStretchLastSection(True)
        self.btnDownloadSelected.setEnabled(False)
        self._set_default_local()

    def _set_default_local(self):
        local_headers = ['Title', 'Platform']
        library = self.fetch_local_collection()
        total_rows = 0
        for platform, roms in library.iteritems():
            total_rows += len(roms)
        self.tableLocalCollection.clear()
        local_header = self.tableLocalCollection.horizontalHeader()
        self.tableLocalCollection.setColumnCount(2)
        self.tableLocalCollection.setRowCount(total_rows)
        local_header.setStretchLastSection(True)
        local_header.setResizeMode(0, QHeaderView.Stretch)
        self.tableLocalCollection.setHorizontalHeaderLabels(local_headers)
        row = 0
        local_platforms = []
        for platform, roms in library.iteritems():
            local_platforms.append(platform)
            for rom in roms:
                self.tableLocalCollection.setItem(row, 0, QtGui.QTableWidgetItem(rom))
                self.tableLocalCollection.setItem(row, 1, QtGui.QTableWidgetItem(platform))
                row += 1
        self.comboLocalFilter.clear()
        self.comboLocalFilter.addItem('All')
        self.comboLocalFilter.addItems(local_platforms)

    def filter_local_library(self):
        """
        Sets a filtered list of local ROMS
        """
        selected = str(self.comboLocalFilter.currentText())
        if selected != 'All':
            local_headers = ['Title', 'Platform']
            library = self.fetch_local_collection()
            filtered_roms = library[selected]
            total_rows = len(filtered_roms)
            local_header = self.tableLocalCollection.horizontalHeader()
            self.tableLocalCollection.clear()
            self.tableLocalCollection.setColumnCount(2)
            self.tableLocalCollection.setRowCount(total_rows)
            local_header.setStretchLastSection(True)
            local_header.setResizeMode(0, QHeaderView.Stretch)
            self.tableLocalCollection.setHorizontalHeaderLabels(local_headers)
            row = 0
            for rom in filtered_roms:
                self.tableLocalCollection.setItem(row, 0, QtGui.QTableWidgetItem(rom))
                self.tableLocalCollection.setItem(row, 1, QtGui.QTableWidgetItem(selected))
                row += 1
        else:
            self._set_default_local()

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
