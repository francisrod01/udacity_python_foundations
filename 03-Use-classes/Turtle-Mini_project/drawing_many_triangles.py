#!~/envs/udacity-python-env

# A contribution of Greg Bullmer to the Udacity discussion forum
# https://discussions.udacity.com/t/turtle-mini-project-f/16121/99?u=francisrod01

import turtle


def draw_triangle(the_turtle, level, dist):
    brad = the_turtle

    if level == 0:
        brad.down()
        brad.begin_fill()

        for _ in range(3):
            brad.forward(dist)
            brad.left(120)

        brad.end_fill()
        brad.up()
    else:

        for _ in range(3):
            draw_triangle(brad, level - 1, dist / 2)
            brad.forward(dist)
            brad.left(120)


def draw_art():
    # Create turtle's background
    background = turtle.Screen()
    background.screensize(300, 300, "gray")
    background.setworldcoordinates(0, 0, 300, 300)

    # Create a new turtle
    brad = turtle.Turtle()
    brad.speed(0)  # speed 1 to slow turtle down
    brad.color("blue", "green")
    brad.shape("turtle")

    draw_triangle(brad, 4, 300)

    background.exitonclick()


draw_art()
