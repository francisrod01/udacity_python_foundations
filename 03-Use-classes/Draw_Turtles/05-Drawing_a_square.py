#!~/envs/udacity-python-env

import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    bad = turtle.Turtle()
    bad.forward(100)

    window.exitonclick()


draw_square()
