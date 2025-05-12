#pyPassword Generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your generator?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

#Easy version

# letters_rand = random.randint(0,51)
# numbers_rand = random.randint(0,9)
# symbols_rand = random.randint(0,8)

#loop for the letters
letters_in_pass = ""
for num in range(0,(num_of_letters)):
    letters_in_pass+=letters[random.randint(0,51)]

#loop for the symbols
symbols_in_pass = ""
for sym in range(0,num_of_symbols):
    symbols_in_pass += symbols[random.randint(0,8)]

#loop for the  numbers
numbers_in_pass = ""

for num in range(0,num_of_numbers):
    numbers_in_pass+=numbers[random.randint(0,9)]

encrypted_password  = letters_in_pass + symbols_in_pass + numbers_in_pass

print(f"Your encryted password is :{encrypted_password}")
