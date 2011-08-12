from PyQt4 import QtCore, QtGui

import ui_client_hall

class client_hall(QtGui.QWidget):
  def __init__(self,parent=None):
    QtGui.QWidget.__init__(self,parent)
    ui = ui_client_hall.Ui_Form()
    ui.setupUi(self)

