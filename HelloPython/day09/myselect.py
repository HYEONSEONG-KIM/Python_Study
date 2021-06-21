import pymysql
import numpy as np

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
    db.close()
    
    return np.array(ret)
    
        
if __name__ =='__main__':
    arr_n = getPricesFromName('삼성전자')
    print(arr_n)