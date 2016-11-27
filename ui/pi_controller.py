from threading import Thread
from PyQt4 import QtGui
from PyQt4.QtGui import QHeaderView
from PyQt4.QtCore import pyqtSignal

from piWindow import Ui_PiWindow


class PiWindow(QtGui.QMainWindow, Ui_PiWindow):
    status = pyqtSignal()
    status_signal = pyqtSignal(str)

    def __init__(self, sync_obj, settings_obj, games_dict, parent=None):
        """
        Controller for the Pi Control Center window
        """
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

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
        self.sync_obj.transfer(self.settings_obj.download_location)
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
