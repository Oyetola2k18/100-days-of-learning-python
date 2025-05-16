#code to check if a number is prime or not
#prime number is a number that is only divisible by 1 and itself
import math

#i and chat-gpt's approach
# def prime_checker(number):
#     #base cases
#     if number == 2:
#         print("it is a prime number")
#     elif number < 2 or number % 2 == 0:
#         print("It is not a prime number")
#     else:
#         for x in range(3,int(math.sqrt(number))+1):
#             if number % x == 0:
#                 print("It is not a prime number")
#                 return
#         print("It is a prime number")

#Angela and i's approach 
def prime_checker(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

#testing
test_numbers = [2]
# n = int(input("Check this number: "))
for n in test_numbers:
    prime_checker(number = n)