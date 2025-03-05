
import random

def get_random_math_problem():
    numbers = [1, 2, 3, 4, 5]
    operators = ["+", "-", "*", "/"]
    problem = ""
    for i in range(3):
        number1 = numbers[random.randint(0, len(numbers) - 1)]
        number2 = numbers[random.randint(0, len(numbers) - 1)]
        operator = operators[random.randint(0, len(operators) - 1)]
        problem += f"{number1} {operator} {number2}"
    return problem