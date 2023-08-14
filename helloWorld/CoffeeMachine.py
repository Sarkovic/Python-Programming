WATER = 300
MILK = 200
COFFEE = 100
MONEY = 0


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

def espresso():
    water = 50
    coffee = 18
    price = 1.5

    make_coffee(water=water, milk=0, coffee=coffee, cost=price, name="espresso")


def latte():
    water = 200
    coffee = 24
    milk = 150
    price = 2.5

    make_coffee(water=water, milk=milk, coffee=coffee, cost=price, name="latte")


def cappuccino():
    water = 250
    coffee = 24
    milk = 100
    price = 3

    make_coffee(water=water, milk=milk, coffee=coffee, cost=price, name="cappuccino")


def make_coffee(water, milk, coffee, cost, name):
    global WATER
    global COFFEE
    global MILK
    global MONEY

    # First checks if all the resources are available
    if water <= WATER and coffee <= COFFEE and milk <= MILK:
        # Count the money given by the customer
        amount_received = coin_count()
        if amount_received >= cost:
            if amount_received == cost:
                WATER -= water
                COFFEE -= coffee
                MILK -= milk
                MONEY += cost
                print(f"Here's is your {name}. Enjoy!")
            else:
                WATER -= water
                COFFEE -= coffee
                MILK -= milk
                MONEY += cost
                print(f"Here's your change ${(amount_received - cost):.2f} and your {name}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Not enough resources!")


def coin_count():
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))

    total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies

    return total_amount


if __name__ == '__main__':
    while True:
        print(f"What coffee do you want?\nEspresso\nLatte\nCappuccino\n")
        user_coffee_choice = input("Enter Here: ")

        if user_coffee_choice == "espresso":
            print("You chose Espresso!")
            espresso()
        elif user_coffee_choice == "latte":
            print("You chose Latte!")
            latte()
        elif user_coffee_choice == "cappuccino":
            print("You chose Cappuccino!")
            cappuccino()
        elif user_coffee_choice == "report":
            print(f"Water: {WATER}ml")
            print(f"Milk: {MILK}ml")
            print(f"Coffee: {COFFEE}g")
            print(f"Money: ${MONEY: .2f}")
        elif user_coffee_choice == "Off" or user_coffee_choice == "off":
            print("Stopping the coffee machine!")
            break
        else:
            print("Invalid Input!")

        print()
