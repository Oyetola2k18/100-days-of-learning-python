#bill + tax calculator

#learnt about the format specifier and a littleabout the format function
#{:.2f},format(var_name)will format the value passed into the function and returns the answer in 2 decimal places
print("Welcome to the tip calculator")
total_bill = input("What is the total of the bill?$")
percentage = input("WHat would tip would you like to give? 10, 12 or 15?")
split_people = input("How many people to split the bill?")
percentage_to_float= float(percentage)
total_bill_toFloat =float(total_bill) 

final_pay = total_bill_toFloat + ((percentage_to_float /100)* total_bill_toFloat)
perPerson = final_pay / int(split_people)
result = round(perPerson,2)
result = "{:.2f}".format(perPerson)
print(f"Each person should pay: ${result}") 