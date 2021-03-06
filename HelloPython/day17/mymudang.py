import numpy as np
from tensorflow.keras.models import load_model

model = load_model('models/20201213_202430.h5')
def getIJAjax(input_str):
    
    arr_num = []
    arr = input_str.split(",")


    for i in arr :
        arr_num.append(int(i))
        
        
    input = np.array(arr_num)
               
    
    input = input.reshape((1, 20, 20, 1))
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    i, j = np.unravel_index(np.argmax(output), output.shape)
    return i,j

if __name__ == '__main__':
   
    str = ""
    
    str += "1,-1,1,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0," 
    str += "0,0,0,0,0,0,0,0,0,0," + "0,0,0,0,0,0,0,0,0,0" 
    
    
    i,j = getIJAjax(str)
    print("i",i)
    print("j",j)