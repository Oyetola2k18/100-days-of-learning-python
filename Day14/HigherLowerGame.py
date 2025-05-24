#Higher lower game
from data import data
import random
def generate_people():
    """Returns Name,Follower count snd other info about the Celebrity"""
    return data[random.randint(0,(len(data)-1))]

def compare(count1,count2):
    """Take in two values and returns the highest value"""
    return max(count1,count2)


def person():
    celeb = generate_people()
    name = celeb["name"]
    follower_count = celeb['follower_count']
    description=celeb["description"]
    country=celeb["country"]
    # def inner():
    #     return follower_count 
    info = (f"{name}, {description},from {country}")
    return info,follower_count
#learnt a new thing about the return keywork that it can return multiple values

info,count = person()
info2,count2 = person()
print(f"Compare A:{info}")
#testing code
print(count)
print(f"Compare A:{info2}")
#testing code
print(count2)
choice = input("Who has more followers? Type 'A' or 'B':").lower()
highest_value = compare(count,count2)

#testing code 
print(highest_value)

if choice == 'a':
    if count == highest_value:
        print("YOu are correct")
    else:
        print("You lose")
elif choice == 'b':
    if count2 == highest_value:
        print("YOu are correct")
    else:
        print("You lose")