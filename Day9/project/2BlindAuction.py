#this is a blindn function program
# from replit import clear
#approach 2

from blin_auction import logo

print(logo)
print("Welcome to the secret auction program")
bidders = {}
def check_highest(the_Auction_log):
    highest_bid = 0
    winner=""#this variables stores the winner (key)at the value that has the higest number
    for key in the_Auction_log:
        bid_amount = the_Auction_log[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

end_of_program = False

while end_of_program == False:
    name = input("What is your name?: ")
    bid = float(input("How much are bidding?: $"))
    

    bidders[name]=bid

    choice = input("Are the any other bidders: 'yes' for Yes , 'no' for No?").lower()
    if choice == 'no':
        end_of_program = True
        check_highest(bidders)