gifts = input().split()

while True:
    command = input()
    if command in "No Money":
        break
    split = command.split()
    command = split[0]
    gift = split[1]

    if "OutOfStock" in command:
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"
    elif "Required" in command:
        gift_idx = int(split[2])
        if gift_idx in range(len(gifts)):
            gifts[gift_idx] = gift
    elif "JustInCase" in command:
        gifts[-1] = gift

for none in gifts:
    if "None" in gifts:
        gifts.remove("None")

print(" ".join(gifts))
print(*gifts)