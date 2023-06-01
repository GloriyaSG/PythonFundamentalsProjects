import re

text = input()
pattern = r"\s([A-Za-z0-9][\w\-.]*[A-Za-z0-9]@[A-Za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])+)"

match_user = re.findall(pattern,text)
for x,y in match_user:
    print(''.join(x))