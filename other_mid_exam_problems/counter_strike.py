# 100/100
initial_energy = int(input())
won_battles = 0
command = input()

while command != "End of battle":
    distance = int(command)
    if initial_energy < distance or initial_energy == 0:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {initial_energy} energy")
        exit(0)
    else:
        initial_energy -= distance
        won_battles += 1
    if won_battles % 3 == 0:
        initial_energy += won_battles
    command = input()

print(f"Won battles: {won_battles}. Energy left: {initial_energy}")



