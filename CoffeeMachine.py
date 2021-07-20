MENU = {
    "espresso": {
        "ingredients": {"water": 50,"coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200,"milk": 150,"coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250,"milk": 100,"coffee": 24},
        "cost": 3.0,
    }
}


money = 0

resources = {
    "water": 300,
    "coffee": 200,
    "milk": 200
}


def check_resources(choice_ingredients):
    """Takes the ingredients from the menu dictionary and checks of quantity is sufficient"""
    for item in choice_ingredients:
        if choice_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def calculate_money():
    """Calculates the total amount the user has"""
    load_cash = input("Please insert coins. ")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def successful_transaction(money_inputted, cost_of_drink):
    """Compares the money available and the cost of the chosen drink and determines if user can continue"""
    if money_inputted > cost_of_drink:
        change = money_inputted - cost_of_drink
        print(f"Here is ${round(change,2)} dollars in change ")
        global money
        money += cost_of_drink
        return True
    else:
        print("Sorry. That's not enough money. Money refunded. ")
        return False


def prepare_drink(drink_name, choice_ingredients ):
    """Deducts ingredients from resources after every order."""
    # the choice ingredients will represents the water, coffee and milk in this case
    for item in choice_ingredients:
        resources[item] -= choice_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        # the user will select the drink options. This will print the dictionaries (ingredients and costs)
        drink = MENU[choice]
        # Compare the ingredients against the available resources
        if check_resources(drink['ingredients']):
            cash_paid = calculate_money()
            if successful_transaction(cash_paid,drink["cost"]):
                prepare_drink(choice, drink['ingredients'])
