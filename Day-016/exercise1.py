# import another_moudel
# print(another_moudel.another_variable)

# from turtle import Turtle, Screen
# Jason = Turtle()
# print(Jason)
# Jason.shape("turtle")
# Jason.color("DarkSlateGray1")
# Jason.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#https://pokemondb.net/pokedex/game/x-y
#https://pypi.org/project/prettytable/
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)
