# hangman. the computer selects a random word and the user tries to guess it 

from random import choice

with open("valid-wordle-words.txt", "r") as wordlist:
    #computer selects a random word from wordbank
    wordbank = wordlist.readlines()
    computerword = choice(wordbank)

def hangman():

    # prints the guesslsit and word list neatly
    def printem():
        print(f'Your guesses: {" ".join(guesslist)}')
        print(" ".join(_word))
        print("")


    # makes a new word of _ the length of the computerword 
    _word = ["_"] * len(computerword)
    """for char in computerword:
        _word.append("_")"""
    
    # turns word into list with spaces to check for win condition
    actualword = []
    for char in computerword:
        actualword.append(char)

    # number of incorrect guesses remaining
    lives = 5
    guesslist = []
    while lives > 0:

        if _word != actualword:
            # user guesses a letter and makes it lowercase
            user_guess = input("Guess a Letter: ")
            guesslist.append(user_guess)
            if user_guess in computerword:

                # replaces _ with the letter
                for char in computerword:
                    if user_guess == char:

                        # finds the index of every occurence of the letter and replaces _ with the letter
                        indices = [i for i, x in enumerate(computerword) if x == char]
                        for i in indices:
                            _word[i] = char
                printem()
            # subtracts a life when you don't guess the letter
            else:
                lives -= 1
                print(f'You have {lives} lives left.')
                printem()

        # if the user wins
        elif _word == actualword:  
            print("You won!")
            break

        # if the user runs out of lives
        if lives == 0:
            print("You lost.")
            print(f'The word was {computerword}')
            
hangman()


#currently adds an extra _ to the words??