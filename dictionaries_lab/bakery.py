line = input().split()
bakery = {}

for x in range(0,len(line), 2):
    key = line[x]
    value = line[x+1]
    bakery[key] = int(value)

print(bakery)