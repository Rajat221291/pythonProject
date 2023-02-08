
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
# TODO:  Create dictionary for resources and menu
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    '''This function will calculate total value of coins'''
    print("Please insert coins. ")
    total=int(input("How many quarters? ")) * 0.25
    total+=int(input("How many dimes? ")) * 0.1
    total+=int(input("How many nickles? ")) * 0.05
    total+=int(input("How many pennies? ")) * 0.01

    return total



def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def transaction(total,cost):

    if total >= cost:
        global profit
        profit +=cost
        change=round(total -cost,2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough Money.Money refunded. ")
        return False

def update_resources(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name} ☕☕")

def make_coffee():
    is_cofeemc_on = True
    while is_cofeemc_on:
      user_choice=input("what would you like (espresso/latte/cappuccino): ").lower()
      if user_choice == "report":
          print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: ${profit}")
      elif user_choice == "off":
          is_cofeemc_on = False
      else:
          drink=MENU[user_choice]
          if check_resources(drink["ingredients"]):
              total_coins=process_coins()
              if transaction(total_coins,drink["cost"]):
                  update_resources(user_choice,drink["ingredients"])


make_coffee()

