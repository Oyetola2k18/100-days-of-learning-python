#code to create a numnber guessing game
import random
from art import logo
Lives = 0
def hard():
    global Lives
    Lives = 5

def easy():
    global Lives
    Lives = 10

print(logo)
print("WELCOME TO THE NUMBER GUESSING GAME!")

computer_choice = random.randint(1,100)
#testing code
print(computer_choice)
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard:").lower()

if difficulty == 'easy':
    easy()
elif difficulty == 'hard':
    hard()

print(f"You have '{Lives} lives'")
while Lives>0:
    user_choice = int(input("Make a guess:"))
    if user_choice > computer_choice:
        print("Too High")
        Lives-=1
        print(f"You have{Lives} left")
    elif user_choice < computer_choice:
        print("Too Low")
        Lives-=1
        print(f"You have{Lives} left")
    elif user_choice == computer_choice:
        print(f"YOu got it ,The answer was {computer_choice}")
        Lives = 0#just to break out of code

