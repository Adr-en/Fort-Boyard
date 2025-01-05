def introduction():
    print("\nHello competitor.\n")
    print("So you've decided to take your chance and confront yourself to the fort and its dangers?\nOnly future will tell us if you made a brave or foolish act")
    print("You will have to face various challenges in order to earn keys.")
    print("3 of them will take you to the tresor room, so fight with everything you have!")
    print("Good luck competitor, and may you come out victorious of the fort\n")



def compose_equipe():
    nb = int(input("How many players wish to include the team? "))
    while nb > 3:
        nb = int(input("There can't be more than 3 players in a team. Write again : "))
    team = []
    for i in range(nb):
        player = {}
        player['name'] = input(f"\nName of the player {i+1} : ")
        player['profession'] = input(f"Profession of the player {i+1} : ")
        while True:
            leader = input('Is the player the leader ("yes" or "no") : ')
            if leader == "yes":
                player['leader'] = True
                break
            elif leader == "no":
                player['leader'] = False
                break
            else:
                print('Incorrect input, you have to write yes or no')
        player['keys_won'] = 0
        team.append(player)

    count_leader = 0
    for ele in team:
        if not ele['leader']:
            count_leader += 1
    if count_leader == len(team):
        team[0]['leader'] = True
    return team


def challenges_menu():
    print("1.   Mathematics challenge")
    print("2.   Logic challenge")
    print("3.   Chance challenge")
    print("4.   Père Fouras' riddle")
    nb_chall = int(input("Choose your challenge : "))
    return nb_chall-1


def choose_player(team):
    for i in range(len(team)):
        lead = 'Member'
        if team[i]['leader']:
            lead = 'Leader'
        print(f"{i+1}. {team[i]['name']} ({team[i]['profession']}) - {lead}")
    player = int(input("Enter the player's number : "))
    return team[player-1]



