import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='_stock_old', port=3307)

#cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()



query = "SELECT count(*) FROM stock_sync_0121"
cursor.execute(query)
data = cursor.fetchall()



result = db.commit()
db.close()
cursor.close()
print(data)