number_lines = int(input())
registered_names = {}
for passing in range(number_lines):
    command = input().split()

    if "register" in command:
        user = command[1]
        license_num = command[2]
        if user in registered_names:
            print(f"ERROR: already registered with plate number {registered_names[user]}")
        else:
            registered_names[user] = license_num
            print(f"{user} registered {registered_names[user]} successfully")
    elif "unregister" in command:
        user = command[1]
        if user not in registered_names:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            registered_names.pop(user)

[print(f"{x} => {registered_names[x]}")for x in registered_names]