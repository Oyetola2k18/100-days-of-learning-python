#Hangman game , first phase generating a random word
import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,len(word_list)-1)]

user_choice = input("Guess a letter:").lower()

for x in range(0,len(chosen_word)):
    if user_choice == chosen_word[x]:
        print("Exists")
    else:
        print("Does not exist")
