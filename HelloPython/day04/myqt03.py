import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
# 파일 불러오기
form_class = uic.loadUiType('myqt03.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
       
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        result = a+b
        self.le3.setText(str(result))
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


