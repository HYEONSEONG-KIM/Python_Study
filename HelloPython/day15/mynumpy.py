import numpy as np

arr = [1,2,3,4,5,6]
arr_n = np.array(arr)

print(arr_n.shape)

arr_n2 = np.reshape(arr_n,(2,3))

print(arr_n2)
print(arr_n2.shape)