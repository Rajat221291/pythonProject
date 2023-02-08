import random
import emoji


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def score_calculator(cards):
    if sum(cards) ==21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(userscore,computerscore):
    if userscore == computerscore:
        return "Draw "
    elif computerscore == 0:
        return "Lose, Opponent has blackjack"
    elif userscore == 0:
        return "Win with a Blackjack"
    elif userscore > 21:
        return "You went over, you lose"
    elif computerscore > 21:
        return "Opponent went over. You win"
    elif userscore > computerscore:
        return "You win"
    else:
        return "You lose"
def play_game():
    user_card=[]
    computer_card=[]
    is_gameover=False


    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())



    while not is_gameover :
        user_score = score_calculator(user_card)
        computer_score = score_calculator(computer_card)
        print(f" Your cards: {user_card},current score: {user_score}")
        print(f" Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score ==0 or user_score >21:
            is_gameover =True
        else:
            another_card=input("Do you want to draw another card? type 'y' for yes and 'n' for no: ")
            if another_card == 'y':
                user_card.append(deal_card())
            else :
                is_gameover = True
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameover = True
    while computer_score !=0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score=score_calculator(computer_card)

    print(f" Your final hand: {user_card}, final score: {user_score}")
    print(f" Computer's final hand:{ computer_card},final score: {computer_score}")
    print(compare_score(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()



