import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
 
# 파일 불러오기
form_class = uic.loadUiType('myqt07.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
       
        self.pb.clicked.connect(self.myclick)
        
        
    def myclick(self):
        mine = self.leMine.text()
        ran = random.random()
        com = ""
        if ran > 0.66 :
            com = "가위"
        elif ran > 0.33 :
            com = "바위"
        else :
            com = "보"
        
        result = ""
        
        if mine =="가위" :
            
            if com == "가위" :
                result = "비김"
            elif com == "바위":
                result = "짐"
            else    :
                result = "이김"
                
        elif mine =="바위" :
            
            if com == "가위" :
                result = "이김"
            elif com == "바위":
                result = "비김"
            else    :
                result = "짐"
        else :
            if com == "가위" :
                result = "짐"
            elif com == "바위":
                result = "이김"
            else    :
                result = "비김"
        
        self.leCom.setText(com)
        self.leResult.setText(result)
            
        
      
 
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


