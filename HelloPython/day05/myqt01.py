import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui, QtCore
from PyQt5.Qt import QPixmap
 
# 파일 불러오기
form_class = uic.loadUiType('myqt01.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.state = 0
        self.btn = QPushButton('', self)
        self.btn.setIcon(QtGui.QIcon("0.png"))
        self.btn.setIconSize(QtCore.QSize(40,40))
        self.btn.setGeometry(0,0,40,40)
       
        self.btn.clicked.connect(self.myclick)
        
        
    def myclick(self):
        self.state += 1
        int_mode = self.state % 3
        self.btn.setIcon(QtGui.QIcon('{}.png'.format(int_mode)))
        
 
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


