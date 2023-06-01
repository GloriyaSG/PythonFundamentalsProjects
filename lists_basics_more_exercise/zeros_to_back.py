my_list = [int(x) for x in input().split(", ")]
printed_list = []
zeros = []
for i in my_list:
    if i == 0:
        zeros.append(i)
    else:
        printed_list.append(i)
for idx in zeros:
    printed_list.append(idx)

print(printed_list)

