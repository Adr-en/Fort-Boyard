import random as r

def math_roulette_challenge():
    list = [r.randint(1, 20) for i in range(5)]
    operation = r.choice(["addition", "subtraction", "multiplication"])
    print(f"Numbers on the roulette: {list}")
    print(f"Calculate the result by combining these numbers with {operation}")
    ans = int(input("Your answer: "))
    res = 0
    if operation == "addition":
        for i in range(5):
            res += list[i]
        return ans == res
    elif operation == "subtraction":
        for i in range(5):
            res -= list[i]
        return ans == res
    elif operation == "addition":
        for i in range(5):
            res *= list[i]
        return ans == res


def factorial(n):
    if n == 0:
        return 1
    else:
        sum = 1
        for i in range(1, n+1):
            sum *= i
        return sum

def math_challenge_factorial():
    nb = r.randint(1, 10)
    print(f"Math Challenge: Calculate the factorial of {nb}.")
    ans = int(input("Your answer: "))
    if ans == factorial(nb):
        print("Correct! You win a key.")
        return True
    else:
        print("False! Better luck next time.")
        return False

def solve_linear_equation():
    a, b = r.randint(1, 10), r.randint(1, 10)
    return a, b, (-b/a)

def math_challenge_equation():
    a, b, x = solve_linear_equation()
    print(f"Math Challenge: Solve the equation {a}x + {b} = 0.")
    ans = float(input("What is the value of x: "))
    if x-0.001 <= ans <= x+0.001:
        print("Correct! You win a key.")
        return True
    else:
        print("False! Better luck next time.")
        return False




