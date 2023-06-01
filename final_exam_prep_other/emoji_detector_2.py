#100 %
import re
text = input()
pattern_1 = r"\d"
pattern_2 = r"(\*{2}|\:{2})([A-Z]{1}[a-z]{2,})(\1)"

match_1 = re.findall(pattern_1,text)
cool_threshold = 1
for match in match_1:
    cool_threshold *= int(match)

match_2 = re.findall(pattern_2,text)
cool_ones = []

for match in match_2:
    count = 0
    for x in match[1]:
        count += ord(x)
    if count > cool_threshold:
        match = "".join(match)
        cool_ones.append(match)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(match_2)} emojis found in the text. The cool ones are:")
[print(x)for x in cool_ones]