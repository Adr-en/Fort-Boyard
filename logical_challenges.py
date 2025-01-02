from random import randint



def display_grid(grid):
    for line in grid:
        #print("\n—————————————") optional je trouve que ça rend pas hyper bien
        print("\n| ", end = "")

        for element in line:
            print(element, end = " | ")



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
    """La fonction permet de choisir où va jouer le master, d'abord on vérifie si le master peut gagner,
     ensuite on vérifie si le joueur peut gagner et dans ce cas là on le bloque
     et sinon le master joue aléatoirement sur une case disponible
     Input : grid (2D list), symbol(string)
     Output : """




    #On vérifie si le master peut gagner, pour chaque case, si elle est vide
    #on vérifie si le master gagne en jouant dessus
    for line in range(len(grid)):
        for column in range(len(grid[line])):

            if grid[line][column] == "":
                grid[line][column] = symbol
                if check_victory(grid, symbol):
                    grid[line][column] = ""
                    return line,column
                grid[line][column] = ""


    #On vérifie si le joueur peut gagner pour chaque case vide,
    # si il peut le master joue dessus pour le bloquer sinon on remet la case vide
    for line in range(len(grid)):
        for column in range(len(grid[line])):

            if grid[line][column] == "":
                grid[line][column] = "X"
                if check_victory(grid, "X"):
                    grid[line][column] = ""
                    return line,column
                else :
                    grid[line][column] = ""


    #Le master joue aléatoirement sur une des cases disponible

    while True:
        line, column = randint(0, len(grid) - 1), randint(0, len(grid) - 1)
        if grid[line][column] == "":
            return line,column




def player_turn(grid):
    line = int(input("\n\nEnter coordinates of the line where you want to play: "))
    col = int(input("Enter coordinates of the col where you want to play: "))

    while grid[line][col] != "" :
        print("Invalid coordinates! /n")

        line = int(input("Enter coordinates of the line where you want to play: "))
        col = int(input("Enter coordinates of the col where you want to play: "))
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
    grid = [["","",""],
            ["","",""],
            ["","",""]]
    display_grid(grid)
    while True:
        player_turn(grid)
        if check_result(grid) == "X":
            print("You won the tictactoe!")
            return True

        if check_result(grid) :                         #must be there because if the grid is full it can only be after the player turn
            print("it's a draw, you lose")
            return False

        master_turn(grid)
        if check_result(grid) == "O":
            print("The master won, you lost the tictactoe!")
            return False



