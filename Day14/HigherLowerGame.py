#Higher lower game
from data import data
import random
def generate_people():
    """Returns Name,Follower count snd other info about the Celebrity"""
    return data[random.randint(0,(len(data)-1))]

def person():
    celeb = generate_people()
    name = celeb["name"]
    follower_count = celeb['follower_count']
    description=celeb["description"]
    country=celeb["country"]
    def inner():
        return follower_count 
    return (f"{name},{description},from {country}"),inner

person1 = person()
