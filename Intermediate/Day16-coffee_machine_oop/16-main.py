from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#instances
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    coffee_options = menu.get_items()
    user_choice = input(f'What would you like? ({coffee_options}): ').lower().strip()

    if user_choice == 'off':
        print('-----MAINTENANCE TIME-----')
        break
    
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink_choice = menu.find_drink(user_choice)

        if drink_choice is None: 
            print("Sorry that item is not available.")
            continue #we jump to the next iteration

        if coffee_maker.is_resource_sufficient(drink_choice): #if this is True
            if money_machine.make_payment(drink_choice.cost): #if this is True
                coffee_maker.make_coffee(drink_choice)
    
    