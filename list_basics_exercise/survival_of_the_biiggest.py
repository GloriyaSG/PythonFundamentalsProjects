import math

numbers = [int(x) for x in input().split()]
count_to_remove = int(input())
my_list = []

for _ in range(count_to_remove):
    remove_num = min(numbers)
    numbers.remove(remove_num)

print(", ".join([str(x) for x in numbers]))
