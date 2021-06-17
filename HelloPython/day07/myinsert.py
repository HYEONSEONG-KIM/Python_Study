import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)

#cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()

query = "INSERT INTO SAMPLE VALUES(%s,%s,%s)"

cnt = cursor.execute(query,(7,7,7))
 
data = cursor.fetchall()


result = db.commit()

print(data)
print(cnt)