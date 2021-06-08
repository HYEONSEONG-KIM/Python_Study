a = "56"
b = 6
c = 1.1
d = True

#타입이 다르기 떄문에 오류 => str로 문자열로 캐스팅
print(a + str(b) + str(c) + str(d))
#일일히 캐스팅 하기 번거로움 => ,로 구분하여 print
print(a,b,c,d)
#c언어의 printf와 비슷한 포맷
print("{}:{}:{}:{}".format(a,b,c,d))
