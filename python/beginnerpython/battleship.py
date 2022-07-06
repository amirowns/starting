from random import randint

board = []

# makes the 5x5 grid, 5 lists of 5 "O"s
for x in range(5):
    board.append(["O"] * 5)

# prints the grid neatly instead of as list
def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

# creates a random row and column for the hidden ship
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# prints the ship coordinates
print(ship_row)
print(ship_col)

# makes the game 4 turns
for turn in range(4):
    print("Turn", turn + 1)

    # the user guess a row and column
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    # wins and breaks
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        # out of bounds
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        # same guess
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        # missses
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        # ends game after 3 turns
        if turn == 3:
            print("Game Over")
            print(f"My ship was on {ship_row},{ship_col}")

    print_board(board)

# TODO 2 player? 
# make ships bigger than 1x1. 
# More than 1 ship? 