import turtle
import prettytable

# phil = turtle.Turtle()
# phil.color("green")
# phil.shape("turtle")
# phil.forward(20)
# phil.forward(100)
# my_screen = turtle.Screen()
#
# my_screen.exitonclick()

my_table = prettytable.PrettyTable()
my_table.add_column("Pokimon Name", ["Pichachoo", "Charmander", "Squirtle"])
my_table.add_column("Type", ["Electric", "Charming", "Squirter"])
print(my_table)