#nested if statements & introduction of elif
#also learning about multiple if statements
#also learning about logical operators
bill = 0
print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?"))


if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age"))
    if age >= 45 and age <= 55:
        bill = 0
    elif age < 12:
        bill +=5
    elif age <= 18:
        bill +=7
    else:
        bill +=12
    
    wants_photo=input("DO you want to take a photo(Y or N)")
    if  wants_photo == "Y":
        bill += 3
    
    print(f"The Amount you are meant to pay is ${bill}")
   
else:
    print("Sorry you have to grow taller before you can ride")
