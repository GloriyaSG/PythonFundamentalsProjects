# 100%

text = input()

while True:
    line = input()
    if line == "Done":
        break
    command = line.split(" ")
    if command[0] == "TakeOdd":
        text = text[1::2]
        print(text)
    elif command[0] == "Cut":
        index = int(command[1])
        length = index + int(command[2])
        substr = text[index:length]
        text = text.replace(substr,"",1)
        print(text)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in text:
            text = text.replace(substring,substitute, -1)
            print(text)
        else:
            print("Nothing to replace!")

print(f"Your password is: {text}")
