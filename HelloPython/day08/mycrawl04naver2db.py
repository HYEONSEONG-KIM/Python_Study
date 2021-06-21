from bs4 import BeautifulSoup
import os
import sys
import urllib.request
import pymysql
import pymysql


db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
cursor = db.cursor()
query = "INSERT INTO JMT(title,link,description,bloggername,bloggerlink,postdate) VALUES(%s,%s,%s,%s,%s,%s)"

client_id = "fybiUHvuaJPxmxTHsvBp"
client_secret = "K2F0icIJsA"
encText = urllib.parse.quote("대흥동 맛집")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    xml = response_body.decode('utf-8')
    soup = BeautifulSoup(xml, "xml")
    items = soup.select('item')
    
    for item in items:
        title = item.title.text
        link = item.link.text
        description = item.description.text
        bloggername = item.bloggername.text
        bloggerlink = item.bloggerlink.text
        postdate = item.postdate.text
        cnt = cursor.execute(query,(title,link,description,bloggername,bloggerlink,postdate))
       
    
    
    db.commit()
    db.close()
    cursor.close()
    
else:
    print("Error Code:" + rescode)
    
    
    
    
    