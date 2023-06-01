numbers = [int(x) for x in input().split(", ")]
max_num = max(numbers)
group_one = 10
group_nums = []
for group in range(1, max_num+1):
    group_nums = []

    if (group_one - 10) >= max_num:
        break
    for el in numbers:
        if (group_one - 10) < el <= group_one:
            group_nums.append(el)

    print(f"Group of {group_one}'s: {group_nums}")

    group_one += 10

