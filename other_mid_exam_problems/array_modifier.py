list_of_int = [int(x) for x in input().split()]

while True:
    command = input()

    if command == "end":
        break

    if command == "decrease":
        list_of_int = list(map(lambda x: x - 1, list_of_int))
        continue

    action = command.split()[0]
    idx1 = int(command.split()[1])
    idx2 = int(command.split()[2])

    if action == "swap":
        temp = list_of_int[idx1]
        list_of_int[idx1] = list_of_int[idx2]
        list_of_int[idx2] = temp

    elif action == "multiply":
        list_of_int[idx1] = list_of_int[idx1] * list_of_int[idx2]

new = ', '.join(str(item) for item in list_of_int)
print(new)