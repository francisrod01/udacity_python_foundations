#!~/envs/udacity-python-env

import turtle


def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(0, 4):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)


def draw_triangle():
    angle = turtle.Turtle()
    angle.shape("arrow")

    for i in range(0, 3):
        angle.forward(60)
        angle.left(120)


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()

    draw_circle()

    draw_triangle()

    window.exitonclick()


draw_shapes()
