import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color {colors}: ").lower()
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for x in range(0, len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-240, y= y_positions[x])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! This {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()