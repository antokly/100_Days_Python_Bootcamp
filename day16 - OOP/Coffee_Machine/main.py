from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def display_menu(menu):
    """Displays the available drinks."""
    print("\nAvailable Menu:")
    print(menu.get_items())

def process_order():
    """Handles the drink ordering process."""
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    
    while True:
        display_menu(menu)
        user_order = input("What would you like to drink? (espresso/latte/cappuccino): ").lower().strip()
        
        if user_order == "off":
            print("Shutting down the machine...")
            break # To stop and quit the program execution
        
        # store the order menu choice
        order = menu.find_drink(user_order)

        if order is None:
            print("\nInvalid order. Please choose a drink from the menu.\n")
            continue
        
        # Display reports before preparation
        coffee_maker.report()
        money_machine.report()
        
        # Check resources
        if not coffee_maker.is_resource_sufficient(order):
            print("Insufficient resources to prepare this drink.\n")
            continue
        
        # Request payment
        if money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
        else:
            print("Insufficient payment. Order canceled.\n")

if __name__ == "__main__":
    print("Welcome to the coffee machine!\n")
    process_order()