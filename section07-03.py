#파이썬 클래스 상세이해
# 상속 , 다중상속

# 예제1
# 상속기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든속성 ,메소드 사용가능

# 라면 -> 속성(종류 , 회사 , 맛 , 면 종류, 이름 ): 부모클래스
# 코드의 재사용 가능

class Car:
    """Parent Class"""
    def __init__(self, tp , color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Clas "Show Method!"'


class BmwCar(Car):
    """sub class"""
    def __init__(self,car_name ,tp , color):
        super().__init__(tp,color)
        self.car_name = car_name


    def show_model(self) -> None:
        return "Your Car Name: %s " % self.car_name

class BenzCar(Car):
    """sub class"""
    def __init__(self,car_name ,tp , color):
        super().__init__(tp,color)
        self.car_name = car_name


    def show_model(self) -> None:
        return "Your Car Name: %s " % self.car_name
    
    def show(self):
        return 'Car Info: %s %s %s' % (self.car_name, self.type, self.color)

# 일반사용
model1 = BmwCar('520d', 'sedan', 'red')
print(model1.color) # super
print(model1.type) # super
print(model1.car_name) # sub
print(model1.show()) # super
print(model1.show_model) # sub
print(model1.__dict__)

# Method Overiding(오버라이딩)
model2 =BenzCar("220d", "suv", "black")
print(model2.show)

# Parent Method Call
model3 = BenzCar("350s", "sedan", "sliver")
print(model3.show())

# Inheriatance Info(상속정보)
print(BmwCar.mro())
print(BenzCar.mro())

#예제2 
# 다중상속

class X(object):
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B, A, Z):
    pass

print(M.mro)
print(A.mro())


ws = wb.active
ws['A1']  = 42
ws.apppend([1,2,3])

import datetime


