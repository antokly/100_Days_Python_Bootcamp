import turtle # https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()  # instance to control window when we run our code

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)  # Counter-clockwise

def turn_right():
    tim.right(10)  # Clockwise

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# W to move forwards
screen.onkey(key="w", fun=move_forward)  # function as input : no need parentheses

# S to move backwards
screen.onkey(key="s", fun=move_backward)

# A to move Counter-Clockwise
screen.onkey(key="a", fun=turn_left)

# D to move Clockwise
screen.onkey(key="d", fun=turn_right)

# C to exit drawing
screen.onkey(key="c", fun=clear)

screen.listen()  # listener

screen.exitonclick()