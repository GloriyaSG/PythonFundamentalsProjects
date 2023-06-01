import re

pattern = r">>([A-Za-z]+)<<([\d]+[\.\d]*)!([\d]+)\b"
bought_furniture = []
total_price = 0
while True:
    command = input()
    if command == "Purchase":
        break

    match = re.findall(pattern,command)
    if match:
        product, price, quantity = match[0]
        price = float(price)
        quantity = int(quantity)
        total_price += price * quantity
        bought_furniture.append(product)

print("Bought furniture:")
if len(bought_furniture) > 0:
    print('\n'.join([x for x in bought_furniture]))

print(f"Total money spend: {total_price:.2f}")

