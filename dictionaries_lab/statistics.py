bakery = {}

command = input()
while command != "statistics":
    prod = command.split(": ")
    product = prod[0]
    value = int(prod[1])
    if product not in bakery:
        bakery[product] = 0
    bakery[product] += value
    command = input()

print("Products in stock:")

for (product, value) in bakery.items():
    print(f"- {product}: {value}")

print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")


