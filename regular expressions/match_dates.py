import re

dates = input()

pattern = r"\b(?P<Day>\d{2})(?P<sep>[-.\/])(?P<Month>[A-Z{1}][a-z][a-z])\2(?P<Year>\d{4})\b"

matches = re.findall(pattern,dates)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")