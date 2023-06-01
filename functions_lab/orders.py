def product(prod, nums):
    result = None
    if prod == "coffee":
        result = nums * 1.50
    elif prod == "water":
        result = nums * 1.00
    elif prod == "coke":
        result = nums * 1.40
    elif prod == "snacks":
        result = nums * 2.00
    return (f"{result:.2f}")

input_prod = input()
num_input = float(input())
print(product(input_prod,num_input))