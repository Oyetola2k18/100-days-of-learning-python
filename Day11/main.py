#BLACK JACK GAME
# ############### Our Blackjack House Rules #####################
# The deck is unlimited in size. There are no jokers. The Jack/Queen/King all count as 10. The the Ace can count as 11 or 1. Use the following list as the deck of cards: 
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] The cards in the list have equal probability of being drawn. Cards are not removed from the deck as they are drawn. 
# The computer is the dealer.
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_card =[]
player_card=[]
def deal_card():
    num = random.randint(0,len(cards))
    return cards[num]

def calculate_score(list):
    if list[0] == 11 and sum(list)>21:
        list[0] = 1
        return
    else:
        return sum(list)

def compare(list1,list2):
    if sum(list1 ) == sum(list2):
        print("Its a Draw")
        return

Start_game = input("Do you want to play BlackJack Game? 'Y' for yes 'N' for no :").lower()

if Start_game == 'y':
    print(logo)
    computer_card+=deal_card()
    player_card+=deal_card()


