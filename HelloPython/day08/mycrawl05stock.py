import requests
from bs4 import BeautifulSoup
import datetime
import time
import pymysql

response = requests.get("http://stock.hankyung.com/apps/rank.panel_sub?market=1")
#response.raise_for_status()
response.encoding = 'euc-kr'

soup = BeautifulSoup(response.content, "html.parser")
title = soup.select('.sbj')
price = soup.select('tr > td:nth-child(2)')
now = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))

db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
cursor = db.cursor()

query = "INSERT INTO stock VALUES(%s,%s,%s,%s)"

for i in range(0,len(title)) :
    cursor.execute(query,(title[i].string,"",price[i].string,now))
    db.commit()
db.close()
#
# for data in price :
#     print(data.string)

