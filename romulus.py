"""
Romulus.
A manager for easy downloading of ROMs for your Retropie.

Author: Arthur Moore <arthur.moore85@gmail.com>
Date: 2016-11-19
License: GPLv2
"""
from __future__ import unicode_literals
from threading import Thread
from PyQt4 import QtGui
from PyQt4.QtCore import *
import time
from data.initial_declaration import InitialData
from data.settings import SUPPORTED_PLATFORMS
from io_utils.directory_utils import Directories
from sync.remote import Sync, GAMES_CLEAN
from ui.pi_controller import PiWindow
from scraping.scraper import Scraper
from ui.mainWindow import Ui_MainWindow
from data.database import *
from ui.settings_controller import SettingsWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    search_signal = pyqtSignal(str)

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
        self.games_dict = GAMES_CLEAN

        # Triggers
        self.actionQuit.triggered.connect(self._quit_romulus)
        self.actionSettings.triggered.connect(self._settings)
        self.btnSearch.clicked.connect(self.search_thread)
        self.search_signal.connect(self.set_status)
        self.tableSearchResults.cellClicked.connect(self.selected_rom)
        self.btnDownloadSelected.clicked.connect(self.download_rom)
        self.actionSync_Library.triggered.connect(self._sync)

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
        self.search = Scraper(rom)
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

    def _sync(self):
        """
        Initialize Pi Control Centre window
        """
        if self.sync_window is None:
            if self.sync_obj is None:
                self.sync_obj = Sync(self.retro_settings)
            self.sync_window = PiWindow(self.sync_obj, self.games_dict)
        self.sync_window.show()

    def _set_defaults(self):
        """
        Set default visuals
        """
        search_headers = ['Title']
        download_headers = ['Title', 'Status']
        self.tableSearchResults.setColumnCount(1)
        self.tableDownloadProgress.setColumnCount(2)
        self.tableSearchResults.setHorizontalHeaderLabels(search_headers)
        self.tableDownloadProgress.setHorizontalHeaderLabels(download_headers)
        search_header = self.tableSearchResults.horizontalHeader()
        download_header = self.tableDownloadProgress.horizontalHeader()
        search_header.setStretchLastSection(True)
        download_header.setStretchLastSection(True)
        self.comboPlatformSearch.addItems(SUPPORTED_PLATFORMS)
        self.btnDownloadSelected.setEnabled(False)


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
