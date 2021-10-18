import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setGeometry(450, 300, 360, 350)
        self.setWindowTitle("Pongpol Calculator")
        self.function()
        self.show()
       
    def function(self):
        self.label = QLabel(self)
        self.label.setGeometry(6, 4, 350, 70)   
        self.label.setStyleSheet("QLabel")
        self.label.setStyleSheet("border : 2px solid red")
                                 
        bp = QPushButton(".", self)
        bp.setGeometry(6, 300, 80, 40)
        b0 = QPushButton("0", self)
        b0.setGeometry(95, 300, 80, 40)
        be = QPushButton("=", self)
        be.setGeometry(185, 300, 80, 40)
        b7 = QPushButton("7", self)
        b7.setGeometry(6, 250, 80, 40)
        b8 = QPushButton("8", self)
        b8.setGeometry(95, 250, 80, 40)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())