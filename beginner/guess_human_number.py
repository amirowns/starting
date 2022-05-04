
# the user guesses a number, computer checks if its correct, returns if its too high, too low, or correct. keep guessing until its correct

# the computer picks a number

from random import randint

actual = randint(1,10)

guess = -1

while guess != actual:
    guess = int(input("Guess a number between 1-10: "))
    if guess > actual:
        print("Too high.")
        
        
    elif guess < actual:
        print("Too low.")
        
    else:
        print("You are correct!")

# TODO: turn it into hotter or colder. maybe abs value it?