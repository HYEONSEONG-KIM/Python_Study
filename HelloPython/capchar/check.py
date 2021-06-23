import os
import sys
import urllib.request

def checkImg(id,secret,keys,input):
    client_id = id # 개발자센터에서 발급받은 Client ID 값
    client_secret = secret # 개발자센터에서 발급받은 Client Secret 값
    code = "1"
    key = keys
    value = input
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        return result
    else:
        print("Error Code:" + rescode)