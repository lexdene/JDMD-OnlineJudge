# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_hall.ui'
#
# Created: Fri Aug 12 17:23:54 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lab_most_active_user = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_most_active_user.setObjectName(_fromUtf8("lab_most_active_user"))
        self.gridLayout.addWidget(self.lab_most_active_user, 0, 2, 1, 2)
        self.lab_problem_list = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_problem_list.setObjectName(_fromUtf8("lab_problem_list"))
        self.gridLayout.addWidget(self.lab_problem_list, 0, 0, 1, 1)
        self.listView = QtGui.QListView(self.gridLayoutWidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 2, 0, 5, 1)
        self.lab_sub = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_sub.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lab_sub.setWordWrap(True)
        self.lab_sub.setObjectName(_fromUtf8("lab_sub"))
        self.gridLayout.addWidget(self.lab_sub, 1, 2, 1, 1)
        self.lab_ac = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_ac.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lab_ac.setWordWrap(True)
        self.lab_ac.setObjectName(_fromUtf8("lab_ac"))
        self.gridLayout.addWidget(self.lab_ac, 2, 2, 1, 1)
        self.lab_wa = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_wa.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lab_wa.setWordWrap(True)
        self.lab_wa.setObjectName(_fromUtf8("lab_wa"))
        self.gridLayout.addWidget(self.lab_wa, 3, 2, 1, 1)
        self.lab_pe = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_pe.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lab_pe.setWordWrap(True)
        self.lab_pe.setObjectName(_fromUtf8("lab_pe"))
        self.gridLayout.addWidget(self.lab_pe, 4, 2, 1, 1)
        self.lab_ce = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_ce.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lab_ce.setWordWrap(True)
        self.lab_ce.setObjectName(_fromUtf8("lab_ce"))
        self.gridLayout.addWidget(self.lab_ce, 5, 2, 1, 1)
        self.lab_tle = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_tle.setMaximumSize(QtCore.QSize(75, 16777215))
        self.lab_tle.setWordWrap(True)
        self.lab_tle.setObjectName(_fromUtf8("lab_tle"))
        self.gridLayout.addWidget(self.lab_tle, 6, 2, 1, 1)
        self.listView_ac = QtGui.QListView(self.gridLayoutWidget)
        self.listView_ac.setObjectName(_fromUtf8("listView_ac"))
        self.gridLayout.addWidget(self.listView_ac, 2, 3, 1, 1)
        self.listView_wa = QtGui.QListView(self.gridLayoutWidget)
        self.listView_wa.setObjectName(_fromUtf8("listView_wa"))
        self.gridLayout.addWidget(self.listView_wa, 3, 3, 1, 1)
        self.listView_pe = QtGui.QListView(self.gridLayoutWidget)
        self.listView_pe.setObjectName(_fromUtf8("listView_pe"))
        self.gridLayout.addWidget(self.listView_pe, 4, 3, 1, 1)
        self.listView_ce = QtGui.QListView(self.gridLayoutWidget)
        self.listView_ce.setObjectName(_fromUtf8("listView_ce"))
        self.gridLayout.addWidget(self.listView_ce, 5, 3, 1, 1)
        self.listView_tle = QtGui.QListView(self.gridLayoutWidget)
        self.listView_tle.setObjectName(_fromUtf8("listView_tle"))
        self.gridLayout.addWidget(self.listView_tle, 6, 3, 1, 1)
        self.lab_personal = QtGui.QLabel(self.gridLayoutWidget)
        self.lab_personal.setObjectName(_fromUtf8("lab_personal"))
        self.gridLayout.addWidget(self.lab_personal, 0, 1, 1, 1)
        self.listView_fresh_news = QtGui.QListView(self.gridLayoutWidget)
        self.listView_fresh_news.setMinimumSize(QtCore.QSize(450, 0))
        self.listView_fresh_news.setObjectName(_fromUtf8("listView_fresh_news"))
        self.gridLayout.addWidget(self.listView_fresh_news, 4, 1, 3, 1)
        self.listView_sub = QtGui.QListView(self.gridLayoutWidget)
        self.listView_sub.setObjectName(_fromUtf8("listView_sub"))
        self.gridLayout.addWidget(self.listView_sub, 1, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_most_active_user.setText(QtGui.QApplication.translate("Form", "most active user during last 24 hours", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_problem_list.setText(QtGui.QApplication.translate("Form", "problem list", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_sub.setText(QtGui.QApplication.translate("Form", "Submit", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_ac.setText(QtGui.QApplication.translate("Form", "Accept", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_wa.setText(QtGui.QApplication.translate("Form", "Wrong Answer", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_pe.setText(QtGui.QApplication.translate("Form", "Presentation Error", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_ce.setText(QtGui.QApplication.translate("Form", "Compile Error", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_tle.setText(QtGui.QApplication.translate("Form", "Time Limit Exceeded", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_personal.setText(QtGui.QApplication.translate("Form", "personal infomation", None, QtGui.QApplication.UnicodeUTF8))

