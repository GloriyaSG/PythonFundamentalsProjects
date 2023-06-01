# bakery shop

shop_stock = {}
sold_product = 0
while True:
    line = input()
    if line == "Complete":
        break
    command = line.split()
    quantity, food = int(command[1]), command[2]
    if command[0] == "Receive":
        if quantity <= 0:
            continue
        if food not in shop_stock:
            shop_stock[food] = quantity
        else:
            shop_stock[food] += quantity

    elif command[0] == "Sell":
        if food not in shop_stock:
            print(f"You do not have any {food}.")
        elif quantity > shop_stock[food]:
            print(f"There aren't enough {food}. You sold the last {shop_stock[food]} of them.")
            sold_product += shop_stock[food]
            shop_stock.pop(food)
        else:
            print(f"You sold {quantity} {food}.")
            sold_product += quantity
            shop_stock[food] -= quantity
            if shop_stock[food] == 0:
                shop_stock.pop(food)
for x in shop_stock:
    print(f"{x}: {shop_stock[x]}")

print(f"All sold: {sold_product} goods")





