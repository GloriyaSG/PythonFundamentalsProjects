def solve(a, b, operator):
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a // b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result
input_operator = input()
input_a = int(input())
input_b = int(input())

print(solve(input_a, input_b, input_operator))