#learnt about the count function and the lower() function
#My own approach
# print("Welcome to the Love calculator")
# name1 = input("What is your name?\n")
# name2 = input("What is their name?\n")

# main1= name1.lower()
# main2 = name2.lower()

# text_combined = main1 + main2

# rate1 = text_combined.count("t") + text_combined.count("r") + text_combined.count("u") + text_combined.count("e")
# rate2 = text_combined.count("l") + text_combined.count("o") + text_combined.count("v") + text_combined.count("e")

# result = str(rate1) + str(rate2)
# if (int(result)< 10 or int(result)>90):
#     print(f"Your Score is {result}% , you go together like coke and mentos")
# elif (int(result)>= 40 and int(result)<= 50):
#     print(f"Your Score is {result}% , you are alright together")
# else:
#     print(f"your score is {result}%")

#angela's approach

print("Welcome to the Love calculator")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combined_string = name1 + name2

lowercase_string = combined_string.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l =  lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e

final_rate = str(true)+str(love)

if (int(final_rate)< 10 or int(final_rate)>90):
    print(f"Your Score is {final_rate}% , you go together like coke and mentos")
elif (int(final_rate)>= 40 and int(final_rate)<= 50):
    print(f"Your Score is {final_rate}% , you are alright together")
else:
    print(f"your score is {final_rate}%")

 
