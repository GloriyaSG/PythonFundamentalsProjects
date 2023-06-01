def bigger_than_average(avg, array):
    for num in array:
        if float(num) > avg:
            return True
    return False

numbers = [int(x)for x in input().split()]

numbers.sort(reverse=True)

average_num = sum(numbers) / len(numbers)
more_than_average = []
for x in numbers:
    if x > average_num:
        more_than_average.append(x)
        if len(more_than_average) == 5:
            break

if not bigger_than_average(average_num,numbers):
    print("No")
else:
    print(*more_than_average)