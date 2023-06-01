items_prices = input().split("|")
budget = float(input())
my_list = []
total_sum = 0
money_earned = 0
for spliter in items_prices:
    items_prices = spliter.split("->")
    type_item = items_prices[0]
    price = float(items_prices[-1])
    if budget < price:
        continue
    if type_item == "Clothes":
        if price <= 50:
            budget -= price
            total_sum += price
            price = price * 1.40
            money_earned += price
            my_list.append(str(f"{price:.2f}"))
    elif type_item == "Shoes":
        if price <= 35:
            budget -= price
            total_sum += price
            price = price * 1.40
            money_earned += price
            my_list.append(str(f"{price:.2f}"))
    elif type_item == "Accessories" and price <= 20.50:
        budget -= price
        total_sum += price
        price = price * 1.40
        money_earned += price
        my_list.append(str(f"{price:.2f}"))

profit = total_sum * 0.40
print(*my_list)
print(f"Profit: {profit:.2f}")
budget += money_earned
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
