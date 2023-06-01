happiness = [int(x) for x in input().split()]
factor_happiness = int(input())
new_list = [(x * factor_happiness) for x in happiness]
average = sum(new_list) / len(new_list)
happy = [x for x in new_list if x >= average]
not_happy = [x for x in new_list if x >= average]

if len(happy) >= len(new_list) / 2:
    print(f"Score: {len(happy)}/{len(new_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy)}/{len(new_list)}. Employees are not happy!")
