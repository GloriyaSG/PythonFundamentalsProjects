dicty = {}
while True:
    command = input()
    if command == "stop":
        break
    else:
        resource = command
        quantity = int(input())

    if resource not in dicty:
        dicty[resource] = quantity
    else:
        dicty[resource] += quantity

[print(f"{resource} -> {dicty[resource]}")for resource in dicty]
