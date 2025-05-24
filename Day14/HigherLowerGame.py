#Higher lower game
from data import data
import random
from replit import clear
from art import logo,vs
def generate_people():
    """Returns Name,Follower count snd other info about the Celebrity"""
    return random.choice(data)

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

print(logo)
Score = 0

info,count = person()

end_game = False
while not end_game:
    info2,count2 = person()
    print(f"Compare A:{info}")
    #testing code
    # print(count)
    print(vs)
    print(f"Compare B:{info2}")
    #testing code
    # print(count2)
    choice = input("Who has more followers? Type 'A' or 'B':").lower()
    highest_value = compare(count,count2)

    #testing code 
    # print(highest_value)

    if choice == 'a':
        if count == highest_value:
            Score+=1
            clear()
            print(f"YOu are Right! Current score: {Score}")
            info = info2
            count = count2
            print(logo)
        else:
            print(f"You lose, Game Over: YOur total score is {Score}")
            end_game = True
    elif choice == 'b':
        if count2 == highest_value:
            Score+=1
            clear()
            print(f"YOu are Right! Current score: {Score}")
            info = info2
            count = count2
           
            print(logo)
        else:
            print(f"You lose, Game Over: YOur total score is {Score}")
            end_game = True
    else:
        end_game = True