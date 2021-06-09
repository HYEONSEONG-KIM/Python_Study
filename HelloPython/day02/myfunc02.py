# 파이썬에는 멀티 return이 가능
# 멀티 return시에 해당 메서드를 불러줄때는 멀티 갯수에 맞는 변수를 같이 선언

def addmin(a,b):
    return a+b, a-b

sum,min = addmin(6,7)

print(sum)
print(min)