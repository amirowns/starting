# the user enters a number, and the computer tries to guess the number

from random import randint


print("Think of a number between 1-100")
guess = randint(1,100)
correction = -1
guesslow = 1
guesshigh = 100
while correction != "correct":
    correction = input(f"Is {guess} high, low, or correct?")

    if correction == "high":
        guesshigh = guess - 1
        guess = randint(guesslow, guesshigh)
        
    elif correction == "low":
        guesslow = guess + 1
        guess = randint(guesslow, guesshigh)
else:
    print(f"I got it! Your number is {guess}")
