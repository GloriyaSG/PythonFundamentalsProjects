command = input()
phonebook = {}

while "-" in command:
    command = command.split("-")
    person = command[0]
    number = command[1]

    phonebook[person] = number

    command = input()

count = int(command)

for search in range(count):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")

    else:
        print(f"Contact {name} does not exist.")