# 83%
lines = int(input())

plants = {}
plant_ratings = {}
for x in range(lines):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity)}
    plant_ratings[plant] = []

while True:
    line = input()
    if line == "Exhibition":
        break
    command = line.split()
    plant = command[1]
    if plant not in plants:
        print("error")
        continue
    if command[0] == "Rate:":
        rating = float(command[3])
        plant_ratings[plant].append(rating)
    elif command[0] == "Update:":
        new_rarity = int(command[3])
        plants[plant]["rarity"] = new_rarity
    elif command[0] == "Reset:":
        plant_ratings[plant] = [0]



print("Plants for the exhibition:")
for x in plants:
    avg_rate = len(plant_ratings[x])
    if avg_rate > 0:
        avg_rate = sum(plant_ratings[x]) / avg_rate
    print(f"- {x}; Rarity: {plants[x]['rarity']}; Rating: {avg_rate:.2f}")