animals = input()
list_reversed = animals.split(", ")
list_reversed.reverse()

for i, item in enumerate(list_reversed):
    if item == "wolf" and i == 0:
        print("Please go away and stop eating my sheep")
        break
    elif item == "wolf":
        print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
        break



