word = input()
group = []
for idx in range(len(word)):
    if word[idx].isupper():
        group.append(idx)
print(group)

