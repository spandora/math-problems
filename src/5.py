import random

def solve_math_problem(a, b):
    """
    Solves a math problem consisting of two numbers and returns the solution.
    """
    operation = random.choice(["+", "-", "*", "/"])
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    else:
        return a / b