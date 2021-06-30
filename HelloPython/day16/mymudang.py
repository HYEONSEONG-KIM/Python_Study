import numpy as np
from tensorflow.keras.models import load_model

model = load_model('models/20201213_202430.h5')
def getIJ(input):
    
    for i in range(len(input[0])) :
        for j in range(len(input)) :
            if input[i][j] == 2 :
                input[i][j] = -1;

  
               
    
    input = input.reshape((1, 20, 20, 1))
    print(input)
    print(input.shape)
    output = model.predict(input).squeeze()
    output = output.reshape((20, 20))
    i, j = np.unravel_index(np.argmax(output), output.shape)
    return i,j

if __name__ == '__main__':
    arr2D =  np.zeros((20,20),dtype = np.int64)
    arr2D[0][0] = 1
    arr2D[0][1] = 2
    arr2D[0][2] = 1
    i,j = getIJ(arr2D)
    print("i",i)
    print("j",j)