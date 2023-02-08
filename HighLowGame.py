import random
from Data.game_data import data
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def select_data():
    """Select random data"""
    return random.choice(data)

def format_data(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess,followers_a,followers_b):
    if followers_a > followers_b:
        return  guess=="a"
    else:
        return  guess=="b"

def game():
    score=0
    continue_play=True
    choice2 = select_data()

    while continue_play:
        choice1 = choice2
        choice2 = select_data()

        while choice1 == choice2:
            choice2 = select_data()

        follower_a = choice1["follower_count"]
        follower_b = choice2["follower_count"]
        print(logo)
        print(f"Compare A: {format_data(choice1)}")
        print(vs)
        print(f"Against B: {format_data(choice2)}")

        user_guess=input("Who has more followers? Type 'A' or 'B': ").lower()
        computer_choice=check_answer(user_guess,follower_a,follower_b)
        if computer_choice:

            score +=1
            print(f"Thats right ,your score is {score}")
        else:

            continue_play =False
            print(f"Sorry, that's wrong. Final score: {score}")


game()






