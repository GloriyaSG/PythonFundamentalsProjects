n = int(input())
positive_num = []
negative_num = []
for _ in range(n):
    integer = int(input())

    if integer >= 0:
        positive_num.append(integer)
    else:
        negative_num.append(integer)

print(positive_num)
print(negative_num)
print(f"Count of positives: {len(positive_num)}")
print(f"Sum of negatives: {sum(negative_num)}")
