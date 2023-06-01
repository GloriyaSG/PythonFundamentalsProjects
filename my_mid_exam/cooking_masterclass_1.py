import math
budget = float(input())
students = int(input())
flour_price = float(input())
eggs_price = float(input()) * 10
single_apron = float(input())
total_sum = 0
counter = 0
for person in range(1,students + 1):
    counter += 1
    if counter % 5 == 0:
        total_sum += eggs_price
    else:
        total_sum += flour_price + eggs_price

apron = math.ceil(students * 1.20) * single_apron
total_sum += apron


diff = abs(total_sum - budget)
if total_sum <= budget:
    print(f"Items purchased for {total_sum:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")