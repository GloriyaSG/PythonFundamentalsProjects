energy = int(100)
coins = 100
events = input().split("|")
cant_do_all = False
gained_energy = 0
for part in events:
    events = part.split("-")
    integer = int(events[-1])
    if "rest" in events:
        if integer + energy >= 100:
            energy += integer
            gained_energy = abs((energy - 100) - integer)
            print(f"You gained {gained_energy} energy.")
            energy = int(100)
            print(f"Current energy: {energy}.")

            continue
        else:
            energy += integer
            print(f"You gained {integer} energy.")
            print(f"Current energy: {energy}.")
    elif "order" in events:
        if energy >= 30:
            coins += integer
            energy -= 30
            print(f"You earned {integer} coins.")
        else:
            energy += 50
            print(f"You had to rest!")
    else:
        if coins >= integer:
            print(f"You bought {events[0]}.")
            coins -= integer
        else:
            print(f"Closed! Cannot afford {events[0]}.")
            cant_do_all = True
            break
if not cant_do_all:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")



