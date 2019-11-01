# import this
import sys

# 파이썬 기본 인코딩
# utf-8기본으로해줌
print(sys.stdin.encoding)
print(sys.stdout.encoding)

print('myname is Good boy!')


#변수선언 값을할당할때하는것
Myname = 'goodboy'

if Myname == "goodboy":
    print('ok')

#반복문


for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d =' % (i,j), (i*j))



#클래스
class Cookie:
    pass

#객체생성
Cookies = Cookie