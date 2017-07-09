#!~/envs/udacity-python-env

import turtle


def draw_flower(some_turtle):
    for i in range(1, 3):
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("grey")

    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(20)

    brad.color("yellow")

    # Put draw of square in loop to draw a flower
    for i in range(0, 36):
        draw_flower(brad)
        brad.right(10)

    brad.setheading(270)
    brad.forward(400)

    window.exitonclick()


draw_art()
