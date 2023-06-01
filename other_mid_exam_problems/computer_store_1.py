products_sum = 0
sum_without_tax = 0
taxes = 0
command = input()

while True:
    if command == "special" or command == "regular":
        break
    if float(command) < 0:
        print("Invalid price!")

    else:
        price_without_tax = float(command)

        sum_without_tax += price_without_tax
        tax = price_without_tax * 0.20
        taxes += tax
        price_with_tax = price_without_tax + tax

        products_sum += price_with_tax

    command = input()

if products_sum == 0:
    print("Invalid order!")
else:
    if command == "special":
        products_sum = products_sum * 0.90

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {products_sum:.2f}$")

