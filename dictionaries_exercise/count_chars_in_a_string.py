word = input().split()
new_word = ''.join(word)

dicty = {}

for char in new_word:
    if char not in dicty:
        dicty[char] = 1
    else:
        dicty[char] += 1

[print(f"{char} -> {dicty[char]}")for char in dicty]