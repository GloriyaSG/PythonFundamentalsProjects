# 100%

raw_key = input()

while True:
    line = input()
    if line == "Generate":
        break
    command = line.split(">>>")
    if command[0] == "Contains":
        substr = command[1]
        if substr in raw_key:
            print(f"{raw_key} contains {substr}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_idx = int(command[2])
        end_idx = int(command[3])
        if command[1] == "Upper":
            raw_key = raw_key[:start_idx] + raw_key[start_idx:end_idx].upper() + raw_key[end_idx:]
        else:
            raw_key = raw_key[:start_idx] + raw_key[start_idx:end_idx].lower() + raw_key[end_idx:]
        print(raw_key)
    elif command[0] == "Slice":
        start_idx = int(command[1])
        end_idx = int(command[2])
        raw_key = raw_key[:start_idx] + raw_key[end_idx:]
        print(raw_key)
print(f"Your activation key is: {raw_key}")