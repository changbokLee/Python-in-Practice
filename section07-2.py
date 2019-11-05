#네임스페이스 
#클래스 ,인스턴스 차이 중요
# 변수에 할당에서 인스턴스화 시켜서 한다
# 네임스페이스: 객체를 인스턴스화 할 때 저장된공간
# 클래스 변수: 직접사용가능 ,객체보다 먼저생성
# 인스턴스 변수 : 객체마다 별도로 존재

# 예제2
# self의 이해
class SelfTest:
    @staticmethod
    def function1():
        print('fuction1 called!')

    def function2(self):
        print(id(self))
        print('function2 caleed')

self_test =SelfTest()
SelfTest.function1()
self_test.function2()

print(id(self_test))

#클래스는 먼저 생기고 호출하고 그 다음 인스턴스로 해서 호출

#예제 3
# 클래스 변수 ,인스턴스 변수
class WareHouse:
    #클래스 변수
    stock_num = 0
    def __init__(self ,name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) #클래스 네임스페이스 , 클래스 변수(공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1