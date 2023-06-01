number = int(input())

total_free_chairs = 0
count_rooms = 0
count_available_rooms = 0

for line in range(1, number + 1):
    count_rooms += 1
    room_chairs = input().split(" ")
    room_capacity = len(room_chairs[0])
    visitors = int(room_chairs[1])

    counter = room_capacity - visitors
    if counter >= 0:
        total_free_chairs += counter
        count_available_rooms += 1

    else:
        print(f"{abs(counter)} more chairs needed in room {count_rooms}")

if count_available_rooms == number:
    print(f"Game On, {total_free_chairs} free chairs left")