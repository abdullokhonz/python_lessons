import turtle
import random

trtl = turtle.Turtle()
window = turtle.Screen()

trtl.speed(0)
trtl.hideturtle()
trtl.color('red')
trtl.width(5)
trtl.up()
trtl.goto(300, -300)
trtl.down()
trtl.goto(300, 300)
trtl.goto(-300, 300)
trtl.goto(-300, -300)

desk = turtle.Turtle()
desk_speed = 500
desk.speed(0)
desk.color('red')
desk.shape('square')
desk.shapesize(1, 4)
desk.up()
desk.goto(0, -290)
desk.down()


def move_right():
    desk_x, desk_y = desk.position()
    desk.setposition(desk_x + desk_speed, desk_y)


def move_left():
    desk_x, desk_y = desk.position()
    desk.setposition(desk_x - desk_speed, desk_y)


window.onkey(move_right, 'Right')
window.onkey(move_left, 'Left')


def move_desk(click_x, click_y):
    desk.up()
    desk_x, desk_y = desk.position()
    desk.setposition(click_x, desk_y)


window.onclick(move_desk)

ball = turtle.Turtle()
ball.shape('circle')
x = random.randint(-299, 299)
y = random.randint(-299, 299)
ball.speed(0)
ball.up()
ball.setposition(x, y)
ball.speed(None)
x_speed = 3
y_speed = 4
while True:
    desk_x, desk_y = desk.position()
    x, y = ball.position()
    ball.setposition(x + x_speed, y + y_speed)
    if x + x_speed >= 300 or x + x_speed <= -300:
        x_speed = -x_speed
    elif y + y_speed >= 300 or y <= desk_y + 5 and x <= desk_x:
        y_speed = -y_speed
    elif y + y_speed <= -290:
        break

window.mainloop()
