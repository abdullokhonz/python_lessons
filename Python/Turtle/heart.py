import math
import turtle
import random


def hearta(k):
    return 15 * math.sin(k) ** 3


def heartb(k):
    return 12 * math.cos(k) - 5 * \
        math.cos(2 * k) - 2 * \
        math.cos(3 * k) - \
        math.cos(4 * k)


turtle.speed(0)
turtle.bgcolor("black")

colors = [
    "red",
    "green",
    "blue",
    "white",
    "pink",
    "orange",
    "purple",
    "brown"
]

for i in range(6000):
    turtle.goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(1):
        turtle.color(colors[random.randint(0, len(colors) - 1)])
    turtle.goto(0, 0)

turtle.done()
