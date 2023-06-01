path = input().split("\\")

last_part = path[-1].split(".")

extension = last_part[-1]
name = last_part[:-1]

print(f"File name: {''.join(name)}")
print(f"File extension: {extension}")