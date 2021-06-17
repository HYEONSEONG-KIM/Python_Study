import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)

#cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()

query = "UPDATE SAMPLE SET COL02 = 5, COL03 = 5 WHERE COL01 = 4"

cursor.execute(query)
 
data = cursor.fetchall()


result = db.commit()

print(data)