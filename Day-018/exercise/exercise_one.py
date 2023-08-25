import turtle as t
import random
tim = t.Turtle()

colors = ['misty rose', 'medium sea green', 'medium turquoise', 'green yellow', 'yellow', 'dark slate blue']

num_sides = 5

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/ num_sides
        tim.forward(100)
        tim.left(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)