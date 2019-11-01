v1 = 1
while v1< 11:
    print("v1 is :" ,v1)
    v1 += 1

for v2 in range(10):
    print("v2 is:", v2)

# while 조건
# for 반복할 변수를 임의대로 선언해주고 in <=안에서 계속돌수있다? range (리스트 반환함수)
# for 변수 in 리스트(또는 튜플 문자열)


sum = 0
cnt1 = 1

while cnt1 <= 100:
    sum += cnt1
    cnt1 += 1

print ('1~100:', sum)

#시퀀스(순서가 있는)자료형 반복
#iterable 리턴 함수 range ,reversed , enumerate ,fliter ,map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for v in names:
    print("You are:", v)

my_info = {
    "name":"kim",
    "age":33,
    "city":"Seoul"
}


numbers = [14, 3, 4, 7 ,10 ,24, 17 ,2 ,33, 15, 34 ,36 ,38]
#for -else구문 for문이 제대로 수행됫다면 for문으로 가고 else문으로 간다.(정상적으로 실행하고 나서)
for num in numbers:
    if num == 33:
        print("found:33 !")
        break
    else:
        print("not found: 33!") 
else:
    print("Not found 33....")        

# continue

lt =[ "1" ,2,5 ,True,4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입:",type(v))