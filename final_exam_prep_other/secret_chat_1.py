# 100%
concealed_message = input()

while True:
    line = input()
    if line == "Reveal":
        break
    command = line.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
    elif command[0] == "Reverse":
        substr = command[1]
        if substr in concealed_message:
            concealed_message = concealed_message.replace(substr,"",1)
            substr = substr[::-1]
            concealed_message = concealed_message + substr
        else:
            print("error")
            continue
    else:
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring,replacement,-1)
    print(concealed_message)
print(f"You have a new text message: {concealed_message}")
