#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
sys.path.append( 'gui/');
sys.path.append('../client-build-desktop');
import MainWindow

app = QtGui.QApplication(sys.argv)
win = MainWindow.MainWindow()
win . show()
sys.exit(app.exec_())
