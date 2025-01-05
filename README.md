FORT BOYARD SIMULATOR

by DE CHAVAGNAC Adrien and FREYNET-SERRE Raphaël - coders

This project aims to recreate the mythic game of Fort Boyard where a team face various challenges (of logic, chance and many more) in order to have 3 keys which give them access to a treasure room
This project was coded in python and we used the "math" and "json" libraries as well as "random" and "time" from the standard library


Functions :
game() (main.py) : combine all the functions from other modules to launch the game

factorial(n) (math_challenges.py) : return an integer whose value is the factorial of n
math_challenge_factorial() (math_challenges.py) : The user must calculates the factorial of a random integer between 1 and 10, and the function returns a boolean whether this answer is true or false.
math_roulette_challenge() (math_challenges.py) : The user must calculate the result of an operation (addition, subtraction, or muliplication) applied to a random list of integers between 1 and 20. The user provides their answer, and the function returns a boolean whether the answer is true or false.
math_challenge_equation() (math_challenges.py) : The user must solve a linear equationof the format a*x + b = 0, and the function returns a boolean whether its answer is correct (rounded up to 0.001) or incorrect.
solve_linear_equation() (math_challenges.py) : generates two random numbers between 1 and 10 and give te solution of the equation a*x + b = 0, and returns these 3 numbers

load_riddles(file) (pere_fouras_challenge.py) : take as a parameter a json file, and load its content in a file f before returning f
pere_fouras_riddles() (pere_fouras_challenge.py) : Use the load_riddles(file) function to get as explotable data a given json file containing riddles. It asks the user one of theses riddles up to three times, then return a boolean whether the user has found the answer or not


introduction() (utility_functions.py) : print a welcome script
compose_equipe() (utility_functions.py) : returns a list of up to three players (each one of them as a dictionary taking there names/professions/whether they are the leader or not) 
challenges_menu() (utility_functions.py) : returns a boolean corresponding to the challenge the user chose
choose_player(team) (utility_functions.py) : take as parameter "team", a list of dictionaries, and ask the user to choose one of the player then returns the dictionary corresponding to the player


shell() (chance_challenge.py) : Take no input, return True if the player win, else, False. Allow the player to play the game of the shell.
rolling_dice_game() (chance_challenge.py) : Take no input, return True if the player win the game, False if he loses or there is a draw. Allow the player to fight the master in a rolling dice game
chance_challenge() (chance_challenge.py): Take no input. Choose randomly a game for the player to play and return the result of the game.

display_grid() (logical_challenge.py) : Take a 2D list as input, and print it to form a grid. No return.
check_victory() (logical_challenge.py) : Take a 2D list and a string as input. Check if the string make 3 in a row on the grid. Return True if so, else False.
master_move() (logical_challenge.py) : Take a 2D list and a string as input. Check where the best move can be for the master in function of the grid. return the coordinates of the best move.
player_turn() (logical_challenge.py) : Take a 2D list as input. No return. Allow the player to play, update the grid in consequence and then display it.
master_turn() (logical_challenge.py) : Take a 2D list as input. No return. Choose where the computer will play thanks to master_move() and update and display the grid in consequence.
full_grid() (logical_challenge.py) : Take a 2D list as input. Return True if the 2D list is full, else False.
check_result() (logical_challenge.py) : Take a 2D list as input. return True if the grid is full, False if not, and if one of the player won, return its symbol.
tictactoe() (logical_challenge.py) : Take no input, Return the result of the game. Combine all precedent function to mage a game of tictactoe, a player against the master (the computer)


treasure_room() (final_challenge.py) : Take no input, Return True if the player find the myster word else False. Give 3 first clues and then one more clues for each failed attempt. If no attempt remaining display the word.


Inputs and error management :
We placed various print() throughout the code to understand better where the errors were located and fix them more easily.
A bug we faced was a circular import case between different modules : we fixed this by importing modules only once, in the main.py
Another bug we faced happened when we tried to call a function at random as errors occur when we try to do a list of functions of this type : [fct1(), fct2()] : we succeded with the following method :
![image](https://github.com/user-attachments/assets/4d1bfbfb-45c5-4fa9-b54f-dd8fbc42c700)

Adrien did chance_challenges.py, final_challenge.py and logical_challenge.py as well as part of the main.py
Raphaël did math_challenges.py, pere_fouras_challenge.py and utility_functions.py as well as part of the main.py


Testing and validations :

If more than 3 players :
![image](https://github.com/user-attachments/assets/c6aa3ff0-a5e0-4588-b5dd-1289b8279ff0)

If no leader, the first one will be designated leader :
![image](https://github.com/user-attachments/assets/2a49946d-7252-4400-9260-a7a5a708788a)

If wrote in lowercase for the riddles, it still gives the key :
![image](https://github.com/user-attachments/assets/88146390-a8e4-451d-8e12-1ddeaed88b41)

Math challenge :
![image](https://github.com/user-attachments/assets/8a9b276a-7efa-44e0-bece-7cc63c33a685)

Logical challenge :
![image](https://github.com/user-attachments/assets/8a58feab-e7d5-41f2-a414-c8ead6ce2d0b)

Chance challenge (still gives the key even if wrote in lower case) :
![image](https://github.com/user-attachments/assets/e7237c9c-8548-4f1a-a507-2a087f425557)


