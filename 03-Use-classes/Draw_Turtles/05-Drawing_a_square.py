#!~/envs/udacity-python-env

import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")

    bad = turtle.Turtle()
    bad.shape("turtle")
    bad.speed(3)
    bad.color("yellow")

    bad.forward(100)
    bad.right(90)
    bad.forward(100)
    bad.right(90)
    bad.forward(100)
    bad.right(90)
    bad.forward(100)

    window.exitonclick()


draw_square()
