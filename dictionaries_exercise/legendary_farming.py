new_dict = {"shards": 0,"fragments": 0,"motes": 0}
junk = {}
boolean = False
while not boolean:
    command = input()
    materials = command.split()

    for x in range(0,len(materials),2):
        quantity = int(materials[x])
        material = materials[x+1].lower()

        if material in new_dict:
            new_dict[material] += quantity
            if new_dict[material] >= 250:
                new_dict[material] -= 250
                boolean = True
                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                else:
                    print("Dragonwrath obtained!")
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity

[print(f"{x}: {new_dict[x]}") for x in new_dict]
[print(f"{x}: {junk[x]}")for x in junk]


