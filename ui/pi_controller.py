from PyQt4 import QtGui
from PyQt4.QtGui import QHeaderView

from piWindow import Ui_PiWindow


class PiWindow(QtGui.QMainWindow, Ui_PiWindow):
    def __init__(self, sync_obj, games_dict, parent=None):
        """
        Some comment here
        """
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.games_dict = games_dict
        self.sync_obj = sync_obj
        if not self.sync_obj.status:
            self.lblPiStatus.setText('<h2>{0}</h2>'.format(self.sync_obj.status_message))
        self.games = self.sync_obj.remote_library
        self.comboFilter.addItem('All')
        self.comboFilter.addItems(self.games.keys())
        self._default_settings()

    def _default_settings(self):
        """
        Sets default settings
        """
        pi_headers = ['Title', 'Platform']
        self.tableLibrary.setColumnCount(2)
        self.tableLibrary.setHorizontalHeaderLabels(pi_headers)
        pi_header = self.tableLibrary.horizontalHeader()
        results = 0
        for k, v in self.games.iteritems():
            for x in v:
                results += 1
        self.tableLibrary.setRowCount(results)
        pi_header.setStretchLastSection(False)
        pi_header.setResizeMode(0, QHeaderView.Stretch)
        row = 0
        for platform, games in self.games.iteritems():
            for game in games:
                self.tableLibrary.setItem(row, 0, QtGui.QTableWidgetItem(game))
                self.tableLibrary.setItem(row, 1, QtGui.QTableWidgetItem(platform))
                row += 1
