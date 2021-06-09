# 출력할 구구단을 입력하고 구구단 출력

a = int(input("구구단 입력"))

for i in range(1,10) :
    print(str(a) + "*" + str(i) + "=" + str(a*i))
    
    