# 첫 숫자를 입력 -> 끝 숫자를 입력 -> 배수를 입력 => 첫 숫자와 끝 숫자의 배수의 합 구하기

a = int(input("첫 숫자 입력"))
b = int(input("끝 숫자 입력"))
c = int(input("배수를 입력"))

sum = 0

for i in range(a,b):
    if i % c == 0 :
       sum += i 
       
print("result " + str(sum))