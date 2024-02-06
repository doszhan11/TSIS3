#13
import random

def guess_n():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret = random.randint(1, 20)
    gues = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        gues += 1

        if guess < secret:
            print("Your guess is too low.")
        elif guess > secret:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {gues} guesses!")
            break

guess_n()
