#the third iteration of the project
#Hangman game , third phase
import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,len(word_list)-1)]

#testing code
print(f"THe chosen word is {chosen_word}")

display = []

while display.count("_") <=0:
    user_choice = input("Guess a letter:").lower()
    #this holds the list  of _
    #this loop is to add as much "_" in the letters of the word
    for letter in chosen_word:
        display+="_"

    #this is the loop to assign the users choice to the display if it exists
    for x in range(0,len(chosen_word)):
        if user_choice == chosen_word[x]:
            display[x]= user_choice


print(display)