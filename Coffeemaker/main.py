from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_check = MoneyMachine()
show_menu = Menu()

while True:
    options = show_menu.get_items()
    choice = input(f"What drink would you like {options}? ").lower()

    if choice == "report":
        coffee_machine.report()
        money_check.report()
    elif choice == "off":
    
        exit()
    else:
        drink = show_menu.find_drink(order_name = choice)
        

        if coffee_machine.is_resource_sufficient(drink):
            print(f"The {drink.name} costs, ${drink.cost}")
            # check if the user pays enough money or more money
            succes = money_check.make_payment(drink.cost)
                        
            if succes:
                coffee_machine.make_coffee(drink)
                
                
                