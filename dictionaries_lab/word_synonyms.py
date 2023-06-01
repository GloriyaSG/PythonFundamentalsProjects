number_lines = int(input())
synonyms = {}

for words in range(number_lines):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []

    synonyms[word].append(synonym)

[print(f"{word} - {', '.join(synonyms[word])}") for word in synonyms]