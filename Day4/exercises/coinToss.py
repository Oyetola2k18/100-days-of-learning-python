#code to create a Virtual coin tosss program
import random

coin = random.randint(0,1)

if  coin == 1:
    print("Heads")
elif coin == 0:
    print("Tails")