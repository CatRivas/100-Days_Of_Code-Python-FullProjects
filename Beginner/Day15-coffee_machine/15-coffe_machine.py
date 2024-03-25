from menu import MENU, resources

def report():
    money = 0
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')

def check_resources(user_coffee):
    for value in user_coffee["ingredients"]:    
        if resources[value] > user_coffee["ingredients"][value]:
            print('choose sometjhing else')

# def check_resources(user_coffee):
#     for ingredient, amount in user_coffee["ingredients"].items():
#         if resources[ingredient] > amount:
#             print(f"Not enough {ingredient}. Choose something else.")
#     #         return False
#     # return True

def option(user_choice):
    if user_choice == 'report':
        report()
    elif user_choice == 'espresso':
        check_resources(MENU["espresso"])
    elif user_choice == 'latte':
        check_resources(MENU["latte"])
    elif user_choice == 'cappuccino':
        check_resources(MENU["cappuccino"])
    elif user_choice == 'off':
        exit()

choose = input("What would you like? (espresso/latte/cappuccino): ")
option(choose)




