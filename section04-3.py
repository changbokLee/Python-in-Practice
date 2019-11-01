# 리스트(순서 중복 수정 삭제 가능), 


a = []
b= list()
c= [1,2,3,4]
d= [1,2,3,4 , 'pen', 'banana', 'orange']
e = [1,2,3,4,['pen', 'banana', 'orange']]

#인덱싱
print(d[3])
print(e[5][2])

#슬라이싱
print(d[0:2])

#연산
print( c + d)

#리스트 수정 ,삭제
c[0]= 77
print(c)

c[1:2] = [100, 1000 ,1000]
c[1] = ['a' , 'b', 'c']

del c[1]
print(c)

# 리스트함수

y = [5,2,3,1,4]
y.append(6) # 리스트 자체추가
y.sort() #정렬
y.reverse()
y.insert(2,7)
x = [11, 22]
y.extend #원소로 넣어준다
y.remove()
y.pop() #맨마지막꺼내는거 LIFO

#튜플 (순서0 ,중복0 , 수정, 삭제) 중요데이터넣을떄 하는거

a= ()
b= (1, 100 , ('a','b', 'c'))

#튜플 함수
z= (5,2,1,3,4)

print(z)
print(3 in z)
print(z.index(5))
print(z.count(1))
