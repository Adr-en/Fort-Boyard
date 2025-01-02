import random
from random import randint, choice
import json
import time

def treasure_room():
    with open("data/TRClues.json", "r") as f:

        tv_game = json.load(f)
        year = choice(list(tv_game["Fort Boyard"].keys()))
        show = choice(list(tv_game["Fort Boyard"][year].keys()))
        clues = tv_game["Fort Boyard"][year][show]["Clues"]
        code_word = tv_game["Fort Boyard"][year][show]["CODE-WORD"]

        print("The first 3 clues are :")
        time.sleep(1)

        for i in range(3) :
            print(clues[i])
            time.sleep(0.5)

        attempt = 3
        answer_correct = False

        while attempt > 0 and not answer_correct :
            answer = str(input("Your answer is : "))

            if answer.upper() == code_word :
                answer_correct = True
            else :
                attempt -= 1
                if attempt != 0 :
                    print(f"You have {attempt} remaining attempt")
                    print(clues[3+(3-attempt)])

                else :
                    print(f"You don't have any more attempt, the code was {code_word}")


        if answer_correct : print("You won the final game! \n CONGRATULATION!!!!")

        else : print("Sorry you lost, you should have been better that that, loser :D")




treasure_room()