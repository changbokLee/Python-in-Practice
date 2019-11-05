# Section 06
# 파이썬 함수식 및 람다(ladmda)

# 함수 정의 방법
# def 함수명(parameter):
# code

# 함수 호출
# 함수명()

# 예제1
def hello(world):
    print("Hello", world)

hello("Pyhon!")
hello(7777)

#예제 4 argumeents의 줄임말 
# *args 퓨틀로 다넘어온다, *kwargs 

def args_func(*args):
    print(args)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

#kwargs =키워드에 매개변수함수 딕셔너리 형태로 매개변수 호출
def kwargs_func(**kwargs):
    for k,v  in kwargs.items():
        print(k ,v)

kwargs_func(name1='Kim', name2 ='park', name3 = 'Lee')


#전체혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10,20)
example_mul(10,20, 'park', 'kim', age1=24, age2= 35)

# 중첩함수(클로저)

def nested_func(num):
    def func_in_func(num):
        print('',num)
    print("in_func")
    func_in_func(num + 1000)

nested_func(10000)    


a = "abc"
if "c":
    print("true")

