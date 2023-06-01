budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_per_loaf = (flour_price * 1.25) * 0.25
price_per_loaf = milk_per_loaf + eggs_price + flour_price
colored_eggs_count = 0
loaves_counter = 0
while price_per_loaf <= budget:
    loaves_counter += 1
    colored_eggs_count += 3
    budget = budget - price_per_loaf
    if loaves_counter % 3 == 0:
        colored_eggs_count -= (loaves_counter - 2)

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")