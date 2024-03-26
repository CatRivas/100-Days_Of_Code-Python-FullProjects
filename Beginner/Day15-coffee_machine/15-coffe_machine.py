from menu import MENU, resources

def report(current_profit):
    """Generate a report showing the current resources and profit."""
    # Print the current levels of water, milk, coffee, and money
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${current_profit}')

# def resources_update(coffee_choice):
#     for ingredient in MENU[coffee_choice]["ingredients"]:
#         resources[ingredient] -=  MENU[coffee_choice]["ingredients"][ingredient]

#this way is more pythonic
def resources_update(coffee_choice):
  """Update the resources based on the selected coffee choice."""
  # Deduct the ingredients of the selected coffee from the available resources
  for ingredient, quantity in MENU[coffee_choice]["ingredients"].items():
    resources[ingredient] -= quantity

def money_update(cost):
    """Update the profit after a successful transaction."""
    # Calculate the new profit after deducting the cost of the coffee
    new_profit = current_profit + cost
    return new_profit

def check_resources(user_coffee):
    """Check if there are enough resources to make the selected coffee."""
    # enough_resources = True
    for value in user_coffee["ingredients"]:    
        # Check if the available resources for the ingredient are less than required
        if resources[value] < user_coffee["ingredients"][value]:
            # enough_resources = False
            # If not enough of an ingredient, print a message and return False
            print(f"Sorry there is not enough {value}.")
            return False

    # if enough_resources:
    # If all ingredients are available in sufficient quantity, return True
    return True
           

def get_coins():
    """Prompt the user to insert coins and return the coins."""
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    return quarters, dimes, nickles, pennies

def process_payment(q, d, n, p):
    """Calculate and returns the total amount of money inserted by the user."""
    # Calculate the total amount of money inserted by the user based on the coin quantities
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    
    return total

def transaction(coffe_cost, user_money):
    """Process the transaction and provide change if necessary."""
    change = 0
    if coffe_cost > user_money:
        print("Sorry that's not enough money. Money refunded.")
        
        return False
    
    elif coffe_cost < user_money:
        change = round(user_money - coffe_cost, 2)
        print(f'Here is ${change} in change.\nHere is your {user_option} ☕ Enjoy!')
        
        return True


# Initialize in zero the current profit (the first report ¡you know!)
current_profit = 0

while True:
    user_option = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    
    if user_option == 'off':
        print('-----MAINTENANCE TIME-----')
        break
    
    elif user_option == 'report':
        report(current_profit)
    
    # elif user_option == "espresso" or user_option == "latte" or user_option == "cappuccino":
    elif user_option in {"espresso", "latte", "cappuccino"}: #more pythonic way to put the conditional with a set
        if check_resources(MENU[user_option]) == True: 
            cant_quarters,cant_dimes,cant_nickles,cant_pennies = get_coins()
            amount = process_payment(cant_quarters,cant_dimes,cant_nickles,cant_pennies)
            result = transaction(MENU[user_option]["cost"], amount)

            # Update resources and profit if the transaction is successful
            if result: #True
                resources_update(user_option)
                current_profit = money_update(MENU[user_option]["cost"])





