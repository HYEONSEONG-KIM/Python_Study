# 1~1000사이의 숫자중 3의 배수가 아닌 숫자의 합
a = range(1,1001)

sum = 0

for i in a :
    if not i % 3 == 0 :
       sum += i
       
print("sum : ", sum) 