import random
mine = input("홀/짝을 선택하시오")
com = ""
result = ""

ran = random.random()

if ran > 0.5 :
    com = "홀"
else :
    com = "짝"
    
if com == mine :
    result = "이김"
else :
    result = "짐"
    
print("mine : ",mine)
print("com : ",com)
print("result : ",result)
print(ran)