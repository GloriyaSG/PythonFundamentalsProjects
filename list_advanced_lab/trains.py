number_of_wagons = int(input())
train = number_of_wagons * [0]
while True:
    command = input()

    if command == "End":
        break

    if "add" in command:
        persons = int(command.split()[1])
        train[-1] += persons
    elif "insert" in command:
        wagon = int(command.split()[1])
        persons = int(command.split()[2])
        train[wagon] += persons
    elif "leave" in command:
        wagon = int(command.split()[1])
        persons = int(command.split()[2])
        train[wagon] -= persons


print(train)
