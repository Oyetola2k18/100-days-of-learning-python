#Making use of the pretty table module

from prettytable import PrettyTable

table = PrettyTable()
#saving the PrettTable class to a variable named table(process of creating an object)

#the pretty table function has a function called add_column(), its take in a data (which serves as the columnn name / header)
# and another arguement which is a list( an it puts does list as the data that belongs under that column's header name
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])
table.align = "l"
print(table)