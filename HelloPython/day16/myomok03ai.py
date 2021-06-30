import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic,QtGui, QtCore, QtWidgets
from PyQt5.Qt import QPixmap
from _csv import Error
from sqlalchemy.sql.expression import false
import numpy as np
from dask.array.tests.test_numpy_compat import dtype
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('models/20201213_202430.h5')
def getIJ(input_ref):
    
    input = np.zeros((20,20))
    
    
    for i in range(20) :
        for j in range(20) :
            if input_ref[i][j] == 2 :
                input[i][j] = -1;
            if input_ref[i][j] == 1 :
                input[i][j] = 1;
            if input_ref[i][j] == 0 :
                input[i][j] = 0;
  
               
    
    input = input.reshape((1, 20, 20, 1))
    print(input)
    print(input.shape)
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    
    for i in range(20) :
        for j in range(20):
            if input_ref[i][j] == 2 or input_ref[i][j] == 1 :
                output[i][j] = 0
    
    i, j = np.unravel_index(np.argmax(output), output.shape)
    return i,j
 
# 파일 불러오기
form_class = uic.loadUiType('myomok03ai.ui')[0]
 
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        self.arr2D =  np.zeros((20,20),dtype = np.int64)
        
        # 전역변수를 담는 그릇...버튼 하나하나에 객체를 나누어 주기 위해서
        self.pb2D = []
        self.flagWB = True
        self.flagOver = False
        self.pbReset.clicked.connect(self.myReset)
        
       
        
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
        
       
        
        self.myRender()
        
        if d1 ==5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flagWB :
                QtWidgets.QMessageBox.information(self, "gameover", "백돌승리")
            else :
                QtWidgets.QMessageBox.information(self, "gameover", "흑돌승리")
                
            self.flagOver = True
            return
            
       
        self.flagWB = not self.flagWB
        
        #-------------------------------------------------
        
        com_i,com_j =getIJ(self.arr2D)
      
        stone = 0
        
        if self.flagWB :
            self.arr2D[com_i][com_j] = 1
            stone = 1
        else :
            self.arr2D[com_i][com_j] = 2
            stone = 2
            
        up = self.getUP(com_i,com_j,stone)    
        dw = self.getDW(com_i,com_j,stone)
        ri = self.getRI(com_i,com_j,stone)
        le = self.getLE(com_i,com_j,stone)
        
        ur = self.getUR(com_i,com_j,stone)
        ul = self.getUL(com_i,com_j,stone)
        dr = self.getDR(com_i,com_j,stone)
        dl = self.getDL(com_i,com_j,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
      
       
        
        self.myRender()
        
        if d1 ==5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flagWB :
                QtWidgets.QMessageBox.information(self, "gameover", "백돌승리")
            else :
                QtWidgets.QMessageBox.information(self, "gameover", "흑돌승리")
                
            self.flagOver = True
            
        self.flagWB = not self.flagWB
        
        
        
    
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


