strings = input().split()
new_list = []

while True:
    command = input().split()
    if command[0] == "3:1":
        break

    if command[0] == "merge":

        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1
        for merge in range(start_index + 1,end_index + 1):
            strings[merge] = ''
            strings[start_index] += strings[merge]


    elif command[0] == "divide":
        indexing = int(command[1])
        portions = int(command[2])
        element = strings[indexing]
        portion = len(element) // portions
        elements = ""
        strings.pop(indexing)

        for parts in element:
            elements += parts
            if len(elements) == portion:
                new_list.append(f"{elements}")
                elements = ""
            element = list(element)
            element.remove(parts)

            if len(element) + 1 < portion and len(element) != 0:
                last_part = new_list[-1]
                last_part += parts
                new_list.pop(-1)
                new_list.append(last_part)

strings.extend(new_list)
print(" ".join([x for x in strings if len(x) > 0]))










