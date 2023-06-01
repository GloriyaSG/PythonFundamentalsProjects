text = input()
emoticon = ":"

for char in range(len(text)):
    sym = text[char]
    if sym == ":":
        emoticon += text[char + 1]
        print(emoticon)
        emoticon = ":"
