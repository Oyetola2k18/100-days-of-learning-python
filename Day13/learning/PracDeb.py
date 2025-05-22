#practing debugging(fixing errors in our code)
############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):#bug here cuz range(1 to 20) runs the code 19 times , so the condition 
#     #condition for 20 doesnt get to run
#     if i == 20:
#       print("You got it")
# my_function()
#fixed
# def my_function():
#   for i in range(1, 20+1):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) #issue here is that code doesnt get to print the first index which is 0(zero)
#and also 6 is out of bound

#fix
dice_num = randint(0, 5)

print(dice_imgs[dice_num])

