quantity_dict = {}
price_dict = {}
command = input()
while command != "buy":
    command = command.split()
    product = command[0]
    price = float(command[1])
    count = int(command[2])

    if product in quantity_dict:
        price_dict[product] = price
        quantity_dict[product] += count
    else:
        price_dict[product] = price
        quantity_dict[product] = count

    command = input()

[print(f"{x} -> {quantity_dict[x] * price_dict[x]:.2f}") for x in quantity_dict]