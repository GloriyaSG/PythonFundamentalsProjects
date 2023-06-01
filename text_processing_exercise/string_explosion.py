sequence = input()
portions = sequence.split(">")

result = [portions[0]]
prev = 0
for portion in portions[1:]:
    power = int(portion[0])
    prev += power
    part = portion[prev:]
    prev = max(prev - len(portion), 0)
    result.append(part)

print(">".join(result))








