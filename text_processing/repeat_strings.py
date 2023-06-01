text = input().split()
result = ""
for txt in text:
    result += txt * len(txt)

print(result)