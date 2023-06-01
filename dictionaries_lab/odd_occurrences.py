words = input().lower().split()
dicti = {}
for x in words:
    count = words.count(x)
    if count % 2 != 0:
        dicti[x] = count

print(' '.join(dicti.keys()))