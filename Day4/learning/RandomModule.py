#learning how to use the random module
#to use random module ,you have to import it

import random

random_integer = random.randint(1,10)#retruns a random integer ranges from 1 to 10(including 1 and  10)

random_float = random.random() #returns a random floating point number from 0.0 to 1.0 (not includeing 0.1 and 1.0)
#if we want to specify a range by which we want our random floating point number should start and end
#we do that by muliplying our random float by the number you want it to range to 
# eg random_float = random.random() * 5 ( random numbers from  0.0000000.......... to 4.9999999999999999)

print(random_float)

#if we go back to day3 ,we worked on a project like slove calculator
# we can randoize like this love_score = random.randint(1,100)