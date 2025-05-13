#Hangman game , second phase generating a
import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,len(word_list)-1)]

#testing code
print(f"THe chosen word is {chosen_word}")

user_choice = input("Guess a letter:").lower()

display = []
for letter in chosen_word:
    display+="_"

for x in range(0,len(chosen_word)):
    if user_choice == chosen_word[x]:
        display[x]= user_choice

print(display)