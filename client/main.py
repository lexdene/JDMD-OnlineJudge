#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui
sys.path.append( 'gui/');
sys.path.append('../client-build-desktop');
import client_hall
import show_problem

app = QtGui.QApplication(sys.argv)
widget = client_hall.client_hall()
widget.show()
widget1 = show_problem.show_problem()
widget1.show();
sys.exit(app.exec_())
