# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1042, 734)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblStatus = QtGui.QLabel(self.centralwidget)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.gridLayout.addWidget(self.lblStatus, 2, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 991, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tableSearchResults = QtGui.QTableWidget(self.tab)
        self.tableSearchResults.setGeometry(QtCore.QRect(10, 90, 691, 491))
        self.tableSearchResults.setObjectName(_fromUtf8("tableSearchResults"))
        self.tableSearchResults.setColumnCount(0)
        self.tableSearchResults.setRowCount(0)
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(710, 90, 20, 491))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(790, 90, 171, 191))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.imgCoverSearch = QtGui.QLabel(self.frame)
        self.imgCoverSearch.setGeometry(QtCore.QRect(-1, -3, 171, 191))
        self.imgCoverSearch.setText(_fromUtf8(""))
        self.imgCoverSearch.setObjectName(_fromUtf8("imgCoverSearch"))
        self.lblSearchDescriptionSelected = QtGui.QLabel(self.tab)
        self.lblSearchDescriptionSelected.setGeometry(QtCore.QRect(740, 400, 261, 121))
        self.lblSearchDescriptionSelected.setText(_fromUtf8(""))
        self.lblSearchDescriptionSelected.setObjectName(_fromUtf8("lblSearchDescriptionSelected"))
        self.btnDownloadSelected = QtGui.QPushButton(self.tab)
        self.btnDownloadSelected.setGeometry(QtCore.QRect(740, 540, 271, 41))
        self.btnDownloadSelected.setObjectName(_fromUtf8("btnDownloadSelected"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 991, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.editSearchTitle = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editSearchTitle.sizePolicy().hasHeightForWidth())
        self.editSearchTitle.setSizePolicy(sizePolicy)
        self.editSearchTitle.setObjectName(_fromUtf8("editSearchTitle"))
        self.horizontalLayout_3.addWidget(self.editSearchTitle)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboPlatformSearch = QtGui.QComboBox(self.layoutWidget)
        self.comboPlatformSearch.setObjectName(_fromUtf8("comboPlatformSearch"))
        self.horizontalLayout_4.addWidget(self.comboPlatformSearch)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.btnSearch = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy)
        self.btnSearch.setObjectName(_fromUtf8("btnSearch"))
        self.horizontalLayout_5.addWidget(self.btnSearch)
        self.layoutWidget1 = QtGui.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(740, 290, 271, 20))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lblSearchTitleSelected = QtGui.QLabel(self.layoutWidget1)
        self.lblSearchTitleSelected.setText(_fromUtf8(""))
        self.lblSearchTitleSelected.setObjectName(_fromUtf8("lblSearchTitleSelected"))
        self.horizontalLayout_6.addWidget(self.lblSearchTitleSelected)
        self.layoutWidget2 = QtGui.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(740, 320, 271, 20))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lblSearchYearSelected = QtGui.QLabel(self.layoutWidget2)
        self.lblSearchYearSelected.setText(_fromUtf8(""))
        self.lblSearchYearSelected.setObjectName(_fromUtf8("lblSearchYearSelected"))
        self.horizontalLayout_7.addWidget(self.lblSearchYearSelected)
        self.layoutWidget3 = QtGui.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(740, 350, 271, 20))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_6 = QtGui.QLabel(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lblSearchPlatformSelected = QtGui.QLabel(self.layoutWidget3)
        self.lblSearchPlatformSelected.setText(_fromUtf8(""))
        self.lblSearchPlatformSelected.setObjectName(_fromUtf8("lblSearchPlatformSelected"))
        self.horizontalLayout_8.addWidget(self.lblSearchPlatformSelected)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 291, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tableDownloadProgress = QtGui.QTableWidget(self.tab_2)
        self.tableDownloadProgress.setGeometry(QtCore.QRect(10, 60, 1001, 511))
        self.tableDownloadProgress.setObjectName(_fromUtf8("tableDownloadProgress"))
        self.tableDownloadProgress.setColumnCount(0)
        self.tableDownloadProgress.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuRetropie = QtGui.QMenu(self.menubar)
        self.menuRetropie.setObjectName(_fromUtf8("menuRetropie"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSync_Library = QtGui.QAction(MainWindow)
        self.actionSync_Library.setObjectName(_fromUtf8("actionSync_Library"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout_Romulus = QtGui.QAction(MainWindow)
        self.actionAbout_Romulus.setObjectName(_fromUtf8("actionAbout_Romulus"))
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRetropie.addAction(self.actionSync_Library)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout_Romulus)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRetropie.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Romulus", None))
        self.lblStatus.setText(_translate("MainWindow", "<h2>Status: Idle</h2>", None))
        self.label_3.setText(_translate("MainWindow", "<h3>Results:</h3>", None))
        self.btnDownloadSelected.setText(_translate("MainWindow", "Download", None))
        self.label.setText(_translate("MainWindow", "<h3>Title:</h3>", None))
        self.label_2.setText(_translate("MainWindow", "<h3>Platform:</h3>", None))
        self.btnSearch.setText(_translate("MainWindow", "Search", None))
        self.label_4.setText(_translate("MainWindow", "<b>Title:</b>", None))
        self.label_5.setText(_translate("MainWindow", "<b>Year:</b>", None))
        self.label_6.setText(_translate("MainWindow", "<b>Platform:</b>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ROM Search", None))
        self.label_7.setText(_translate("MainWindow", "<h2>Current Download Progress:</h2>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Download Progress", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuRetropie.setTitle(_translate("MainWindow", "Retropie", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionSync_Library.setText(_translate("MainWindow", "Pi Control Center", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAbout_Romulus.setText(_translate("MainWindow", "About Romulus", None))

