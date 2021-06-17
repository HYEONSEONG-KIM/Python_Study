import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)

#cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()

query = "DELETE FROM sample WHERE COL01 = 7"

cnt = cursor.execute(query)
 
data = cursor.fetchall()


result = db.commit()

print(data)
print(cnt)