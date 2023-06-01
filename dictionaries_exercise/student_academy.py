number = int(input())
new_dict = {}

for grades in range(number):
    name = input()
    grade = float(input())
    if name not in new_dict:
        new_dict[name] = []

    new_dict[name].append(grade)


for person in new_dict:
    average_grade = sum(new_dict[person]) / len(new_dict[person])
    if average_grade >= 4.50:
        print(f"{person} -> {average_grade:.2f}")