#this is a blindn function program
# from replit import clear
#approach 1

from blin_auction import logo

print(logo)
print("Welcome to the secret auction program")
bidders = {}


end_of_program = False
bidders = {
    "name":[],
    "bid":[]
}

while end_of_program == False:
    name = input("What is your name?: ")
    bid = float(input("How much are bidding?: $"))
    

    bidders["name"].append(name)
    bidders["bid"].append(bid)


    choice = input("Are the any other bidders: 'yes' for Yes , 'no' for No?").lower()
    if choice == 'no':
        end_of_program = True

Highest=max(bidders["bid"])
index = bidders["bid"].index(Highest)
Highest_person = bidders["name"][index]

print(f"The WINNER IS {Highest_person} with a bid of {Highest}")
