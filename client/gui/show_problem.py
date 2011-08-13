from PyQt4 import QtCore, QtGui

import ui_show_problem

class show_problem(QtGui.QWidget):
  def __init__(self,parent=None):
    QtGui.QWidget.__init__(self,parent)
    ui = ui_show_problem.Ui_show_problem()
    ui.setupUi(self)

