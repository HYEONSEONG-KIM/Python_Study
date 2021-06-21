import numpy as np
import matplotlib.pyplot as plt
import pymysql
from day09.my3dgraph import figure

def getPricesFromName(s_name):
    ret =[]
    db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
    
    #cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    
    
    query = f"""
        SELECT price FROM stock where s_name = '{s_name}'
        ORDER BY crw_date
        """
    
    cursor.execute(query)
    
    data =cursor.fetchall()
    
    for row in data :
        ret.append(row[0])
        
   
    db.commit()
    cursor.close()
    db.close()
    
    return np.array(ret)/data[0][0]





fig = plt.figure(1)
ax = fig.gca(projection='3d')

y = range(10)
x = np.zeros((10))
zs = []
zs.append(getPricesFromName('삼성전자'))
zs.append(getPricesFromName('SK'))
zs.append(getPricesFromName('LG'))



figure = ax.plot(x+0, y , zs[0])
figure = ax.plot(x+1, y , zs[1])
figure = ax.plot(x+2, y , zs[2])


plt.show()


