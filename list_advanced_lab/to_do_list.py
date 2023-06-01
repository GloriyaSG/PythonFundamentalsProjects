numbering = 10 * [0]

while True:
    command = input()

    if command == "End":
        break
    x = command.split("-")
    position = int(x[0]) - 1
    numbering[position] = x[1]

resilt = [x for x in numbering if x != 0]
print(resilt)
