#exercise 3
#code that takes age input and returns your age  in weeks month and days
#it returns how many days, weeks and month you have left to live if you lived till 90 years old

age = input("What is your age?\n")

age_as_int = int(age)

years_remaining = 90 - age_as_int

day_remaining =  years_remaining * 365

weeks_remaining = years_remaining* 52

months_remaining = years_remaining*12



print(f"You have {day_remaining} days left, {weeks_remaining} weeks, and {months_remaining}months left")