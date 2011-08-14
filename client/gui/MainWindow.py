from PyQt4 import QtCore, QtGui

import ui_MainWindow
import client_hall
import show_problem

class MainWindow(QtGui.QMainWindow):
  def __init__(self,parent=None):
    QtGui.QWidget.__init__(self,parent)
    self.ui = ui_MainWindow.Ui_MainWindow()
    self.ui.setupUi(self)
    self.toolBar=self.addToolBar('sheet')
    self.toolBar.addAction(self.ui.action_Home_page)
    self.toolBar.addAction(self.ui.action_Show_problem)
    self.stackedLayout=QtGui.QStackedLayout(self.ui.centralwidget)
    self.page_client_hall=client_hall.client_hall()
    self.page_show_problem=show_problem.show_problem()
    self.stackedLayout.addWidget(self.page_client_hall)
    self.stackedLayout.addWidget(self.page_show_problem)
    self.ui.centralwidget.setLayout(self.stackedLayout)
    self.signalMapper=QtCore.QSignalMapper(self)
    self.signalMapper.setMapping( self.ui.action_Home_page,0 )
    self.signalMapper.setMapping( self.ui.action_Show_problem, 1 )
    self.ui.action_Home_page.triggered.connect( self.signalMapper.map )
    self.ui.action_Show_problem.triggered.connect( self.signalMapper.map )
    self.signalMapper.mapped.connect(self.stackedLayout.setCurrentIndex)

