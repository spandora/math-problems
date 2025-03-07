import random

def get_random_math_problem():
    operators = ["+", "-", "*", "/"]
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(operators)
    problem = f"{num1} {operator} {num2}"
    return problem

print(get_random_math_problem())
