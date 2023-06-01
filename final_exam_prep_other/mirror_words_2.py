# 100%
import re

text = input()

pattern = r"(#|@)(([A-Za-z]{3,})\1{2}([A-Za-z]{3,}))\1"

matches_full = re.findall(pattern,text)
mirror_words = []

if not matches_full:
    print("No word pairs found!")
else:
    for match in matches_full:
        if match[2] == match[3][::-1]:
            mirror_words.append(f"{match[2]} <=> {match[3]}")
    print(f"{len(matches_full)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(*mirror_words, sep=", ")