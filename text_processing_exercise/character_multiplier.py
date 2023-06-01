text = input().split()
min_len = min(len(text[0]), len(text[1]))

result = 0
first_word = text[0]
second_word = text[1]

for multiply in range(min_len):
    result += ord(first_word[multiply]) * ord(second_word[multiply])

for index in range(min_len, len(first_word)):
    result += ord(first_word[index])

for index in range(min_len, len(second_word)):
    result += ord(second_word[index])

print(result)