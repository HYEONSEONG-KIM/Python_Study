# 클래스 생성시 전역변후는 생성자에서 선언한다
# 각 메서드에는 self라는 파라미터를 반드시 넣어준다
class Animal :

    def __init__(self):
        self.age = 1
        
        
    def getOlder(self):
        self.age += 1
    
# 특정 클래스를 상속 받을때는 클래스명 옆에 (부모클래스)
class Human(Animal):
    
    def __init__(self):
        # 상속을 받을때는 부모클래스의 변수를 받아오기 위해서는 super().__init__() 을 호출해야함
        super().__init__()
        self.level_lang = 0
    
    def levelUp(self):
        self.level_lang += 1
    

hum = Human()

print(hum.age)
print(hum.level_lang)

hum.getOlder()
hum.levelUp()
    
print(hum.age)
print(hum.level_lang)
    