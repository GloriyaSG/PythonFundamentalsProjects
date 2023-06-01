quantity = int(input())
days_left = int(input())
budget = 0
spirit_total = 0
ornament = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
day = 0

while days_left > 0:
    days_left -= 1
    day += 1
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += ornament * quantity
        spirit_total += 5
    if day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity
        spirit_total += 13
    if day % 5 == 0:
        budget += tree_lights * quantity
        spirit_total += 17
        if day % 3 == 0:
            spirit_total += 30
        if day % 10 == 0:
            spirit_total -= 20
            budget += tree_skirt + tree_garland + tree_lights
            if days_left == 0:
                spirit_total -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit_total}')



