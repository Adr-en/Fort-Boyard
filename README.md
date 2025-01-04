FORT BOYARD SIMULATOR

by DE CHAVAGNAC Adrien and FREYNET-SERRE Raphaël - coders

This project aims to recreate the mythic game of Fort Boyard where a team face various challenges (of logic, chance and many more) in order to have 3 keys which give them access to a treasure room
This project was coded in python and we used the "math" and "json" libraries as well as "random" and "time" from the standard library


Functions :
game() (main.py) : combine all the functions from other modules to lauch the game

factorial(n) (math_challenges.py) : return an integer whose value is the factorial of n
math_challenge_factorial() (math_challenges.py) : The user must calculates the factorial of a random integer between 1 and 10, and the function returns a boolean whether this answer is true or false.
math_roulette_challenge() (math_challenges.py) : The user must calculate the result of an operation (addition, subtraction, or muliplication) applied to a random list of integers between 1 and 20. The user provides their answer, and the function returns a boolean whether the answer is true or false.
math_challenge_equation() (math_challenges.py) : The user must solve a linear equationof the format a*x + b = 0, and the function returns a boolean whether its answer is correct (rounded up to 0.001) or incorrect.
solve_linear_equation() (math_challenges.py) : generates two random numbers between 1 and 10 and give te solution of the equation a*x + b = 0, and returns these 3 numbers

load_riddles(file) (pere_fouras_challenge.py) : take as a parameter a json file, and load its content in a file f before returning f
pere_fouras_riddles() (pere_fouras_challenge.py) : Use the load_riddles(file) function to get as explotaible data a given json file containing riddles. It asks the user one of theses riddles up to three times, then return a boolean whether the user has found the answer or not

upper_case(s) (utility_functions.py) : converts a letter to uppercase if in lowercase
introduction() (utility_functions.py) : print a welcome script
compose_equipe() (utility_functions.py) : returns a list of up to three players (each one of them as a dictionnary taking there names/professions/whether they are the leader or not) 
challenges_menu() (utility_functions.py) : returns a boolean corresponding to the challenge the user chose
choose_player(team) (utility_functions.py) : take as parameter "team", a list of dictionnaries, and ask the user to choose one of the player then returns the dictionnary corresponding to the player


Inputs and error management :
We placed various print() troughout the code to understand better where the errors were located and fix them more easily.
A bug we faced was a circular import case between different modules : we fixed this by importing modules only once, in the main.py
Another bug we faced happened when we tried to call a function at random as erros occur when we try to do a list of functions of this type : [fct1(), fct2()] : we succeded with the following method :
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


