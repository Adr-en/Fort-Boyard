from random import randint



def display_grid(grid):
    for line in grid:
        print("\n| ", end = "")

        for element in line:
            print(element, end = " | ")
    print("")


def check_victory(grid, symbol) :

    for line in range(len(grid)):
        check_col = True
        check_line = True

        for col in range(len(grid)):

            if grid[line][col] != symbol:
                check_line = False

            if grid[col][line] != symbol:
                check_col = False

        if check_col or check_line : return True

    if grid[0][0] == grid [1][1] == grid [2][2] == symbol : return True
    if grid[0][2] == grid[1][1] == grid[2][0] == symbol : return True

    return False




def master_move(grid, symbol):

    for line in range(len(grid)):
        for column in range(len(grid[line])):

            if grid[line][column] == "":
                grid[line][column] = symbol
                if check_victory(grid, symbol):
                    grid[line][column] = ""
                    return line,column
                grid[line][column] = ""



    for line in range(len(grid)):
        for column in range(len(grid[line])):

            if grid[line][column] == "":
                grid[line][column] = "X"
                if check_victory(grid, "X"):
                    grid[line][column] = ""
                    return line,column
                else :
                    grid[line][column] = ""




    while True:
        line, column = randint(0, len(grid) - 1), randint(0, len(grid) - 1)
        if grid[line][column] == "":
            return line,column




def player_turn(grid):
    print("\nEnter the coordinnates of your choice (0,1 or 2) :")
    line = int(input("Line :"))
    col = int(input("Column :"))

    while grid[line][col] != "" :
        print("Invalid coordinates! \n")

        line = int(input("Line : "))
        col = int(input("Column : "))
    grid[line][col] = "X"
    display_grid(grid)




def master_turn(grid):
    line,col = master_move(grid, "O")
    grid[line][col] = "O"
    display_grid(grid)




def full_grid(grid):

    for line in grid:
        for element in line:
            if element == "":
                return False
    return True


def check_result(grid):
    if check_victory(grid, "X") :
            return "X"
    elif check_victory(grid, "O"):
        return "O"
    elif full_grid(grid) :
        return True
    else :
        return False


def tictactoe_game():
    print("Win the TicTacToe:\n")
    grid = [["","",""],
            ["","",""],
            ["","",""]]
    display_grid(grid)
    while True:
        player_turn(grid)
        if check_result(grid) == "X":
            print("You won the tictactoe! And a key!")
            return True

        if check_result(grid) :
            print("it's a draw, you lose")
            return False

        master_turn(grid)
        if check_result(grid) == "O":
            print("The master won, you lost the tictactoe!")
            return False



