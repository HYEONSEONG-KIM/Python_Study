import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
# 파일 불러오기
form_class = uic.loadUiType('myqt01.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
       
        self.btn.clicked.connect(self.myclick)
        
        
    def myclick(self):
        self.lbl.setText("Good Morning")
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


