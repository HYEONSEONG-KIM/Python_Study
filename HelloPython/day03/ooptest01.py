class Dog:
     def __init__(self):
         self.skill_bark = False
         
         
     def doSergury(self):
        self.skill_bark = True
        

class Bird:
    
    def __init__(self):
        self.x = 5
        self.y = 5
    
    def goTosaukkang(self,x,y):
        self.x = x
        self.y = y
        
# 다중 상속시 상속받는 자식의 생성자에 super하나만 선언하면 먼저 상속받은 클래스만 실행
# 상속받는 모든 부모의 클래스 생성자를 모두 선언하여 주어야 함
class GaeSae(Dog,Bird):
    
    def __init__(self):
        Dog.__init__(self)      
        Bird.__init__(self)

gs = GaeSae()

print(gs.skill_bark)
print(gs.x)
print(gs.y)
gs.doSergury()
gs.goTosaukkang(50, 50)
print(gs.skill_bark)
print(gs.x)
print(gs.y)