import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)

#cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()

data = []

query = "SELECT price FROM stock where s_name = '삼성전자'"
cursor.execute(query)
data.append(cursor.fetchall())

query = "SELECT price FROM stock where s_name = '현대차'"
cursor.execute(query)
data.append(cursor.fetchall())

query = "SELECT price FROM stock where s_name = 'LG'"
cursor.execute(query)
data.append(cursor.fetchall())


result = db.commit()
db.close()
cursor.close()
print(data)