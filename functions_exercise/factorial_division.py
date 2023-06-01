import math


def factorial_division(a,b:int):
    factorial_a = math.factorial(a)
    factorial_b = math.factorial(b)
    result = factorial_a / factorial_b
    return f"{result:.2f}"

input_a = int(input())
input_b = int(input())

print(factorial_division(input_a, input_b))

