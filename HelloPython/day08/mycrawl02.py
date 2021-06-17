import requests
from bs4 import BeautifulSoup
from spyder.widgets.browser import WebPage

response = requests.get("http://localhost/WEBCRAWL/index.html")
response.encoding = 'utf-8'

soup = BeautifulSoup(response.content, "html.parser")
table = soup.select('td')
for data in table :
    print(data.string)