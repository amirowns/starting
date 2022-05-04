# rock paper scissors, the computer picks one, then the user picks one, play until win

from random import choice

# list of options to choose from
options = ["rock", "paper", "scissors"]

while True:

    # computer randomly chooses an option
    computer_choice = choice(options)

    # user chooses an option
    user_choice = input("The computer has chosen. Pick rock, paper, or scissors ")
    
    # does all the ties

    # can just use if user_choice == computer_choice:
    if (user_choice == "rock" and computer_choice == "rock") \
        or (user_choice == "paper" and computer_choice == "paper")\
        or (user_choice == "scissors" and computer_choice == "scissors"):
        print("It's a tie! ")

    # does all the wins
    elif (user_choice == "rock" and computer_choice == "scissors") \
        or (user_choice == "paper" and computer_choice == "rock")\
        or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! ")
        break

    # does the SAME THING as writing in all the losses
    else: 
        print("RIP you lost. Try again! ")

    """# does all the losses
    elif (user_choice == "rock" and computer_choice == "paper") \
        or (user_choice == "paper" and computer_choice == "scissors")\
        or (user_choice == "scissors" and computer_choice == "rock"):
        print("RIP you lost. Try again! ")"""    

