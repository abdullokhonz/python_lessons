import turtle

trtl = turtle.Turtle()
window = turtle.Screen()
speed = 10


def move_up():
    x, y = trtl.position()
    trtl.setposition(x, y + speed)


def move_down():
    x, y = trtl.position()
    trtl.setposition(x, y - speed)


def move_left():
    x, y = trtl.position()
    trtl.setposition(x - speed, y)


def move_right():
    x, y = trtl.position()
    trtl.setposition(x + speed, y)


def hide_trtl():
    if trtl.isvisible():
        trtl.hideturtle()
    else:
        trtl.showturtle()


def speed_1():
    global speed
    speed = 1


window.onkey(move_up, 'Up')
window.onkey(move_down, 'Down')
window.onkey(move_left, 'Left')
window.onkey(move_right, 'Right')
window.onkey(hide_trtl, 'space')
window.onkey(speed_1, '1')

window.listen()
window.mainloop()

print(trtl.position())

# _____________________________________________________

# import turtle, random
#
# trtl = turtle.Turtle()
# window = turtle.Screen()
#
# # Блок отвечающий за барьер
# trtl.speed(0)
# trtl.hideturtle()
# trtl.color('red')
# trtl.width(5)
# trtl.up()
# trtl.goto(300, 300)
# trtl.down()
# trtl.goto(300, -300)
# trtl.goto(-300, -300)
# trtl.goto(-300, 300)
# trtl.goto(300, 300)
#
# # Блок отвечающий за мяч
# ball = turtle.Turtle()
# ball.shape('circle')
# x = random.randint(-299, 299)
# y = random.randint(-299, 299)
# ball.speed(0)
# ball.up()
# ball.setposition(x, y)
# ball.speed(None)
# x_speed = 3
# y_speed = 4
# while True:
#     x, y = ball.position()
#     ball.setposition(x + x_speed, y + y_speed)
#     if x + x_speed >= 300 or x + x_speed <= -300:
#         x_speed = -x_speed
#     elif y + y_speed >= 300 or y + y_speed <= -300:
#         y_speed = -y_speed
#
# window.mainloop()

# ______________________________________________________________________-
