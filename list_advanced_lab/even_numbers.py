numbers = [int(x) for x in input().split(", ")]
even = [x for x in range(len(numbers)) if numbers[x] % 2 == 0]
print(even)
