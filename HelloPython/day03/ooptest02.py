# 자바와 달리 생성자가 있으면 소멸자가 있음
# 소멸자는 프로그램이 끝난 후 실행
# toString과 같은 역할 -> str
class Terran:
    def __init__(self):
        print("생성자")
    
    def __del__(self):
        print("소멸자")
        
    def __str__(self):
        return "abcd"
    


print(Terran())