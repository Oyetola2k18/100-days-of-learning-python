#russian roulette but for bill payment

#str.spilt() fuuncion takes in an arguement( asign, punction mark or anything) , if the passed in arguement is found in the string, it prints out an array seperating each word in that string 
#e.g
#  essay = "My,name,is,moses"
# op = essay.split(",")
#then op is now a list ["My", "name", "is" , "Moses"]

#lets make use of that here
import random
names_string = input("Input everyone's names, Seperated by a comma and space\n")

name = names_string.split(", ")

random_person = random.randint(1,(len(name) - 1))
print(name)
print(f"{name[random_person]} is going to buy the meal today!")

#i could have used the choice function