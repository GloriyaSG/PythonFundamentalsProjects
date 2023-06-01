initial_helath = 100
bitcoins = 0
dungeons_rooms = input().split("|")
rooms_count = 0
max_num = 0
for room in dungeons_rooms:
    room = room.split(" ")
    command, number = room[0], int(room[1])
    max_num = float("-inf")
    if number > max_num:
        max_num = number
        rooms_count += 1

    if command == "potion":
        diff = 100 - initial_helath
        initial_helath += number
        if initial_helath > 100:
            initial_helath = 100
            print(f"You healed for {diff} hp.")
        else:
            print(f"You healed for {number} hp.")
        print(f"Current health: {initial_helath} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        initial_helath -= number
        if initial_helath > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms_count}")
            break
if initial_helath > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_helath}")
