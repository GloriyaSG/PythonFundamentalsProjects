# easter

string = input()

while True:
    line = input()
    if line == "Easter":
        break
    command = line.split()
    if command[0] == "Replace":
        curr_char, new_char = command[1], command[2]
        string = string.replace(curr_char,new_char,-1)
        print(string)
    elif command[0] == "Remove":
        substr = command[1]
        if substr in string:
            string = string.replace(substr,"")
        print(string)
    elif command[0] == "Includes":
        sstring = command[1]
        if sstring in string:
            print(True)
        else:
            print(False)
    elif command[0] == "Change":
        lower_upper = command[1]
        if lower_upper == "Lower":
            string = string.lower()
        else:
            string = string.upper()
        print(string)
    else:
        start_idx = int(command[1])
        end_idx = int(command[2])
        reverse = string
        if 0 <= start_idx < len(string) and 0 < end_idx <= len(string):
            reverse = reverse[start_idx:end_idx+1]
            reverse = reverse[::-1]
            print(reverse)
        else:
            continue
