import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 300, 350, 350)
        self.setWindowTitle("Pongpol Calculator")
        self.function()
        self.show()
       
    def function(self):
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)   
        bp = QPushButton(".", self)
        b0 = QPushButton("0", self)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())