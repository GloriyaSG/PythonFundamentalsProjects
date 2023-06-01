cities_gold_population = {}

while True:
    command = input()
    if command == "Sail":
        break
    else:
        line = command.split("||")
        city, population, gold = line[0], int(line[1]), int(line[2])
        if city not in cities_gold_population:
            cities_gold_population[city] = {"gold": gold, "population": population}
        else:
            cities_gold_population[city]["gold"] += gold
            cities_gold_population[city]["population"] += population

while True:
    command = input()
    if command == "End":
        break
    else:
        line_2 = command.split("=>")
        if line_2[0] == "Plunder":
            town, peoples, money = line_2[1], int(line_2[2]), int(line_2[3])

            if town in cities_gold_population:
                cities_gold_population[town]["gold"] -= money
                cities_gold_population[town]["population"] -= peoples
            print(f"{town} plundered! {money} gold stolen, {peoples} citizens killed.")
            if cities_gold_population[town]["gold"] <= 0 or cities_gold_population[town]["population"] <= 0:
                print(f"{town} has been wiped off the map!")
                cities_gold_population.pop(town)

        if line_2[0] == "Prosper":
            town, money = line_2[1], int(line_2[2])
            if money < 0:
                print("Gold added cannot be a negative number!")
                continue
            else:
                cities_gold_population[town]["gold"] += money
                total_money = cities_gold_population[town]["gold"]
                print(f"{money} gold added to the city treasury. {town} now has {total_money} gold.")

if len(cities_gold_population) < 1:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities_gold_population)} wealthy settlements to go to:")
    for town in cities_gold_population.keys():
        population = cities_gold_population[town]["population"]
        gold = cities_gold_population[town]["gold"]
        print(f"{town} -> Population: {population} citizens, Gold: {gold} kg")

