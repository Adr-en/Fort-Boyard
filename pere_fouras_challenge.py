import json  # as it is a json file, we use the json function to load it into a list of dictionaries
import random


def load_riddles(file):
    with open(file, "r") as f:
        return json.load(f)

def pere_fouras_riddles():
    print("\nHere is your riddle :")
    L = load_riddles("data/PFRiddles.json")
    dic = L[random.randint(0, len(L)-1)]
    print(dic["question"])
    attempts = 3
    while attempts > 0:
        ans = input("Take a guess :").lower()
        if ans == dic['answer'].lower():
            print("Correct ! You win a key.\n")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect ! {attempts} attempts remaining")
            else:
                print("You failed the challenge ! The correct answer was :", dic['answer'],"\n")
                return False


