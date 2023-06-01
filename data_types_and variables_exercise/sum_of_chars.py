numbers = int(input())
sum_chars = 0
for idx in range(numbers):
    symbol = input()
    sum_chars += ord(symbol)

print(f"The sum equals: {sum_chars}")
