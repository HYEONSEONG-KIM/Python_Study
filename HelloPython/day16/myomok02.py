import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui, QtCore, QtWidgets
from PyQt5.Qt import QPixmap
from _csv import Error
from sqlalchemy.sql.expression import false
 
# 파일 불러오기
form_class = uic.loadUiType('myomok02.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]
            
         
            
        ]
        # 전역변수를 담는 그릇...버튼 하나하나에 객체를 나누어 주기 위해서
        self.pb2D = []
        self.flagWB = True
        self.flagOver = False
        self.pbReset.clicked.connect(self.myReset)
        self.cnt = 0;
        
        for i in range(len(self.arr2D[0])) :
            line = []
            for j in range(len(self.arr2D)) :
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(40*j,40*i,40,40)
                strTooltip = str(i) + "," + str(j) 
                btn.setToolTip(strTooltip)
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
        self.myRender()
        
        
    def myRender(self):
        for i in range(len(self.pb2D[0])) :
            for j in range(len(self.pb2D)) :
                int_pb = self.arr2D[i][j]
                self.pb2D[i][j].setIcon(QtGui.QIcon("{}.png".format(int_pb)))
                
    def myReset(self):
        self.flagOver = False
        self.flagWB = True
        
        for i in range(len(self.arr2D[0])) :
            for j in range(len(self.arr2D)) : 
                self.arr2D[i][j] = 0
        
        self.myRender()
        
        
                    
    def myclick(self):
        
        if self.flagOver :
            return
        
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
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
       
        
        # print("up",up)
        # print("dw",dw)
        # print("ri",ri)
        # print("le",le)
        # print("ur",ur)
        # print("ul",ul)
        # print("dr",dr)
        # print("dl",dl)
        # print("d1",d1)
        # print("d2",d2)
        # print("d3",d3)
        # print("d4",d4)
        

        
        self.myRender()
        
        if d1 ==5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flagWB :
                QtWidgets.QMessageBox.information(self, "gameover", "백돌승리")
            else :
                QtWidgets.QMessageBox.information(self, "gameover", "흑돌승리")
                
            self.flagOver = True
            return
            
        self.arr2D[0][self.cnt] = 2
        self.cnt += 1
        self.myRender()
        # self.flagWB = not self.flagWB
    
    def getDL(self,i,j,stone):
        cnt = 0
        try :
            while True :
                i += 1
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
                j -= 1
                if j < 0 :
                    return cnt
                
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
                if j < 0 :
                    return cnt
                
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


