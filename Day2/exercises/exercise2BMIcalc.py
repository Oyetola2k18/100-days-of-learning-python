#BMI CLACULATOR

weight = input("input your weight in kg:\n")
height = input("Input your height in m:\n")

calc_weight = float(weight)
calc_height = float(height)

BMI = calc_weight/(calc_height ** 2)
conv_bmi = int(BMI)
print("The Body Mass index of the person is " + str(conv_bmi))