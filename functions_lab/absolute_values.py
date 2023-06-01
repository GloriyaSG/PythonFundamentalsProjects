numbers = [float(x) for x in input().split()]
new_list = []

for part in numbers:
    new_list.append(abs(part))

print(new_list)