import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
 
 # Open the drawing window 1, draw in 3D space
fig = plt.figure(1)
ax = fig.gca(projection='3d')
 
 # Give points (0, 0, 0) and (100, 200, 300)
y = range(3)
x = np.zeros((3))
zs = []
zs.append([0,0,0])
zs.append([0,50,0])

for i in range(0,3) :
    x_np = x + i
    figure = ax.plot(x_np, y, zs[0], c='y')
    





    
 
 # Connect the first two points in the array
# figure = ax.plot(x, y, z, c='y')
# figure = ax.plot(x2, y, z2, c='b')


plt.show()
