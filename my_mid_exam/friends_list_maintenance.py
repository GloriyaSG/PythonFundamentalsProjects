def is_valid_index(index, list):
    if 0 <= index < len(list):
        return True
    return False


friends = input().split(", ")
command = input()
blacklisted = 0
lost = 0
while True:
    if command == "Report":
        print(f"Blacklisted names: {blacklisted}")
        print(f"Lost names: {lost}")
        print(*friends, sep=" ")
        break
    else:
        command = command.split()
        if "Blacklist" in command:
            name = command[1]
            if name in friends:
                index = friends.index(name)
                friends[index] = "Blacklisted"
                blacklisted += 1
                print(f"{name} was blacklisted.")
            else:
                print(f"{name} was not found.")

        elif "Error" in command:
            index = int(command[1])
            if is_valid_index(index,friends):
                if friends[index] != "Lost" and friends[index] != "Blacklisted":
                    print(f"{friends[index]} was lost due to an error.")
                    friends[index] = "Lost"
                    lost += 1

        elif "Change" in command:
            index = int(command[1])
            new_name = command[2]
            if is_valid_index(index,friends):
                print(f"{friends[index]} changed his username to {new_name}.")
                friends[index] = new_name

    command = input()
