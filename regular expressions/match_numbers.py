import re

nums = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

match = re.finditer(pattern,nums)

for mat in match:
    print(mat.group(),end=" ")

