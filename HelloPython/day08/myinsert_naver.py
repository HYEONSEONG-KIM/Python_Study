import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
cursor = db.cursor()
query = "INSERT INTO JMT(title,link,description,bloggername,bloggerlink,postdate) VALUES(%s,%s,%s,%s,%s,%s)"
cnt = cursor.execute(query,(7,7,7,7,7,7))
 
data = cursor.fetchall()


db.commit()
db.close()
cursor.close()
print(data)
print(cnt)