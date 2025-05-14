#At our 4th iteration, designing ascii arts
import random
#ascii arts

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = word_list[random.randint(0,len(word_list)-1)]

#testing code
print(f"THe chosen word is {chosen_word}")


display = []
for letter in chosen_word:
    display+="_"

lives = 6
end_of_game = False
while not end_of_game:

    user_choice = input("Guess a letter:").lower()

    for x in range(0,len(chosen_word)):
        if user_choice == chosen_word[x]:
            display[x]= user_choice
        else:
            for stage in stages:
                print (stages[lives])
                break
            lives-=1


    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")