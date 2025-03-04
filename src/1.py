import random

def get_random_math_problem(max_value=100):
    problem = ""
    # Generate two random numbers between 1 and max_value
    num1 = random.randint(1, max_value)
    num2 = random.randint(1, max_value)
    # Choose a random operator (+, -, x, /)
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        problem = f"What is {num1} + {num2}?"
    elif op == "-":
        problem = f"What is {num1} - {num2}?"
    elif op == "*":
        problem = f"What is {num1} x {num2}?"
    else:
        problem = f"What is {num1} / {num2}?"
    return problem