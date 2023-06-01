a = int(input())
b = int(input())

print(f"Before:")
print(f"a = {a}")
print(f"b = {b}")

temp = a
a = b
b = temp

print(f"After:")
print(f"a = {a}")
print(f"b = {b}")


