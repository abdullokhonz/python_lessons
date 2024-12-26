import turtle
import random

joe = turtle.Turtle()
joe.speed(1)

# joe.forward(100)
# joe.left(60)
# joe.forward(100)
# joe.left(30)
# joe.forward(100)

# joe.speed(10)
# joe.color('red')
# joe.forward(100)
# joe.left(90)
# joe.color('yellow')
# joe.forward(100)
# joe.left(90)
# joe.color('green')
# joe.forward(100)
# joe.left(90)
# joe.color('blue')
# joe.forward(100)
# joe.left(90)

# for i in range(4):
#     joe.speed(i)
#     joe.forward(100)
#     joe.left(90)

colorsss = ['red', 'brown', 'green', 'blue']


def sq(a):
    for i in range(4):
        # joe.color(colours[i % len(colours)])
        joe.color(colorsss[i % 4])
        joe.forward(a)
        joe.left(90)


dlina = 100
# for i in range(dlina, 0, -10):
#     sq(i)

# for i in range(10):
#     sq(i)
#     dlina += 20

colours = ['red', 'green', 'blue', 'yellow', 'gray', 'orange', 'pink', 'violet', 'gold', 'brown']
# new_start = 1
# new_finish = 100
# new_speed = 10
# random.shuffle(colours)
# for colors in colours:
#     for i in range(new_start, new_finish, new_speed):
#         joe.color(colors)
#         sq(i)
#     new_start += 10
#     new_finish += 20
#     new_speed += 1

# for j in range(4):
#     for i in range(100, 0, -1):
#         joe.circle(i, 90)
#         joe.left(90)
#         joe.circle(i, 90)
#         joe.left(90)
#         joe.color(random.choice(colours))
#     joe.left(90)

joe.circle(100, 60)
joe.left(60)
joe.circle(100, 60)
joe.left(60)
joe.circle(100, 60)
joe.left(60)

dlina = 30
# for i in range(60):
#     # joe.color(colours[i % len(colours)])
#     # joe.color(colorsss[i % 4])
#     sq(dlina)
#     joe.right(10)
#     dlina += 4

# for i in range(60):
#     joe.circle(dlina)
#     joe.right(10)
#     dlina += 4
