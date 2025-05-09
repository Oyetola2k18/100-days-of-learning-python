#version 2 of the BMI calculator
height = float(input("ENTER YOUR HEIGHT IN M: "))
weight = float(input("Enter the Weight in kg: "))

bmi = round(weight / (height**2))


if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are Underweoight")
elif bmi < 25:
    print(f"Your BMI is {bmi}, You have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, You are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, You are obese")
elif bmi >= 35:
    print(f"Your BMI is {bmi}, You are clinically obese")