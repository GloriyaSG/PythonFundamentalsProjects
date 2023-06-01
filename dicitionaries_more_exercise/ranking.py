cont_pass_contest = {}
cont_user_points = {}
while True:
    command = input()
    if command == "end of contests":
        break
    else:
        command = command.split(":")
        contest = command[0]
        password = command[1]
        cont_pass_contest[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break
    else:
        command = command.split("=>")
        contest = command[0]
        password = command[1]
        name = command[2]
        points = int(command[3])
        if contest in cont_pass_contest:
            if cont_pass_contest[contest] == password:
                if contest not in cont_user_points:
                    cont_user_points[contest] = {name: points}
                else:
                    if name in cont_user_points[contest]:
                        if cont_user_points[contest][name] < points:
                            cont_user_points[contest][name] = points
                    else:
                        cont_user_points[contest][name] = points

ordered_ratings = {x: y for x, y in (sorted(cont_user_points.items()))}

for key, value in ordered_ratings.items():
    v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    ordered_ratings[key] = v

print(ordered_ratings)
print(cont_pass_contest)
print(cont_user_points)



