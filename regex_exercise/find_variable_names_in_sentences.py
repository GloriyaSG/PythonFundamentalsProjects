import re

text = input()

pattern = r"\b\_([A-Za-z0-9]+)\b"

matches = re.findall(pattern,text)

print(*matches, sep=",")

