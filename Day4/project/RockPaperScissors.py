#RPS games
import random


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
paper = '''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

selection = int(input("What do you want to input (0 for Rock,1 for paper, 2 for scissors)\n"))
print("You Chose:")
if selection == 0:
    print(rock)
elif selection == 1:
    print(paper)
elif selection==2:
    print(scissors)
else:
    print("Invalid Input")
    exit()


robot_select = random.randint(0,2)
print("Computer Chose: ")
if robot_select == 0:
    print(rock)
elif robot_select == 1:
    print(paper)
elif robot_select==2:
    print(scissors)
else:
    print("Invalid Input")
    exit()

#RUles check
if selection == 0 and robot_select == 0:
    print("Draw")
elif selection == 0 and robot_select == 1:
    print("Paper wins")
    print("You lose")
elif selection == 0 and robot_select == 2:
    print("Rock wins")
    print("You win")

if selection == 1 and robot_select == 1:
    print("Draw")
elif selection == 1 and robot_select == 0:
    print("Paper wins")
    print("You win")
elif selection == 1 and robot_select == 2:
    print("Scissors wins")
    print("You lose")

if selection == 2 and robot_select == 2:
    print(" Draw")
elif selection == 2 and robot_select == 0:
    print("Rock wins")
    print("You lose")
elif selection == 2 and robot_select == 1:
    print("Scissors wins")
    print("You win")
