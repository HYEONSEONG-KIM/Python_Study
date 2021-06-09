a = ["홍길동", "전우치", "신사임당"]

j = 0
for i in a:
    print(j,i)
    j += 1

# enumerate함수를 사용하면 앞(idx)에는 몇번째 도는 결과가 나오고, 뒤(i)에는 담은 값이 출력
for idx,i in enumerate(a) :
    print(idx,i)
