# Section 10 
# 파이썬 예외처리의 이해

# 예외 조류
# 문법적으로 에러가 없지만 코드 실행(런타임)프로게스에서 발생하는 예외처리도 중요

# Linter : 코드스타일 , 문법 체크
# Syntax Error 잘못된 문법

# NameError: 참조변수 없음
# ZeroDivisionError : 0나누기 에러
# IndexError : 인덱스 범위 오버
# AttribyteError : 모듈 ,클래스에 잇는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month())

#ValueError : 참조값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError

f = open('test.txt', 'r')

# TypeError

x= [1,2]
y = (1,2)
z= 'test'

print(x +  y)

# ㅖ외처리기본
# try :에러가 발생할 가능성이 있는 코드실행
# except :에러명 1
# except :에러명 2
# else: 에러가 발생하지 않았을 경우 실행
# finally 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

