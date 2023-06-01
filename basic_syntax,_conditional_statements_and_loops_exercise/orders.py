number_of_orders = int(input())
total = 0
for n in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_days = int(input())
    total_price_per_day = (capsules_per_days * price_per_capsule) * days
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_days <= 2000:
        total += total_price_per_day
        print(f"The price for the coffee is: ${total_price_per_day:.2f}")
    else:
        continue
print(f"Total: ${total:.2f}")