from menu import MENU, resources

def report():
    money = 0
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')

def resources_update(coffe_choose):

    for ingredient in MENU[coffe_choose]["ingredients"]:
        resources[ingredient] -=  MENU[coffe_choose]["ingredients"][ingredient]


def check_resources(user_coffee):
    enough_resources = True
    for value in user_coffee["ingredients"]:    
        if resources[value] < user_coffee["ingredients"][value]:
            enough_resources = False
            print(f"Sorry there is not enough {value}.")
            return False

    if enough_resources:
        return True
           

def get_coins():
    print('Please insert coins.')
    quarters = float(input('How many quarters?: '))
    dimes = float(input('How many dimes?: '))
    nickles = float(input('How many nickles?: '))
    pennies = float(input('How many pennies?: '))

    return quarters, dimes, nickles, pennies

def process_payment(q, d, n, p):
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    
    return total

def transaction(coffe_cost, user_money):
    change = 0
    profit = 0
    if coffe_cost > user_money:
        return "Sorry that's not enough money. Money refunded."
    elif coffe_cost < user_money:
        profit = coffe_cost
        change = user_money - profit
        change = round(change, 2)

        return f'Here is ${change} in change.'
    else:
        profit = user_money

        return profit 


def option(user_choice):
    if user_choice == 'report':
        report()
    elif user_choice == 'off':
        print('bye bye')
        exit()
    else:
        if check_resources(MENU[user_choice]) == True: 
            cant_quarters,cant_dimes,cant_nickles,cant_pennies = get_coins()
            amount = process_payment(cant_quarters,cant_dimes,cant_nickles,cant_pennies)
            result = transaction(MENU[choose]["cost"], amount)
            resources_update(user_choice)
  

    # if user_choice == 'report':
    #     report()  
    # elif user_choice == 'espresso':
    #     check_resources(MENU["espresso"])
    # elif user_choice == 'latte':
    #     check_resources(MENU["latte"])
    # elif user_choice == 'cappuccino':
    #     check_resources(MENU["cappuccino"])
    # elif user_choice == 'off':
    #     print('bye bye')
    #     exit()

while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ")
    option(choose)

    if choose == 'off':
        break
# if check_resources() == True: 
#     cant_quarters,cant_dimes,cant_nickles,cant_pennies = get_coins()
#     amount = process_payment(cant_quarters,cant_dimes,cant_nickles,cant_pennies)
#     result = transaction(MENU[choose]["cost"], amount)
#     print(result)
# else:
#     exit()


