def even_numbers(nums):
    res = nums % 2 == 0
    return res

numbers = [int(x) for x in input().split()]

print(list(filter(even_numbers, numbers)))
