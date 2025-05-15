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

# chosen_word = word_list[random.randint(0,len(word_list)-1)]
#clean 
chosen_word = random.choice(word_list)

#testing code
print(f"THe chosen word is {chosen_word}")

lives = 6
display = []
for letter in chosen_word:
    display+="_"

end_of_game = False

print(stages[lives])
while not end_of_game:

    user_choice = input("Guess a letter:").lower()

    for x in range(0,len(chosen_word)):
        if user_choice == chosen_word[x]:
            display[x]= user_choice

    if user_choice not in chosen_word:
        lives -= 1 
        print("Wrong")
        print(stages[lives])   
        if lives == 0:
            print("Game over, you lose")
            end_of_game = True



    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")