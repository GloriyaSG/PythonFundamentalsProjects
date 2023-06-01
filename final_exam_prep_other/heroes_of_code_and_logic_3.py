# 100%
num_heroes = int(input())
heroes = {}

for x in range(num_heroes):
    hero_hit_points_mana_points = input().split(" ")
    hero = hero_hit_points_mana_points[0]
    hit_points = int(hero_hit_points_mana_points[1])
    mana_points = int(hero_hit_points_mana_points[2])
    heroes[hero] = {"HP":hit_points, "MP":mana_points}

while True:
    line = input()
    if line == "End":
        break
    command = line.split(" - ")
    hero = command[1]
    if command[0] == "CastSpell":
        mp_needed, spell_name = int(command[2]), command[3]
        if heroes[hero]["MP"] >= mp_needed:
            heroes[hero]["MP"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        damage, attacker = int(command[2]), command[3]
        heroes[hero]["HP"] -= damage
        if heroes[hero]["HP"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['HP']} HP left!")
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        amount = int(command[2])
        if heroes[hero]["MP"] + amount > 200:
            diff = 200 - heroes[hero]["MP"]
            heroes[hero]["MP"] = 200
            print(f"{hero} recharged for {diff} MP!")
        else:
            heroes[hero]["MP"] += amount
            print(f"{hero} recharged for {amount} MP!")
    elif command[0] == "Heal":
        amount = int(command[2])
        if heroes[hero]["HP"] + amount > 100:
            diff = 100 - heroes[hero]["HP"]
            heroes[hero]["HP"] = 100
            print(f"{hero} healed for {diff} HP!")
        else:
            heroes[hero]["HP"] += amount
            print(f"{hero} healed for {amount} HP!")

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")
