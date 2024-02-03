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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = 0.0

def print_report():
    global RESOURCES
    global MONEY
    print(f"Water: {RESOURCES['water']}ml\nMilk: {RESOURCES['milk']}ml\nCoffee: {RESOURCES['coffee']}g\nMoney: ${MONEY}")


def check_resources(answer):
    global MENU
    global RESOURCES
    drink = MENU[answer]
    if drink['ingredients']['water'] > RESOURCES["water"]:
        print('Sorry there is not enough water')
    elif drink['ingredients']['milk'] > RESOURCES["milk"]:
        print('Sorry there is not enough milk')
    elif drink["ingredients"]['coffee'] > RESOURCES["coffee"]:
        print('Sorry there is not enough coffee.')
    else:
        return True
    
    
def calculate_payment(quarters, dimes, nickels, pennies):
    sum = 0
    quarters *= 0.25
    dimes *= 0.10
    nickels *= 0.05
    pennies *= 0.01
    sum += quarters + dimes + nickels + pennies
    return sum
    
    
def check_payment(payment, answer):
    global MENU
    global MONEY
    if payment < MENU[answer]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    elif payment > MENU[answer]['cost']:
        change = MENU[answer]['cost'] - payment
        print(f"Here is ${round(abs(change), 2)} dollars in change.")
        MONEY += payment
        return True
    else:
        MONEY += payment
        return True
    
    
    
def prompt_again():
    answer = input('Would you like another drink? "yes" or "no". ')
    if answer == 'no':
        exit()
    else:
        start_coffee()
    
    
def make_coffee(answer):
    global MENU
    global RESOURCES
    drink = MENU[answer]['ingredients']
    RESOURCES["coffee"] - drink['coffee']
    RESOURCES['milk'] - drink['milk']
    RESOURCES['water'] - drink['water']
    print(f'Here is your {answer}. Enjoy!')
    prompt_again()
    

def get_coffee(answer):
    can_make_drink = check_resources(answer)
    if can_make_drink:
        print('Please insert coins.')
        quarters = int(input('How many quarters? '))
        dimes = int(input('How many dimes? '))
        nickels = int(input('How many nickels? '))
        pennies = int(input('How many pennies? '))
        payment = calculate_payment(quarters, dimes, nickels, pennies)
        can_pay = check_payment(payment, answer)
        if can_pay:
            make_coffee(answer)
    

def handle_prompt(answer):
    if answer == 'off':
        exit()
    if answer == 'report':
        print_report()
    if answer == 'latte' or answer == 'cappuccino' or answer == 'espresso':
        get_coffee(answer)
    

def start_coffee():
    user_answer = input("What would you like?(espresso/latte/cappuccino)☕️")
    handle_prompt(user_answer)
    
start_coffee()