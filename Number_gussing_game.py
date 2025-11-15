import random

print("***************************************")
print("Welcome this is a Number Guessing Game!")
print("***************************************\n\n")

def Guess_number():
    secret_number = random.randint(1, 100)
    num_gausses = 0
    difficuly = input("Enter difficulty level (easy or hard): ").lower()
    print("------------------------------------------\n")
    user_guesses = 0
    if difficuly == "easy":
        Guess = 10
    else:
        Guess = 5
    print(f"You have {Guess} number of guesses!")
    print("------------------------------------------\n")
    while num_gausses < Guess and user_guesses != secret_number:
        user_guesses = int(input("Guess a number between 1 and 100: "))
        print("------------------------------------------")
        if num_gausses > Guess:
            break
        if user_guesses > secret_number:
            print(f"{user_guesses} is to high!")
            print("------------------------------------------\n")
        elif user_guesses < secret_number:
            print(f"{user_guesses} is to low!")
            print("------------------------------------------\n")
        elif user_guesses == secret_number:
            return (f"You got it! It is {secret_number}")
        num_gausses += 1
        print(f"You have left with {Guess - num_gausses} number of guesses!")
        print("------------------------------------------\n")

    return "You have run out of guesses!"

print(Guess_number())

