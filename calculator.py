import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets

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
        self.label.setFont(QFont('Arial', 15))
                                 
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
        b6 = QPushButton("6", self)
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
        bdiv = QPushButton("/", self)
        bdiv.setGeometry(275, 300, 80, 40)
        bcle = QPushButton("C", self)
        bcle.setGeometry(5, 100, 200, 40)
        bdel = QPushButton("Del", self)
        bdel.setGeometry(210, 100, 145, 40)

        b0.clicked.connect(self.act0)
        b1.clicked.connect(self.act1)
        b2.clicked.connect(self.act2)
        b3.clicked.connect(self.act3)
        b4.clicked.connect(self.act4)
        b5.clicked.connect(self.act5)
        b6.clicked.connect(self.act6)
        b7.clicked.connect(self.act7)
        b8.clicked.connect(self.act8)
        b9.clicked.connect(self.act9)
        be.clicked.connect(self.actequ)
        bmin.clicked.connect(self.actmin)
        bdiv.clicked.connect(self.actdiv)
        bmul.clicked.connect(self.actmul)
        bplus.clicked.connect(self.actplus)
        bp.clicked.connect(self.actp)
        bcle.clicked.connect(self.actcle)
        bdel.clicked.connect(self.actdel) 

    def act0(self):            
        text = self.label.text()
        self.label.setText(text + "0")

    def act1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def act2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def act3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def act4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def act5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def act6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def act7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def act8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def act9(self):
        text = self.label.text()
        self.label.setText(text + "9")   

    def actplus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def actmin(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def actdiv(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def actmul(self):
        text = self.label.text()
        self.label.setText(text + " x ")

    def actp(self):
        text = self.label.text()
        self.label.setText(text + ".")    

    def actcle(self):
        self.label.setText("")

    def actdel(self):
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])  

    def actequ(self):
        equation = self.label.text()
        try:
            if "+" in equation:
                a,b = equation.split("+")  
                result = float(a) + float(b)  
                if result.is_integer():
                    self.label.setText(str(int(result)))
                else:    
                    self.label.setText(str(result))
            if "-" in equation:
                a,b = equation.split("-")  
                result = float(a) - float(b)  
                if result.is_integer():
                    self.label.setText(str(int(result)))
                else:    
                    self.label.setText(str(result))    
            if "x" in equation:
                a,b = equation.split("x")  
                result = float(a) * float(b)
                if result < 0 and result.is_integer():
                    self.label.setText(str(int(result)))
                if result > 0 and result.is_integer():
                    self.label.setText(str(int(result)))     
                else:    
                    self.label.setText(str(result))            
        except Exception as e:
            e="Can only execute 1 order once"
            self.label.setText(str(e))     


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())