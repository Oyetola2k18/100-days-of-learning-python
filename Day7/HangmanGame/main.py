#final touches of the project 

import random
import words
import AsciiArts

# chosen_word = word_list[random.randint(0,len(word_list)-1)]
#clean 
print(AsciiArts.logo)
chosen_word = random.choice(words.word_list)

#testing code
# print(f"THe chosen word is {chosen_word}")

lives = 6
display = []
for letter in chosen_word:
    display+="_"

end_of_game = False

print(AsciiArts.stages[lives])
while not end_of_game:

    user_choice = input("Guess a letter:").lower()
    if user_choice in display:
        print(f"you chose this letter {user_choice} already")

    for x in range(0,len(chosen_word)):
        if user_choice == chosen_word[x]:
            display[x]= user_choice
    

    if user_choice not in chosen_word:
        lives -= 1 
        print(f"{user_choice} does not exists in the word(You lose a life)")
        print(AsciiArts.stages[lives])   
        if lives == 0:
            print("Game over, you lose")
            end_of_game = True



    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("You win")