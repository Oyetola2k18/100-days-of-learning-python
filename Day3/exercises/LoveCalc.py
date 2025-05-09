#learnt about the count function and the lower() function

print("Welcome to the Love calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

main1= name1.lower()
main2 = name2.lower()

text_combined = main1 + main2

rate1 = text_combined.count("t") + text_combined.count("r") + text_combined.count("u") + text_combined.count("e")
rate2 = text_combined.count("l") + text_combined.count("o") + text_combined.count("v") + text_combined.count("e")

result = str(rate1) + str(rate2)
if (int(result)< 10 or int(result)>90):
    print(f"Your Score is {result}% , you go together like coke and mentos")
elif (int(result)>= 40 and int(result)<= 50):
    print(f"Your Score is {result}% , you are alright together")
else:
    print(f"your score is {result}%")
 
