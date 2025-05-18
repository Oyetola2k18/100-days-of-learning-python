#learning about dictionaries in python(kind of like lists that have Key and values)
#syntax is - dictionary_name = {key:value,key:value,key:value}

programming_dictionary = {
    "Bug":"An errror in a program that prevents the program from runnning as expected",
    "Function":"A piece of code that you can easily call over and over again",
}

#to get item from the dictionary

print(programming_dictionary["Bug"])

#to append data into the dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)


#to create an empty dictionary

empty_dictionary = {}

#and to populate it 
empty_dictionary["w"]="word"


#to wipe a dictionary , we just have to declare the dictionary as empty again

empty_dictionary={}#now empty

#to edit an item in the dictionary
programming_dictionary["Bug"] = "An insect" #overwriting bug's real meaning in the dictionary
print(programming_dictionary) 

#how to loop through a dictionary 
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    #prints out the key and we use the key to print out the value at the key or position