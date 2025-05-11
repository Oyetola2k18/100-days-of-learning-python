#fizzbuzz, if divisible by 3 print fizz, if divisible by 5 print buzz, if divisible by both 3 and 5 print fizzbuzz


for n in range(1,100):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBizz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)