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
        chall_sel = challenges_menu()
        nb_player = choose_player(equipe)
        if chall[chall_sel]():
            for ele in equipe:
                if ele == nb_player:
                    ele['keys_won'] += 1
            keys += 1
            record_history(chall_sel, nb_player["name"], "game won", keys)
        else :
            record_history(chall_sel, nb_player["name"], "game won", keys)
        print(equipe)
    print("And now the treasure room!")
    treasure_room()
game()