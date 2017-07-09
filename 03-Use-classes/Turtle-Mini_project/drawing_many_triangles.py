#!~/envs/udacity-python-env

import turtle


def draw_triangle(the_turtle, length, recursion):
    recursion += 1
    brad = the_turtle

    for i in range(0, 3):
        if recursion < 4:
            brad.forward(length / 2)
            brad.left(120)
            draw_triangle(brad, length / 2, recursion)


def draw_art():
    brad = turtle.Turtle()
    brad.speed(10)  # speed 1 to slow turtle down
    brad.color("yellow", "green")
    brad.shape("turtle")

    # Create turtle's background
    background = turtle.Screen()
    background.bgcolor("grey")

    draw_triangle(brad, 200, 0)

    background.exitonclick()


draw_art()
