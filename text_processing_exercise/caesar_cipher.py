string = input()
new = ""

for char in string:
    new_char = chr(ord(char) + 3)
    new += new_char

print(new)
