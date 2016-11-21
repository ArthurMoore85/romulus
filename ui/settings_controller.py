from __future__ import unicode_literals
import os
from PyQt4.QtGui import QLineEdit, QFileDialog
from data.database import Settings, RetropieSettings, session
from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import *
from network.discovery import PiDiscovery
from network.network_utils import is_online_string
from settingsWindow import Ui_settingsWindow


class SettingsWindow(QtGui.QMainWindow, Ui_settingsWindow):
    def __init__(self, ip, parent=None):
        """
        Settings window controller
        """
        self.rasp_ip = ip
        self.session = session()
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.db_settings = self.session.query(Settings).first()
        self.db_pi_settings = self.session.query(RetropieSettings).first()
        self._default_settings()
        self.passworded = True

        self.btnPiViewPassword.clicked.connect(self._view_password)
        self.btnFindRetropie.clicked.connect(self._scan_ip)
        self.btnCancel.clicked.connect(self._close_window)
        self.btnDownloadLocBrowse.clicked.connect(self._download_location_picker)
        self.btnSave.clicked.connect(self._save_settings)

    def _scan_ip(self):
        """
        Discovers new IP
        """
        obj = PiDiscovery()
        obj.set_new_ip()

    def _save_settings(self):
        """
        Saves all the settings and closes the window
        """
        pi_username = str(self.editPiUsername.text())
        pi_password = str(self.editPiPassword.text())
        download_loc = str(self.editDownloadLoc.text())
        service = str(self.comboRomSource.currentText()).lower()
        service = os.path.join(self.service_dirs(), service)
        self.db_settings.download_location = download_loc
        self.db_settings.selected_service = service
        self.db_pi_settings.username = pi_username
        self.db_pi_settings.password = pi_password
        self.session.commit()
        self._close_window()

    def _download_location_picker(self):
        """
        Selects download location using GUI
        """
        loc = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.editDownloadLoc.setText(loc)

    def _close_window(self):
        """
        Closes the settings window
        """
        self.close()

    def _default_settings(self):
        """
        Sets all the defaults
        """
        self.editDownloadLoc.setText(self.db_settings.download_location)
        self.editPiIP.setText(self.db_pi_settings.last_known_ip)
        self.editPiUsername.setText(self.db_pi_settings.username)
        self.editPiPassword.setEchoMode(QLineEdit.Password)
        self.editPiPassword.setText(self.db_pi_settings.password)
        self.editPiPassword.setEnabled(False)
        self.online = is_online_string(self.rasp_ip)
        self.lblPiStatus.setText('<h2>{0}</h2>'.format(self.online))
        self.comboRomSource.addItems(self.available_services())

    def _view_password(self):
        """
        Makes password viewable
        """
        if self.passworded:
            self.editPiPassword.setEchoMode(QLineEdit.Normal)
            self.btnPiViewPassword.setText('Hide Password')
            self.editPiPassword.setEnabled(True)
            self.passworded = False
        else:
            self.editPiPassword.setEchoMode(QLineEdit.Password)
            self.btnPiViewPassword.setText('View/Edit Password')
            self.editPiPassword.setEnabled(False)
            self.passworded = True

    def service_dirs(self):
        """
        Returns the service directory
        """
        return os.path.join(os.getcwd(), 'services')

    def available_services(self):
        """
        Returns a list of all available services
        """
        services_dir = self.service_dirs()
        return [
            name.capitalize() for name in os.listdir(
                services_dir) if os.path.isdir(
                os.path.join(services_dir, name))
            ]
