import sys
from PyQt4 import QtCore, QtGui
sys.path.append( 'gui/');
import client_hall

app = QtGui.QApplication(sys.argv)
widget = client_hall.client_hall()
widget.show()
sys.exit(app.exec_())
