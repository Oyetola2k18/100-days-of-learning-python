#learning about lists in python (they are kind of like arrays)
#lists are useed to store elememts that have same relationship under one variable 
#Systax is group_name = [value1, value2, value3...]

states_of_nigeria = ["Ogun", "Osun"]

print(states_of_nigeria[1])

#if we use negatiive values to refer to our lists , it starts from the end

#also we can change items on the list

states_of_nigeria[1]="Ondo"

#i changed osun to ondo

print(states_of_nigeria[1])

#print(states_of_nigeria) to print all elemments in the states of nigeria list

#if we want to add another item to the list ,we use the append() function

states_of_nigeria.append("Osogbo")

#to add a whole list of item to the list, we use the extend() function

states_of_nigeria.extend(["Kwara","Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa"])
#that line of code adds this list to the oreexisting list(basically appending a whole lot of values at once)

print(states_of_nigeria)