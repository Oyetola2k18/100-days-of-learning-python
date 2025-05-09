#fstrings: help making programmer life easy , it doest allow the 
#return of error when we try to  print the concatenatination of  strings with 
#other data types like integers and floating point numbers

score = 0
height = 1.8
isWinning = True
#fstring: sysntax, add f to the front of the string and
#  add the stuff you want to refer in squigly brackets

print(f"your score is {score}, your height is {height}, and win status: {isWinning}")

#instead of 
# print("your score is  " + str(score) + "your height is "+ str(height) +"Win status is :" + str(isWinning))