import numpy as np
import matplotlib.pyplot as plt
import pymysql

def getS_names():
    s_name = []
    db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
    cursor = db.cursor()
    
    sql = """
    SELECT a.s_name
        from
        (
        SELECT s_name,count(s_name) cnt FROM stock GROUP BY s_name
        ) a
        WHERE a.cnt < 20
    """
    cursor.execute(sql)
    
    data =cursor.fetchall()
    
    for name in data:
        s_name.append(name[0])
        
    cursor.close()
    db.close()
    
    return s_name


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
    
    ret = np.array(ret)
    
    myDivide = data[0][0]
    if data[0][0] == 0 :
        ret = ret+1
        myDivide =1
    
    return np.array(ret)/myDivide


names = getS_names()

fig = plt.figure(1)
ax = fig.gca(projection='3d')

y = range(10)
x = np.zeros((10))
zs = []

for n in names :
    zs.append(getPricesFromName(n))

for idx,n in enumerate(names) :
    figure = ax.plot(x+idx,y,zs[idx])

plt.show()


