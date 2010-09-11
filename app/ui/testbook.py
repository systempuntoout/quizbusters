import sys 
import time 
from PyQt4 import QtCore, QtGui
from statistics import Ui_Dialog
from app.models import questions

class TestDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
  
        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        print dir(self.ui.listView)
        #self.ui.listView.setText('pippo')
        print questions.get_question(1).description 
        # Connect up the buttons.
        #self.connect(self.ui.okButton, QtCore.SIGNAL("clicked()"), self.bok)
  
    def bok(self):
        print "OK 2 !!!!!!!!"
  
if __name__ == '__main__':
     a = QtGui.QApplication(sys.argv)
     w = TestDialog()    
     w.show()
     sys.exit(a.exec_())
