import pymysql

def insertStock(val) :
    db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
    cursor = db.cursor()
    query = "INSERT INTO stock(s_name,s_code,price,crw_date) VALUES(%s,%s,%s,%s)"
    
    cnt = cursor.executemany(query,val)
     
    data = cursor.fetchall()
    
    
    db.commit()
    db.close()
    cursor.close()
    print(data)
    print(cnt)


if __name__ == '__main__':
    val = [
            (1,1,1,1),
            (2,2,2,2)
        ]
    insertStock(val)