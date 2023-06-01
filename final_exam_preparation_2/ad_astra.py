# 83%

import re

pattern = r"(\||#)(?P<name>[A-Za-z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{,10000})\1"

text = input()

KCAL_PER_DAY = 2000

compiled = re.compile(pattern)

tot_kcal = 0
for match in compiled.finditer(text):       
    tot_kcal += int(match.group("calories"))

kcal_days = tot_kcal // KCAL_PER_DAY
print(f"You have food to last you for: {kcal_days} days!")

for match in compiled.finditer(text):
    print(f"Item: {match.group('name')}, Best before: {match.group('date')}, Nutrition: {match.group('calories') }")
