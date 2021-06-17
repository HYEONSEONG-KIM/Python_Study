from bs4 import BeautifulSoup
import os
import sys
import urllib.request
import pymysql


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
    soup = BeautifulSoup(response_body, "html.parser")
    
    
    db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)
    cursor = db.cursor()
    
    title = soup.select('item > title')
    link = soup.select('item > link')
    description = soup.select('item > description')
    bloggername = soup.select('item > bloggername')
    bloggerlink = soup.select('item > bloggerlink')
    postdate = soup.select('item > postdate')
    
 
    query = "INSERT INTO JMT VALUES(%s,%s,%s,%s,%s,%s)"
    for i in range(0,len(title)) :
        cnt = cursor.execute(query,(title[i].string,link[i].string,description[i].string, bloggername[i].string,bloggerlink[i].string,postdate[i].string))
        db.commit()
    db.close()
else:
    print("Error Code:" + rescode)
    
    
    
    
    