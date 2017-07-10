#!~/envs/udacity-python-env

import turtle


def draw_first_letter(the_turtle):
    brad = the_turtle

    # Drawing the first arrow
    brad.up()
    brad.setpos(270, -50)
    brad.down()
    brad.goto(270, -200)
    brad.setpos(270, -50)

    # Drawing the second arrow
    brad.up()
    brad.setpos(330, -50)
    brad.down()
    brad.goto(270, -130)
    brad.goto(340, -200)


def draw_second_letter(the_turtle):
    brad = the_turtle

    # Drawing the first arrow
    brad.up()
    brad.setpos(370, -50)
    brad.down()
    brad.goto(370, -200)
    brad.setpos(370, -50)

    # Drawing the second arrow
    brad.goto(470, -50)
    brad.setpos(370, -50)

    # Drawing the third arrow
    brad.goto(370, -50)
    brad.down()
    brad.goto(370, -200)
    brad.goto(470, -200)


def draw_initials():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(1)

    draw_first_letter(brad)
    draw_second_letter(brad)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    draw_initials()

    window.exitonclick()


draw_art()
