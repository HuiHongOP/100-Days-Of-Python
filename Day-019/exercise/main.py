from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
screen.onkey(clear, 'c')

screen.exitonclick()