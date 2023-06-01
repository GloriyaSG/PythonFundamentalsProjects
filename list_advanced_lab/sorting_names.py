input_names = input().split(", ")
my_list = sorted(input_names, key=lambda x: (-len(x), x))
print(my_list)