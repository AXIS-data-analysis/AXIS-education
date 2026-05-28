# ==========================================
# [AXIS Basic반] 10회차 문제
# ==========================================
"""
문제 1. 클래스의 생성자(__init__)와 멤버 변수
자동차의 기본 정보를 담는 Car 클래스를 만들어 봅시다.
객체가 생성될 때 브랜드(brand)와 가격(price)을 전달받아 멤버 변수로 저장하는 생성자를 작성하고, 
정보를 출력하는 코드를 완성하세요.
"""
### 모범답안 ###
# 1. Car 클래스와 __init__ 생성자를 정의하여 멤버 변수 brand와 price를 초기화하세요.
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

# 2. 브랜드는 "테슬라", 가격은 80000000인 Car 인스턴스(객체)를 생성하여 my_car 변수에 저장하세요.
my_car = Car("테슬라", 80000000)

# 3. f-string과 멤버 변수를 사용하여 my_car의 브랜드와 가격을 출력하세요.
#    * 출력 예시: 제 차는 테슬라이고, 가격은 80000000원입니다.
print(f"제 차는 {my_car.brand}이고, 가격은 {my_car.price}원입니다.")

"""
문제 2. 클래스 메소드 정의와 self
문제 1에서 만든 Car 클래스에 주행(drive) 기능을 추가하려고 합니다.
주행할 거리(km)를 전달받아 메세지를 출력하는 메소드를 작성하고 호출해 보세요.
"""
### 모범답안 ###
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    # 1. distance를 매개변수로 받아 주행 메시지를 출력하는 drive 메소드를 정의하세요. 
    # (힌트: 클래스 메소드의 첫 번째 매개변수는 반드시 자기 자신을 의미하는 self여야 합니다.)
    def drive(self, distance):
        print(f"{self.brand} 차량이 {distance}km를 주행합니다.")

# 2. 브랜드는 "현대", 가격은 40000000인 Car 인스턴스를 생성하세요.
my_car = Car("현대", 40000000)

# 3. 생성한 객체를 통해 drive 메소드를 호출하고 50을 전달해 보세요.
#    * 출력 예시: 현대 차량이 50km를 주행합니다.
my_car.drive(50)

"""
문제 3. 클래스 상속 (Inheritance)
Car 클래스의 기본 기능(브랜드, 가격, drive)을 그대로 물려받으면서, 
전기차만의 새로운 기능(배터리 충전)을 가진 ElectricCar 클래스를 만들어 봅시다.
"""
### 모범답안 ###
# (부모 클래스인 Car는 위에 이미 만들어져 있다고 가정합니다)
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def drive(self, distance):
        print(f"{self.brand} 차량이 {distance}km를 주행합니다.")

# 1. 부모 클래스인 Car를 상속받는 새로운 자식 클래스 ElectricCar를 정의하세요.
class ElectricCar(Car):
    
    # 2. 충전 시간(time)을 매개변수로 받아 충전 메시지를 출력하는 charge 메소드를 추가하세요.
    def charge(self, time):
        print(f"{time}분 동안 고속 충전을 진행합니다.")

# 3. 브랜드가 "기아", 가격이 50000000인 ElectricCar 인스턴스를 생성하세요.
ev_car = ElectricCar("기아", 50000000)

# 4. 부모 클래스에게 물려받은 drive 메소드에 30을 전달하여 호출하세요.
ev_car.drive(30)

# 5. 자식 클래스에서 새로 추가한 charge 메소드에 40을 전달하여 호출하세요.
ev_car.charge(40)