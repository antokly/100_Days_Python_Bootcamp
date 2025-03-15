# # Lesson examples file 

# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen # from module import class or function

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight) #300
# my_screen.exitonclick()

from prettytable import PrettyTable # import PrettyTable Class

table = PrettyTable() # Create a PrrettyTable object and store it in a variable called table
table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander", "Fire"])

table.align = "l"

print(table)
