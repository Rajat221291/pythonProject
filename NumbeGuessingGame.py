logo="""
  ________                               _______               ___.
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|
        \/            \/     \/     \/          \/            \/    \/     \/
"""
import random
print(logo)
EASY_ATTEMPT=10
HARD_ATTEMPT=5

def choose_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return  EASY_ATTEMPT
    else:
        return  HARD_ATTEMPT


def check_answer(turns,guess,answer):

    if guess > answer:
        print("Too High!!!")
        return turns -1
    elif guess < answer:
        print("Too Low!!!")
        return turns -1
    else:
        print("You guessed it right")

def game():
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer= random.randint(1, 100)
    turns=choose_level()
    guess=0
    while guess!=answer:
      
        print(f"you have {turns} attempts remaining to guess the number")
        guess=int(input("Guess a number: "))
        turns=check_answer(turns,guess,answer)
        if turns == 0:
            print("you are out of attempts, you lose")
            return
        elif answer!=answer:
            print("Guess again!!!")


game()




