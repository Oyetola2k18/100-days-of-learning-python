#BLACK JACK GAME
# ############### Our Blackjack House Rules #####################
# The deck is unlimited in size. There are no jokers. The Jack/Queen/King all count as 10. The the Ace can count as 11 or 1. Use the following list as the deck of cards: 
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] The cards in the list have equal probability of being drawn. Cards are not removed from the deck as they are drawn. 
# The computer is the dealer.
import random
from art import logo
import replit
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)

def calculate_score(list):
    if len(list)==2 and 11 in list and 10 in list:
        return 0
    
    if 11 in list and sum(list)>21:
        index = list.index(11)
        list[index] = 1

    return sum(list)

def compare(user_score,cpu_score):
    scores = [user_score,cpu_score]
    if user_score == cpu_score:
        return 'Draw'
    elif user_score ==  0:
        return "You win with a blackjack"
    elif cpu_score == 0:
        return "You lose,Cpu Wins with BlackJack"
    elif user_score > 21:
        return "You went over, you lose"
    elif cpu_score > 21:
        return "You win,Cpu lost"
    else:
        if  max(scores) == scores[0]:
            return "You win"
        elif max(scores) == scores[1]:
            return "Cpu wins"
def blackJack():
    cpu =[]
    user=[]
    print(logo)
    for x in range(2):
        cpu.append(deal_card())
        user.append(deal_card())
    is_game_over = False
    while is_game_over == False: 
        cpu_score=calculate_score(cpu)
        user_score=calculate_score(user)
        print(f"You:{user}  Total:{user_score}")
        print(f"Ai:{cpu[0]}")
        
        if cpu_score == 0 or user_score == 0 or user_score >21:
            print("End of Game")
            is_game_over =True
        else:
            user_continue_deal = input("DO you want to draw another card?'Y' for yes 'N' for no :").lower()
            if user_continue_deal == 'y':
                user.append(deal_card())
                print(user)
            else:
                print("End of Game")
                is_game_over =True

    while cpu_score != 0 and cpu_score<17:
        cpu.append(deal_card())
        cpu_score=calculate_score(cpu)

    print(f"Your final hand is {user} Final score is : {user_score}")
    print(f"Computer's final hand is {cpu} Final score is : {cpu_score}")
    print(compare(user_score,cpu_score))

while input( "Do you want to play a game of black jack?'Y' for yes 'N' for no :").lower() == 'y':
    replit.clear()
    blackJack()
    






        

