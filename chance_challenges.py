from random import randint, choice
from utility_functions import upper_case


def shell():
    nb_attempt = 2
    shell = ["A", "B", "C"]

    print("Hi, in this game you will compete against the game master,"
          "You have two attempt to find the shell where the key is randomly placed")
    print("Choose between the shells A, B and C")               # juste les lettres ou un message qui va avec



    while nb_attempt > 0:

        print(f"you have {nb_attempt} attempt left")
        nb_attempt -= 1

        myst = choice(shell)
        player = str(input("Choose a shell")).upper()


        if player in shell:

            if player == myst:
                print("You found the right shell!")
                return True
            else :
                print("Ouch, you found the wrong shell!")

        else :
            print("This choice is not valid, try again")
            nb_attempt += 1
    print("You lost the game, what a bad luck!!")
    return False



def rolling_dice_game():
    nb_attempt = 3

    for i in range(nb_attempt):
        print(f"you have {nb_attempt - i} attempt left")
        input("press enter to roll the dice")
        dices_plr = (randint(1, 6), randint(1, 6))
        print(dices_plr)
        if 6 in dices_plr:
            print("Congratulations you won the game, AND THE KEY!!!")
            return True

        dices_mstr = (randint(1, 6), randint(1, 6))
        print(dices_mstr)
        if 6 in dices_mstr:
            print("You lost, you'll have to find another way to get a key")
            return False
        print("No 6 were obtain, let's try again")

    print("Nobody got a 6, that's a draw, too bad you lose the game")
    return False


def chance_challenge():
    game = ["Shell game", "rolling dice challenge"]

    if choice(game) == "Shell game":
        print("You'll play the shell game")
        return shell()

    else :
        print("You will play the game of the dices")
        return rolling_dice_game()

