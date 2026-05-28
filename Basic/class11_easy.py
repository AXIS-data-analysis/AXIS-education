# ==========================================
# [AXIS Basic반] 11회차 문제
# ==========================================
"""
문제 1. super()와 상속
부모 클래스인 Animal을 상속받는 자식 클래스 Dog을 만들고, 
super()를 사용하여 부모 클래스의 __init__ 메소드를 호출하는 코드를 작성하세요.
"""
### 모범답안 ###
class Animal:
    def __init__(self, name):
        self.name = name

# 1. Animal 클래스를 상속받는 Dog 클래스를 정의하세요.
class Dog(Animal):
    # 2. __init__ 메소드를 정의하고 매개변수로 name과 breed(품종)를 받으세요.
    def __init__(self, name, breed):
        # 3. super()를 사용하여 부모 클래스의 __init__ 메소드에 name을 전달하세요.
        super().__init__(name)
        # 4. 전달받은 breed를 자식 클래스의 멤버 변수로 저장하세요.
        self.breed = breed

# 5. 이름은 "바둑이", 품종은 "진돗개"인 Dog 인스턴스를 생성하고 출력해서 확인해 보세요.
my_dog = Dog("바둑이", "진돗개")
print(f"우리 강아지 이름은 {my_dog.name}이고, 품종은 {my_dog.breed}입니다.")


"""
문제 2. 다중 상속과 메소드 오버라이딩 & pass
두 개의 부모 클래스를 다중 상속받아 새로운 기능을 추가하고, 
부모 클래스의 메소드를 덮어쓰는(오버라이딩) 코드를 작성하세요.
"""
### 모범답안 ###
class Speaker:
    def sound(self):
        print("소리를 출력합니다.")

class Mic:
    def record(self):
        print("소리를 녹음합니다.")

# 1. Speaker와 Mic 클래스를 다중 상속받는 SmartSpeaker 클래스를 정의하세요.
class SmartSpeaker(Speaker, Mic):
    
    # 2. 부모 클래스인 Speaker의 sound() 메소드를 오버라이딩하여 
    # "스마트하게 소리를 출력합니다."가 출력되도록 덮어쓰세요.
    def sound(self):
        print("스마트하게 소리를 출력합니다.")
    
    # 3. 인공지능 기능인 ai_search() 메소드를 정의하되, 
    # 당장 구현하지 않으므로 pass 키워드를 사용해 비워두세요.
    def ai_search(self):
        pass

# 4. SmartSpeaker 객체를 생성하고, 오버라이딩된 sound() 메소드와 
# 다중 상속받은 record() 메소드를 각각 호출해 보세요.
my_speaker = SmartSpeaker()
my_speaker.sound()
my_speaker.record()


"""
문제 3. 예외 처리 (try, except, else, finally)
숫자를 나누는 연산 중에 0으로 나누는 등 예상치 못한 오류가 발생할 수 있습니다.
에러 발생 여부에 따라 각각 다른 메시지가 출력되도록 예외 처리 코드를 작성하세요.

num1 = 10
num2 = 0
"""
### 모범답안 ###
num1 = 10
num2 = 0

# 1. try 블록 안에서 num1을 num2로 나누어 result 변수에 저장하세요.
try:
    result = num1 / num2
# 2. except 블록에서 에러가 발생했을 때 "에러가 발생했어요!"를 출력하세요.
except:
    print("에러가 발생했어요!")
# 3. else 블록에서 정상 동작 시 f-string을 활용해 "연산 결과는 {result}입니다"를 출력하세요.
else:
    print(f"연산 결과는 {result}입니다")
# 4. finally 블록에서 마지막으로 항상 "수행 종료"가 출력되도록 하세요.
finally:
    print("수행 종료")