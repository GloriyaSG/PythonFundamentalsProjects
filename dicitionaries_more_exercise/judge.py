user_cont_points = {}
user_tot_points = {}

while True:
    command = input()
    if command == "no more time":
        break
    else:
        command = command.split(" -> ")
        username = command[0]
        contest = command[1]
        points = int(command[2])
        if contest not in user_cont_points:
            user_cont_points[contest] = {username: points}
            if username not in user_tot_points:
                user_tot_points[username] = points
            else:
                user_tot_points[username] += points
        elif contest in user_cont_points:
            if username not in user_cont_points[contest]:
                user_cont_points[contest][username] = points
                user_tot_points[username] = points

            else:
                if user_cont_points[contest][username] < points:
                    user_cont_points[contest][username] = points
                    user_tot_points[username] += points

for key in user_cont_points.keys():
    print(f"{key}: {len(user_cont_points[key])} participants")
    sorted_list = sorted(user_cont_points[key].items(), key=lambda x: (-x[1], x[0]))
    for n in range(1, len(sorted_list) + 1):
        print(f"{n}. {sorted_list[n - 1][0]} <::> {sorted_list[n - 1][1]}")

print("Individual standings:")

sorted_list = sorted(user_tot_points.items(), key=lambda x: (-x[1], x[0]))
for n in range(1,len(sorted_list) + 1):
    print(f"{n}. {sorted_list[n-1][0]} -> {sorted_list[n-1][1]}")