num = [1,2,3]

#this is how we perform list comprehenshion
# new_list = [n+1 for n in num]

#new_list = [newlist for item in list]
# print(new_list)

#WE Can also work with strings 

# name = "angela"
# new_list = [letter for letter in name]

# print(new_list)

# number = [2*x for x in range(1,5)]
# print(number)


#there are some that are also called conditional list comprehension
#taking list comprehension up a notch , we can also do that 
#new_list = [ new_list for item in list if test]
#new_list will only be added to the list if a certain condition is met

# even_number = [x for x in range(10) if x %2 == 0]
# print(even_number)

names = ["alex","beth", "caroline", "dave", "Eleanor", "freddie"]

# short_names = [name for name in names if len(name) <= 4]

upper_name = [name.upper() for name in names if len(name)>5]
print(upper_name)