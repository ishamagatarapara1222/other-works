#1. Guess the Number (User vs Computer with hints)

import random

number = random.randint(1, 100)

while True:
    gusse = int(input("Gusse the number (1-100):"))

    if gusse > number:
        print("Too high! Try again.")
    elif gusse < number:
        print("Too low ! Try agin.")
    else:
        print("Correct! You gussed it.")
        break
