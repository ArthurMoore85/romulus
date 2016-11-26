# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piWindow.ui'
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

class Ui_PiWindow(object):
    def setupUi(self, PiWindow):
        PiWindow.setObjectName(_fromUtf8("PiWindow"))
        PiWindow.resize(981, 695)
        self.centralwidget = QtGui.QWidget(PiWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnSync = QtGui.QPushButton(self.centralwidget)
        self.btnSync.setGeometry(QtCore.QRect(750, 570, 221, 71))
        self.btnSync.setObjectName(_fromUtf8("btnSync"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 201, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableLibrary = QtGui.QTableWidget(self.centralwidget)
        self.tableLibrary.setGeometry(QtCore.QRect(10, 50, 961, 511))
        self.tableLibrary.setObjectName(_fromUtf8("tableLibrary"))
        self.tableLibrary.setColumnCount(0)
        self.tableLibrary.setRowCount(0)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 570, 731, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lblPiStatus = QtGui.QLabel(self.layoutWidget)
        self.lblPiStatus.setObjectName(_fromUtf8("lblPiStatus"))
        self.horizontalLayout.addWidget(self.lblPiStatus)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(550, 0, 421, 51))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboFilter = QtGui.QComboBox(self.layoutWidget1)
        self.comboFilter.setObjectName(_fromUtf8("comboFilter"))
        self.horizontalLayout_2.addWidget(self.comboFilter)
        PiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuClose = QtGui.QMenu(self.menubar)
        self.menuClose.setObjectName(_fromUtf8("menuClose"))
        PiWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PiWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PiWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuClose.menuAction())

        self.retranslateUi(PiWindow)
        QtCore.QMetaObject.connectSlotsByName(PiWindow)

    def retranslateUi(self, PiWindow):
        PiWindow.setWindowTitle(_translate("PiWindow", "RetroPie Control Centre", None))
        self.btnSync.setText(_translate("PiWindow", "Sync Games Library", None))
        self.label_2.setText(_translate("PiWindow", "<h2>Remote Library</h2>", None))
        self.label.setText(_translate("PiWindow", "<h2>Connection status:</h2>", None))
        self.lblPiStatus.setText(_translate("PiWindow", "<h2>Connected</h2>", None))
        self.label_3.setText(_translate("PiWindow", "<h3>Filter:</h3>", None))
        self.menuClose.setTitle(_translate("PiWindow", "Close", None))

