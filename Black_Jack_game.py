import random

def main_part(user_choice, dealer_choice, total_amount, deal_amount):
    sum1 = sum(user_choice)
    sum2 = sum(dealer_choice)
    if sum2 == sum1 == 21:
        print(f"{dealer_choice} and {user_choice}\n Black Jack    Black Jack\n It's Draw")
        total_amount += deal_amount
        return total_amount
    elif sum1 == 21:
        print("Black Jack!\n You Win!")
        total_amount += 2 * deal_amount
        return total_amount
    elif sum2 == 21:
        print("Black Jack!\n You lose!")
        return total_amount
    elif sum2 == sum1:
        print(f"{dealer_choice} and {user_choice}\n It's Draw")
        total_amount += deal_amount
        return total_amount
    elif sum1 > 21:
        print(f"Your card: {sum1} > 21!")
        print("Blast!\n You lose!")
        return total_amount
    elif sum2 > 21:
        print(f"Dealer card: {sum2} > 21!")
        print("Blast!\n You Win!")
        total_amount += 2 * deal_amount
        return total_amount
    elif 21 - sum2 > 21 - sum1:
        print("You Win!")
        total_amount += 2 * deal_amount
        return total_amount
    elif 21 - sum2 > 21 - sum1:
        print("You Lose!")
        return total_amount

print("""  
                         _____                _____    ______                 ______
          \\    /\\    /  |       |     |      |        |      |   /\\    /\\    | 
           \\  /  \\  /   |-----  |     |      |        |      |  /  \\  /  \\   |------
            \\/    \\/    |_____  |____ |____  |_____   |______| /    \\/    \\  |______
                         """)
print("**************************")
print("This Is A Black Jack Game!")
print("**************************")

total_amount = 1000
def black_jack():
    global total_amount
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    currency = {"A": 25,
                "B": 50,
                "C": 100,
                "D": 500,
                "E": 1000}
    print(f"Your amount is: ${total_amount}")
    print("--------------------------------")
    print("CHOOSE")
    for key, value in currency.items():
        print(f"{key} for {value}")
    print("--------------------------------")
    deal_letter = input("Enter the amount you want to deal: ").upper()
    print("--------------------------------")
    deal_amount = currency[deal_letter]
    total_amount -= deal_amount
    if total_amount < 0:
        print("You can't bet this amount!")
        want_continue = input("Do you want to continue(y or n): ")
        if want_continue == "y":
            black_jack()
        else:
            return 0
    else:
        print("--------------------------------")
        print(f"Deal amount {deal_amount}")
        print("--------------------------------")
        print(f"Your current amount {total_amount}")
        print("--------------------------------")
        dealer_choice = []
        user_choice = []
        for i in range(2):
            dealer_choice.append(random.choice(deck))
            user_choice.append(random.choice(deck))
        print("--------------------------------")
        print(f"Dealer {[dealer_choice[1]]}")
        print(f"User {user_choice}")
        print("--------------------------------")
        if sum(dealer_choice) != 21:
            while sum(user_choice) < 21:
                add = input("Do you want to hit: (y or n):").lower()
                if add == "y":
                    user_choice.append(random.choice(deck))
                    print(f"Your cards are: {user_choice}")
                else:
                    break
        print("--------------------------------")
        if sum(user_choice) != 21:
            while sum(dealer_choice) < 17:
                dealer_choice.append(random.choice(deck))
        print(f"The dealer cards are: {dealer_choice}")
        print(f"Your cards are: {user_choice}")

        total_amount = main_part(user_choice, dealer_choice, total_amount, deal_amount)
        print(f"Your amount is: ${total_amount}")

        if total_amount == 0:
            print("You total amount is 0!")
        want_continue = input("Do you want to continue(y or n): ")
        if want_continue == "y":
            total_amount = black_jack()


black_jack()



















