#----------import necessary modules----------------#

from chance_challenges import *
from final_challenge import *
from math_challenges import *
from logical_challenges import *
from pere_fouras_challenge import *
from utility_functions import *
from random import randint, choice



#-----------------------------------------------------------#

def game():
    introduction()
    equipe = compose_equipe()
    keys = 0
    while keys < 3:
        chall = [math_challenge, tictactoe_game, chance_challenge, pere_fouras_riddles]
        print()
        chall_sel = challenges_menu()
        print()
        nb_player = choose_player(equipe)
        if chall[chall_sel]():
            for ele in equipe:
                if ele == nb_player:
                    ele['keys_won'] += 1
            keys += 1

    print("And now the treasure room!")
    treasure_room()

game()