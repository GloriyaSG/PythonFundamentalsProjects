string = str.lower(input())
counter = 0

list = ["sand", "water", "fish", "sun"]
for n in list:
    counter += string.count(n)
print(counter)