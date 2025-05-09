#pizza order system 

print("Welcome to python pizza deliveries! ")
size = input("What size of pizza do you want?S,M , L")
add_pepperoni = input("Do you want pepperoni?Y or N")
extra_chess = input("DO you want extra cheese ? Y or N")

Bill =0

if size == "S":
    Bill += 15
    if add_pepperoni == "Y":
        Bill+=2   
elif size == "M":
    Bill += 20
    if add_pepperoni == "Y":
        Bill+=3
elif size == "L":
    Bill+=25
    if add_pepperoni == "Y":
        Bill+=3

if extra_chess == "Y":
    Bill+=1

print(f"Your Final Bill is ${Bill}") 