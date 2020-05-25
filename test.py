# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# color_list = ["yellow", "red",  "blue" , "green"]

# t.fillcolor(color_list[0])
# t.begin_fill()
# t.circle(100)
# t.end_fill()


# t.forward(50)
# t.fillcolor(color_list[1])
# t.begin_fill()
# t.circle(100)
# t.end_fill()

# import turtle
# t =turtle.Turtle()
# t.shape("turtle")

# t.penup()
# t.goto(100, 100)
# t.write("거북이가 여기로오면 0")
# t.goto(100, - 100)
# t.write("거북이가 여기로오면 음수입니다")

# t.goto(0, 0 )
# t.pendown()
# s= turtle.textinput ("","숫자를 입력하시오")
# n =int(s)
# if( n >0):
#     t.goto(100, 100)
# if (n == 0):
#     t.goto(100, 0)
# if(n < 0):
#     t.goto(100, -100)

# import turtle

# t =turtle.Turtle()
# t.width(3)
# t.shape("turtle")
# t.shapesize(3,3)

# while True:
#     command = input ("명령을 입력하시오")
#     if command == "i":
#         t.left(90)
#         t.forward(100)
      

#     if command == "r":
#         t.right(90)
#         t.forward(100)


# import random

# print("동전던지기")
# coin = random.randrange(2)
# if coin == 0:
#     print("앞면")

# else:
#     print("뒷면")
# print("게임종료")


# import turtle
# import random

# screen  =  turtle.Screen()
# image1 = "front.gif"
# image2 = "back.gif"
# screen.addshape(image1)
# screen.addshape(image2)

# t1 = turtle.Turtle()
# coin = random.randint(0, 1)
# if coin == 0 :
#     t1.shape(image1)
#     t2.stamp()

# else: 
#     t1.shape(image2)
#     t1.stamp()   

# import random
# time = random.randint(1, 24)
# print("좋은아침입니다 .지금시각은 ." + str(time)+ "시입니다")

# sunny = random.choice([True, False])
# if sunny:
#     print("현재 날씨가 화창합니다")
# else:
#     print("현재 날씨가 화창하징않습니다")

# if(time >= 6) and (time < 9) and sunny:
#     print("종달새가 노래를한다.")
# else:
#     print("종달새가 노래를 하지않는다")

# id =" i love python"
# s = input("아이디를 입력하시오")
# if s == id:
#     print("환영합니다")

# else:
#     print("아이디를 찾을수없습니다")

import turtle
t = turtle.Turtle()
t.shape("turtle")

s =turtle.textinput("", "도형을입력하시오")
if s =="사각형":
    s = turtle.textinput("","가로:")
    w = int(s)
    s = turtle.textinput("","세로")
    h = int(s)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90) t.forward(h)