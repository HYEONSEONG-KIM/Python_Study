# 첫 숫자를 입력 -> 끝 숫자를 입력 => 두 수의 사이 합은 x입니다 라고 출력(앞이 작은숫자)

a = int(input("첫 숫자 입력"))
b = int(input("끝 숫자 입력"))
sum = 0

for i in range(a,b+1) :
    sum += i
    
print("두수의 사이의 합은 " + str(sum) + "입니다")