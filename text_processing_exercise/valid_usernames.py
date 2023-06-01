from string import ascii_lowercase,digits

usernames = input().split(", ")
allowed_chars = ascii_lowercase + digits + "-" + "_"
valid_usernames = []

for user in usernames:
    not_valid = False
    if (len(user)) < 3 or len(user) > 16:
        continue
    for char in user:
        if char.lower() not in allowed_chars:
            not_valid = True
            break
    if not_valid:
        continue
    else:
        print(user)