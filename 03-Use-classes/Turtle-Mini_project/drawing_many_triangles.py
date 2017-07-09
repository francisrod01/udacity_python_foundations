#!~/envs/udacity-python-env

# A contribution of Thai Thien to the Udacity discussion forum
# https://discussions.udacity.com/t/turtle-mini-project-f/16121/8?u=francisrod01

import turtle


def draw_triangle(the_turtle, length, origin, recursion):
    recursion += 1
    brad = the_turtle

    for i in range(0, 3):
        if recursion < 4:
            brad.forward(length / 2)
            brad.left(120)
            draw_triangle(brad, length / 2, 0, recursion)
            brad.right(120)
            brad.forward(length / 2)
        else:
            brad.forward(length)

        if origin == 1:
            brad.left(120)
        else:
            brad.right(120)


def draw_art():
    brad = turtle.Turtle()
    brad.speed(10)  # speed 1 to slow turtle down
    brad.color("yellow", "green")
    brad.shape("turtle")

    # Create turtle's background
    background = turtle.Screen()
    background.bgcolor("grey")

    draw_triangle(brad, 200, 1, 0)

    background.exitonclick()


draw_art()
