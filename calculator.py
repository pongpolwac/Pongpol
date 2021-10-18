import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()

layout = QGridLayout()
l1=layout.addWidget(QPushButton('7'), 0, 0)
l2=layout.addWidget(QPushButton('8'), 0, 1)
l3=layout.addWidget(QPushButton('9'), 0, 2)
l4=layout.addWidget(QPushButton('+'), 0, 3)
l5=layout.addWidget(QPushButton('4'), 1, 0)
l6=layout.addWidget(QPushButton('5'), 1, 1)
l7=layout.addWidget(QPushButton('6'), 1, 2)
l8=layout.addWidget(QPushButton('-'), 1, 3)
l9=layout.addWidget(QPushButton('1'), 2, 0)
l10=layout.addWidget(QPushButton('2'), 2, 1)
l11=layout.addWidget(QPushButton('3'), 2, 2)
l12=layout.addWidget(QPushButton('x'), 2, 3)
l13=layout.addWidget(QPushButton('.'), 3, 0)
l14=layout.addWidget(QPushButton('0'), 3, 1)
l15=layout.addWidget(QPushButton('='), 3, 2)
l16=layout.addWidget(QPushButton('/'), 3, 3)
l17=layout.addWidget(QPushButton('Del'), 4, 0, 1, 2)
l18=layout.addWidget(QPushButton('C'), 4, 2, 1, 2)

window.setLayout(layout)

window.setWindowTitle('Pongpol Calculator')
window.show()
sys.exit(app.exec_())