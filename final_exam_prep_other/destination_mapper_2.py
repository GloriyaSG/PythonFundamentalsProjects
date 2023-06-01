# 100%

import re

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"

text = input()

matches = re.findall(pattern,text)

points = [len(y) for x,y in matches]

destination = [y for x,y in matches]

print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {sum(points)}")