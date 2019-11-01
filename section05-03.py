q1 ={"봄": "딸기",  "여름": "토마토", "가을":"사과"}

for k in q1.keys():
    if k == '가을':
        print(k)

for v in q1.items():
    if v == '가을':
        print(v)

q2 ={"봄": "딸기", "여름":"토마토", "가을":"사과"}

for k,v in q2.items():
    if v =='사과':
        print(k ,v)
        break
else:
    print("사과없음")


a= 77

if a >= 81:
    print('A학점')
elif a >= 61:
    print('B학점')
elif a >=41:
    print('C학점')

for n in range(1,101):
    if n % 2 != 0:
        print(n, end= ',')

# 리스트 컴프리헨션
numbers =[]
for n in range(1,101):
    numbers.append(n)
print(numbers)

numbers2 =[x for x in range(1,101)]
print(numbers2)


