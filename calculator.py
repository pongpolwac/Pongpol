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
        bp.setGeometry(5, 300, 80, 40)
        b0 = QPushButton("0", self)
        b0.setGeometry(95, 300, 80, 40)
        be = QPushButton("=", self)
        be.setGeometry(185, 300, 80, 40)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())