from itertools import groupby
new_sequence = []

sequence = [''.join(x) for _,x in groupby(input())]
for word in sequence:
    if len(word) > 1:
        new_sequence.append(word[0])
    else:
        new_sequence.append(word)
print("".join(new_sequence))