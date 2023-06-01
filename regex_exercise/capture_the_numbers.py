import re

pattern = r'(\d+)'
matches = []
while True:
    text = input()
    if not text:
        break
    match = re.findall(pattern, text)
    if match:
        matches.append(" ".join(match))

print(" ".join(matches))


