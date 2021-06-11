import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
# 파일 불러오기
form_class = uic.loadUiType('myqt02.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
       
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        num = int(self.le.text())
        print(num)
        num += 1
        self.le.setText(str(num))
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


