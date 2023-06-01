encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break
    line = command.split("|")
    if line[0] == "Move":
        num_letters = int(line[1])
        encrypted_message = encrypted_message[num_letters:] + encrypted_message[:num_letters]

    elif line[0] == "Insert":
        index = int(line[1])
        value = line[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    else:
        substr = line[1]
        replacement = line[2]
        encrypted_message = encrypted_message.replace(substr,replacement)

print(f"The decrypted message is: {encrypted_message}")
