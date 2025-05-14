#Hangman game , second phase generating a
#Angela way
import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,len(word_list)-1)]

#testing code
print(f"THe chosen word is {chosen_word}")


display = []
for letter in chosen_word:
    display+="_"

end_of_game = False
while not end_of_game:

    user_choice = input("Guess a letter:").lower()

    for x in range(0,len(chosen_word)):
        if user_choice == chosen_word[x]:
            display[x]= user_choice

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")





#the third iteration of the project
#Hangman game , third phase
#my way
# import random
# word_list = ["ardvark", "baboon", "camel"]

# chosen_word = word_list[random.randint(0,len(word_list)-1)]
# print(f"THe chosen word is {chosen_word}")

# user_choice = input("Guess a letter:").lower()
# display=[]
# for letter in chosen_word:
#     display+="_"
    
# #this is the loop to assign the users choice to the display if it exists
# for x in range(0,len(chosen_word)):
#     if user_choice == chosen_word[x]:
#         display[x]= user_choice
# print(display)
# while display.count("_") > 0:
#     user_choice = input("Guess a letter:").lower()
#     for x in range(0,len(chosen_word)):
#         if user_choice == chosen_word[x]:
#             display[x]= user_choice
#     print(display)

#     if not "_" in display:
#         print("YOu win")
#         exit()