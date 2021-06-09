# 1~100 까지의 짝수의 합
a = range(2,101,2)

sum = 0;

for i in a :
    sum += i
    
print("sum = ", sum)

b = range(1,101)

sum2 = 0

for i in b:
    if i % 2 == 0 :
        sum2 += i
        
print("sum2 : ",sum2)