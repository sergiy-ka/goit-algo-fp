import turtle
import math


def pifagor_tree(x, y, l, angle, n):
    k = 0.7

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x1 = x + l * math.cos(math.radians(angle))
    y1 = y + l * math.sin(math.radians(angle))
    turtle.goto(x1, y1)

    if n <= 1:
        return

    pifagor_tree(x1, y1, k*l, angle+45, n-1)
    pifagor_tree(x1, y1, k*l, angle-45, n-1)


def draw_pifagor_tree(x=0, y=-200, l=100, angle=90):
    turtle.speed(2)
    turtle.bgcolor("white")
    turtle.pen(fillcolor="black", pencolor="red", pensize=2)
    turtle.title("Дерево Піфагора")
    turtle.showturtle()
    n = turtle.numinput("Рівень рекурсії", "Введіть рівень рекурсії:", 8)
    pifagor_tree(x, y, l, angle, n)
    turtle.exitonclick()
