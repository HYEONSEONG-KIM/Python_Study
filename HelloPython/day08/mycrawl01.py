import requests

response = requests.get("http://localhost/WEBCRAWL/index.html")
#response.raise_for_status()
response.encoding = 'utf-8'
print(response.text)