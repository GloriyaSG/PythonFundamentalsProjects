coffee_needed = 0
while True:
    command = input()
    if command == "END":
        break
    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        coffee_needed += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        coffee_needed += 2
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
