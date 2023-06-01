nums = input().split(", ")

positive = []
negative = []
even = []
odd = []

positive = ", ".join([x for x in nums if int(x) >= 0])
negative = ", ".join([x for x in nums if int(x) < 0])
even = ", ".join([x for x in nums if int(x) % 2 == 0])
odd = ", ".join([x for x in nums if int(x) % 2 != 0])

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
