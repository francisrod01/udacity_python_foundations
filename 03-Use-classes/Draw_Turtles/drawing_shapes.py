#!~/envs/udacity-python-env

import turtle


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("blue")

    flower = turtle.Turtle()
    flower.speed(100)
    flower.shape("arrow")
    flower.right(45)

    for i in range(1, 37):
        for j in range(1, 5):
            draw_circle(flower, i, "green")
            flower.left(90)

    flower.right(45)
    flower.color("green")
    flower.forward(200)

    window.exitonclick()


def draw_circle(circle, radius, color):
    circle.color(color)
    circle.circle(radius)


draw_shapes()
