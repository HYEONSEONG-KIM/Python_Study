a = ["홍길동", "강감찬", "이몽룡"]

print(a[0])
print(a[1])
print(a[2])

# 배열 추가 -> append, 배열 특정 인덱스에 추가 -> insert
# 배열의 길이 -> len(배열)
b = []
b.append("홍길동")
b.append("강감찬")
b.append("이몽룡")
b.insert(len(b), "이순신")

print(b[0])
print(b[1])
print(b[2])
print(b[3])