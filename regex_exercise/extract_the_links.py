import re

pattern = r"(www\.[A-Za-z0-9\-]+\.[a-z]+[\.a-z]*)"

while True:
    command = input()
    if not command:
        break

    matches = re.findall(pattern,command)
    if matches:
        print(*matches)