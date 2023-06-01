def is_index_valid(indexing, targets):
    if 0 <= indexing < len(targets):
        return True
    return False
targets_value = [int(x) for x in input().split()]
command = input()

while True:
    if command == "End":
        print("{target1}|{target2}…|{targetn}")
        exit(0)
    else:
        split = command.split(" ")
        command, index, manipulation = split[0], int(split[1]), int(split[2])
        if command == "Shoot":
            if is_index_valid(index,targets_value):
                targets_value[index] -= manipulation
                if targets_value[index] <= 0:
                    targets_value.pop(index)

        elif command == "Add":
            if is_index_valid(index,targets_value):
                targets_value[index] = manipulation
            else:
                print("Invalid placement!")
        elif command == "Strike":
            
            pass
        command = input()



