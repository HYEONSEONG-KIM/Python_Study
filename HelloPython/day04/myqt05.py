import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
 
# 파일 불러오기
form_class = uic.loadUiType('myqt05.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
       
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        mine = self.leMine.text()
        ran = random.random()
        com = ""
        if ran > 0.5 :
            com = "짝"
        else :
            com = "홀"
        
        result = ""
        
        if com == mine :
            result = "이김"
        else :
            result = "짐"
        
        self.leCom.setText(com)
        self.leResult.setText(result)
            
        
      
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


