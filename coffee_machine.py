
machine_resource = {"Water": 300,
                    "Milk": 200,
                    "Coffee": 100,}
flavors = {"espresso": {"Water": 50,
                    "Milk": 0,
                    "Coffee": 18,},
           "latte": {"Water": 200,
                    "Milk": 150,
                    "Coffee": 24,},
           "cappuccino": {"Water": 250,
                    "Milk": 100,
                    "Coffee": 24,}}


def M_resource(machine_money=0):
    i = 0
    for key, value in machine_resource.items():
        if i == 0 or i == 1:
            print(f"{key}: {value}ml")
        elif i == 2:
            print(f"{key}: {value}g")
        i += 1
    print(f"Money: ${machine_money}")


def Check_resource(machine_resource, flavors, user_input):
    for key, value in flavors[user_input].items():
            machine_resource[key] -= flavors[user_input][key]
    return machine_resource


def process_coins():
    quarters = int(input("How many Quarters?: "))
    dimes = int(input("How many Dimes?: "))
    nickels = int(input("How many Nickels?: "))
    pennies = int(input("How many Pennies?: "))
    inserted_money = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return round(inserted_money, 2)

def make_coffe(machine_resource, flavors, money):
    price = {"espresso": 1.2,
             "latte": 2.5,
             "cappuccino": 2.0}
    user_input = input("What would you like? (Espresso, Latte, Cappuccino): ")
    if user_input == "report":
        M_resource(money)
        return make_coffe(machine_resource, flavors, money)

    if user_input not in price:
        print("Invalid choice.")
        return make_coffe(machine_resource, flavors, money)

    print("Please insert the coins.")
    money += round(process_coins(), 2)
    if money < price[user_input]:
        print("Sorry that is not enough money. Money refunded.")
        return make_coffe(machine_resource, flavors, money)
    else:
        machine_resource = Check_resource(machine_resource, flavors, user_input)
        for key, value in machine_resource.items():
            if value < 0:
                print(f"Sorry there is no enough {key}.")
                for key, value in flavors[user_input].items():
                    machine_resource[key] += flavors[user_input][key]
                return make_coffe(machine_resource, flavors, money)
        money -= price[user_input]
        print(f"Here is ${round(money, 2)} in change.")
        print(f"Here is your {user_input}, Enjoy!")

        return make_coffe(machine_resource, flavors, money)

print(make_coffe(machine_resource, flavors, 0))





