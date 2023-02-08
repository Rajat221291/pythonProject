import random
import supportingFile
from supportingFile import word_list
import math
def treasureMap():
    row1=[" "," "," "]
    row2=[" "," "," "]
    row3=[" "," "," "]
    map=[row1,row2,row3]
    print(f"{row1}\n{row2}\n{row3}")
    position= input("Where do you want to put the treasure? ")
    column=position[0]
    row=position[1]
    map[int(row) - 1][int(column) -1] = "X"

    print(f"{row1}\n{row2}\n{row3}")


def rockPaperScissorGame():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    user_choice=int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors. " ))
    options_list=[rock,paper,scissors]
    computer_choice=random.choice(options_list)
    if options_list[user_choice] == options_list[0] and computer_choice == options_list[2]:
        print(options_list[user_choice])
        print(computer_choice)
        print ("You won!!")
    elif options_list[user_choice] == options_list[2] and computer_choice == options_list[1]:
        print(options_list[user_choice])
        print(computer_choice)
        print( "You won !!!")
    elif options_list[user_choice] == options_list[1] and computer_choice == options_list[0]:
        print(options_list[user_choice])
        print(computer_choice)
        print( "You won !!!")
    elif options_list[user_choice] == computer_choice:
        print(options_list[user_choice])
        print(computer_choice)
        print("It's a Draw!!!")
    else:
        print(options_list[user_choice])
        print(computer_choice)
        print("you lose")


def passwordGenerator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    initial_password=[]
    final_password=""
    for i in range(0,nr_letters):
        initial_password.append(random.choice(letters))
    for j in range(0,nr_symbols):
        initial_password.append(random.choice(symbols))
    for k in range(0,nr_numbers):
        initial_password.append((random.choice(numbers)))

    print(initial_password)
#   for k in range(0,len(initial_password)):
#       j=initial_password.pop(random.randint(0,len(initial_password)-1))
#        final_password.append(j)
    random.shuffle(initial_password)
    # for char in initial_password:
    #    final_password +=char
    #print(final_password)
    print(''.join(initial_password))



def hangManChallenge():
    print(supportingFile.logo)
    stages=supportingFile.stages
    word_list=["ardvark","baboon","camel"]
    lives_left=len(stages) -1
    choosen_word=random.choice(word_list)
    print(choosen_word)
    display=[]
    word_length=len(choosen_word)
    for i in range(word_length):
        display += "_"
    print(display)
    end_of_game= False
    while not end_of_game:
        guess=input("Guess a letter: ").lower()
        if guess in display:
            print(f"you have already guessed the word {guess}")

        for position in range(word_length):
            letter = choosen_word[position]
            if letter == guess:
                display[position]= letter
        if guess not in choosen_word:
            print(f"You have guessed {guess}, that is not in word. You lose a life. ")
            lives_left -= 1
            if lives_left == 0:
                end_of_game = True
                print("You lose!!!")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game =True
            print("you win!!!")

        print(stages[lives_left])


def primeNumberChecker(number):
    is_prime= True
    if number ==1 :
        is_prime = False
    for i in range(2,number):
        if number %i == 0:
            is_prime = False
    if is_prime == True:
        print("It's a prime number")
    else:
        print("It's not a prime number")







def caesor_cipher():
    print(supportingFile.logo)
    rerun= True
    while rerun == True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']
        shift = shift % 26
        final_text=""
        if direction == "decode":
            shift *= -1
        for i in text:
            if i in alphabet:
                position= alphabet.index(i)
                new_position = position + shift
                final_text += alphabet[new_position]
            else:
                final_text +=i

        print(f"The {direction}d text is {final_text}")
        user_rerun = input("Do you want to rerun? ,type Y for yes and N for No:\n").lower()
        if user_rerun == "n":
            rerun = False
            print("Goodbye!!!")


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

travel_log=[
    {"country":"France",
     "cities_visited":["paris","france"],
    "total_visits":12},

    { "country":"Germany",
        "cities_visited":["Berlin","stuart"],
"total_visits":5}
            ]
def bid_calculator():
    more_bids=True
    print(supportingFile.logo1)
    bid_chart={}
    final_bid_value=0
    final_user=""
    while more_bids == True:
        name=input("Enter Name of bidder? ")
        bid=input("What is bid value? $")
        bid_chart[name]=bid

        user_choice=input("Are there any more bidders? Enter Y or N ").lower()
        if user_choice == "n":
            more_bids =False

    for user in bid_chart:
        value=bid_chart[user]
        if int(value) > final_bid_value:
            final_bid_value= int(value)
            final_user =user
    print(f"Highest bidder is {final_user} with bid of {final_bid_value} ")






