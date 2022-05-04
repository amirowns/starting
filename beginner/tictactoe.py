# tic tac toe , make a grid, if 3 in a row, win

def tictactoe():
    grid = []

    # makes the 3x3 grid
    for i in range(3):
        grid.append(["."] * 3)

    # print grid neatly
    def print_grid(grid):
        for i in grid:
            print(" ".join(i))
    print_grid(grid)

    currentgrid = [[],[],[]]
    currentgrid[0].append("X")

    print_grid(currentgrid)


tictactoe()