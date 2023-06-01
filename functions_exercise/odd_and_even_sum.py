def odd_even_sum(nums:  str):
    odd = 0
    even = 0
    for idx in nums:
        idx = int(idx)
        if idx % 2 == 0:
            even += idx
        else:
            odd += idx
    return f"Odd sum = {odd}, Even sum = {even}"

number = input()

print(odd_even_sum(number))