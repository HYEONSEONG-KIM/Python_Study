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
        
        for i in range(10) :
            btn = QPushButton('', self)
            btn.setIcon(QtGui.QIcon("0.png"))
            btn.setIconSize(QtCore.QSize(40,40))
            btn.setGeometry(40*i,0,40,40)
           
            btn.clicked.connect(self.myclick)
            
        
    def myclick(self):
        self.sender().setIcon(QtGui.QIcon("1.png"))
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


