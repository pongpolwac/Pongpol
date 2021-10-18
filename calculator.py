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
        b9 = QPushButton("9", self)
        b9.setGeometry(185, 250, 80, 40)
        b4 = QPushButton("4", self)
        b4.setGeometry(6, 200, 80, 40)
        b5 = QPushButton("5", self)
        b5.setGeometry(95, 200, 80, 40)
        b6 = QPushButton("5", self)
        b6.setGeometry(185, 200, 80, 40)
        b1 = QPushButton("1", self)
        b1.setGeometry(6, 150, 80, 40)
        b2 = QPushButton("2", self)
        b2.setGeometry(95, 150, 80, 40)
        b3 = QPushButton("3", self)
        b3.setGeometry(185, 150, 80, 40)
        bmul = QPushButton("x", self)
        bmul.setGeometry(275, 250, 80, 40)
        bmin = QPushButton("-", self)
        bmin.setGeometry(275, 200, 80, 40)
        bplus = QPushButton("+", self)
        bplus.setGeometry(275, 150, 80, 40)
        pequ = QPushButton("=", self)
        pequ.setGeometry(275, 300, 80, 40)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())