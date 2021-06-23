import os
import sys
import urllib.request
from datetime import datetime

def getImages(id,secret, setKey):
    client_id = id # 개발자센터에서 발급받은 Client ID 값
    client_secret = secret # 개발자센터에서 발급받은 Client Secret 값
    key = setKey # 캡차 Key 값
    url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        print("캡차 이미지 저장")
        response_body = response.read()
        dt = datetime.now()
       
        imageName =  str(dt.microsecond) + ".jpg"
        with open('static/img/' + imageName, 'wb') as f:
            f.write(response_body)
            
        return imageName
    else:
        print("Error Code:" + rescode)
    
# 현재 코드에서 이미지 입출력 어떤 방식???=> 구글링을 위한 방향성
