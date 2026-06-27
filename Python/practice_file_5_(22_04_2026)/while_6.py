#while_6. Guess the number game

import random

secret = random.randint(1, 10)

guess = 0

while guess != secret:
    guess = int(input("Guess number (1 to 10): "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
