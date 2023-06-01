my_dict = {}

while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split(" -> ")
        company = command[0]
        user = command[1]
        if company not in my_dict:
            my_dict[company] = []
        if user not in my_dict[company]:
            my_dict[company].append(user)

for x in my_dict:
    print(x)
    for y in my_dict[x]:
        print(f"-- {y}")
