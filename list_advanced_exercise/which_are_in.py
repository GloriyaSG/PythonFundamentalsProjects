input_line_1 = input().split(", ")
input_line_2 = input().split(", ")
new_list = []

for x in input_line_1:
    for y in input_line_2:
        if x in y:
            new_list.append(x)
            break
print(new_list)