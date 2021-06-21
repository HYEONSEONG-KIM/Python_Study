import requests
from bs4 import BeautifulSoup
import datetime
import time
import pymysql
import pymysql
from day08 import myinsert_stock

# def insertStock(val) :
#     db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
#     cursor = db.cursor()
#     query = "INSERT INTO stock(s_name,s_code,price,crw_date) VALUES(%s,%s,%s,%s)"
#
#     cnt = cursor.executemany(query,val)
#
#     data = cursor.fetchall()
#
#
#     db.commit()
#     db.close()
#     cursor.close()
#     print(data)
#     print(cnt)
    
response = requests.get("http://stock.hankyung.com/apps/rank.panel_sub?market=1")
#response.raise_for_status()
response.encoding = 'euc-kr'

soup = BeautifulSoup(response.content, "html.parser")
sbjs = soup.select('.sbj')
crw_date = time.strftime('%Y%m%d.%H%M', time.localtime(time.time()))

val = []

for sbj in sbjs :
    s_name = sbj.text
    s_code = sbj.a['href'].split('=')[1]
    price = int(sbj.parent.select('td')[1].text.replace(",",""))
    val.append((s_name,s_code,price,crw_date))

myinsert_stock.insertStock(val)
    



