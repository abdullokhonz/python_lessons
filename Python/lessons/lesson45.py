from time import sleep
from turtle import *

trtl = Turtle()


# trtl.hideturtle()
#
# trtl.showturtle()
#
# trtl.forward(100)
# trtl.right(90)
#
# trtl.forward(100)
# trtl.right(90)
#
# trtl.forward(100)
# trtl.right(90)
#
# trtl.forward(100)
# trtl.right(90)
#
# trtl.right(45)
# trtl.forward(140)
#
# trtl.left(135)
# trtl.forward(100)
#
# trtl.left(135)
# trtl.forward(140)

# trtl.circle(45)

def square(px):
    trtl.hideturtle()
    for _ in range(4):
        trtl.forward(px)
        trtl.left(90)


# for i in range(1, 10):
#     trtl.speed(i)
#     square(i * 10)

# sleep(1)

# trtl.forward(100)
# trtl.left(120)
# trtl.forward(100)
# trtl.left(120)
# trtl.forward(100)

def mnogougolnik(n: int, px: int, clr: str):
    trtl.hideturtle()
    sum_angle = (n - 2) * 180
    angle = sum_angle // n
    for _ in range(n):
        trtl.color(clr)
        trtl.forward(px)
        trtl.left(180 - angle)


colors = ['black', 'red', 'yellow', 'green', 'purple', 'orange', 'brown', 'pink', 'blue', 'white']
bg_colors = colors.copy()
bg_colors.reverse()

# for i in range(3, 10):
#     mnogougolnik(i, 50, colors[i - 3])

# trtl.speed(100)
# pixel = 1
# for i in range(1, 100):
#     bgcolor(bg_colors[i % 10])
#     trtl.color(colors[i % 10])
#     trtl.left(20)
#     square(pixel)
#     pixel += 10


def star(n: int, px: int):
    if n % 2 != 0:
        angle = (n // 2) * 360 / n
        for _ in range(n):
            trtl.forward(px)
            trtl.left(angle)


# trtl.write('Abdullo', move=True, font=('sans-serif', 50, 'bold'))

sleep(1)
