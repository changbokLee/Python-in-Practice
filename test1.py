# score = int(input("성적을 입력하시오:"))

# if score>=60:
#     print("합격입니다.")
# else:
#     print("불합격입니다")

# num = int(input("성적을 입력하시오:"))

# if num % 2 == 0:
#     print("짝수입니다")

# else:
#      print("홀수입니다")


# age = int(input("나이입력"))

# if age >=20:
#     print("영화가능")

# else:
#     print("영화불가능")

# age = int(input("나이입력"))

# if age > =15:
#     print("영화가능")
# while True:
#     score = int(input("점수를입력하세요"))

#     if (score >=95):
#         print("A+")
#     elif ( 90< score  & score < 95):
#         print("A") 
#     elif (score >=85 & score < 90):
#         print("B+") 
#     elif (score >=60 & score < 85 ):
#         print("B") 
#     else:
#         print("F")   

# import turtle

# t = turtle.Turtle()

# for count in range(6):
#     t.circle(100)
#     t.left(360/6)

# import turtle
# t = turtle.Turtle
# t.shape("turtle")

# n = 60
# t.shape("turtle")
# t.speed('fastest')
# for i  in range(n):
#     t.circle(120)
#     t.right(360/ n)

# import turtle
# import random
# t = turtle.Turtle()
# t.shape("turtle")
# t.shapesize(2,2)


# for i in range(30):
#     length = random.randint(300, 300)
#     t.forward(length)
#     angle = random.randint(-180, 180)
#     t.right(angle)

# dan = int(input("원하는 단은:"))
# i = 1

# while i <= 9:
#     print("%s %s =%s" % (dan , i, (dan*i))
#     i  = i +1

import turtle
t = turtle.Turtle

for a in range(1,9):
    print("======", end ="\t")
print("")

for i in range(1,10):
    print(" &d단" "% i ", end ="\t")
print("")

for c in range(1,9):
    print("==========" , end = "\t")

for i in range(1,10):
    for j in range(2,10):
        print("%d * %d = %d" % (i,j, i*j), end=("\t"))
    print("")