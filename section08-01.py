# section 08 패키지 설정
# 모듈사용 및 Alias 설정
# 패키지 사용 장점
# 파일하나하나가 모듈이라고 볼수있다 파일들을 다 디렉토리 구조를 가진게 패키지
# 상대경로 ..부모디렉토리 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibaonacci

Fibaonacci.fib(300)


# 사용2(클래스)
from pkg.fibonacci import *

from pkg.fibonacci import Fibaonacci as fb

fb.fib(300)

#사용 4 (함수)

import pkg.calculations as c

print("ex4:", c.add(10,100))
print("ex4:", c.mul(10,100))

#사용 5(함수)

from pkg.calculations import div as d
print("ex5:", int(d(100,10)))