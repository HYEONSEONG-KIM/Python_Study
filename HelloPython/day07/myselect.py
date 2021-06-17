import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)

#cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()

query = "SELECT * FROM jmt"

cursor.execute(query)
 
data = cursor.fetchall()


result = db.commit()
db.close()
cursor.close()
print(data)