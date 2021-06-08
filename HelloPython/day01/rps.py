import random
mine = input("가위 바위 보")

com = ""
result = ""

ran = random.random()

if ran > 0.33 :
    com = "가위"
elif ran > 0.66 :
    com = "바위"
else :
    com = "보"
    

if mine =="가위" :
    
    if com == "가위" :
        result = "비김"
    elif com == "바위":
        result = "짐"
    else    :
        result = "이김"
        
elif mine =="바위" :
    
    if com == "가위" :
        result = "이김"
    elif com == "바위":
        result = "비김"
    else    :
        result = "짐"
else :
    if com == "가위" :
        result = "짐"
    elif com == "바위":
        result = "이김"
    else    :
        result = "비김"
        
print(mine)
print(com)
print(result)
        