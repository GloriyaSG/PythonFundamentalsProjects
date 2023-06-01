factor = int(input())
count = int(input())
my_list = []
for element in range(factor, factor * count + 1, +factor):
    my_list.append(element)

print(my_list)
