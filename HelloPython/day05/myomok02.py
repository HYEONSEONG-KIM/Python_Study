import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui, QtCore
from PyQt5.Qt import QPixmap
from _csv import Error
 
# 파일 불러오기
form_class = uic.loadUiType('myomok02.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.arr2D = [
            [0,0,0,0, 0,0,0,0],
            [0,0,0,0, 0,0,0,0],
            [0,0,0,0, 0,0,0,0],
            [0,0,0,0, 0,0,0,0],
            
            [0,0,0,0, 0,0,0,0],
            [0,0,0,0, 0,0,0,0],
            [0,0,0,0, 0,0,0,0],
            [0,0,0,0, 0,0,0,0]
        ]
        # 전역변수를 담는 그릇...버튼 하나하나에 객체를 나누어 주기 위해서
        self.pb2D = []
        self.flagWB = True
 
        for i in range(len(self.arr2D[0])) :
            line = []
            for j in range(len(self.arr2D)) :
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(40*j,40*i,40,40)
                str_tooltip = str(i) + "," + str(j) 
                btn.setToolTip(str_tooltip)
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
        self.myrender()
        
        
    def myrender(self):
        for i in range(len(self.pb2D[0])) :
            for j in range(len(self.pb2D)) :
                int_pb = self.arr2D[i][j]
                self.pb2D[i][j].setIcon(QtGui.QIcon("{}.png".format(int_pb)))
                
                
   
    def myclick(self):
        getTool = self.sender().toolTip()
        get_ij = getTool.split(",")
        int_i = int(get_ij[0])
        int_j = int(get_ij[1])
        
        if self.arr2D[int_i][int_j] > 0 :
            return
        
        stone = 0;
        
        if self.flagWB :
            self.arr2D[int_i][int_j] = 1
            stone = 1
        else :
            self.arr2D[int_i][int_j] = 2
            stone = 2
            
        up = self.getUP(int_i,int_j,stone)    
        dw = self.getDW(int_i,int_j,stone)
        ri = self.getRI(int_i,int_j,stone)
        le = self.getLE(int_i,int_j,stone)
        
        ur = self.getUR(int_i,int_j,stone)
        ul = self.getUL(int_i,int_j,stone)
        dr = self.getDR(int_i,int_j,stone)
        dl = self.getDL(int_i,int_j,stone)
        
        
        
        self.myrender()
        self.flagWB = not self.flagWB
    
    def getDL(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i -= 1
                j -= 1
                
                if i < 0 or j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt     
    
    
    
    def getDR(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i += 1
                j += 1
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt     
    
    
    def getUL(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i -= 1
                j += 1
                if i < 0 :
                    return cnt
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt 
        
        
    
    def getUR(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i += 1
                j -= 1
                if j < 0 :
                    return cnt
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt 
    
    def getUP(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i -= 1
                if i < 0 :
                    return cnt
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt 
        
        
        
    def getDW(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i += 1
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt    
        
        
        
    def getRI(self,i,j,stone):
        cnt = 0
        try :
            while True :
                j += 1
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt
        
        
    def getLE(self,i,j,stone):
        cnt = 0
        try :
            while True :
                j -= 1
                if(j < 0) :
                    return cnt
                
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else : 
                    return cnt
        except :
            return cnt      
        
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


