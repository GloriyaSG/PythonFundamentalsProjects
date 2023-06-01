num_lines = int(input())
capacity = 255
total_litre = 0
for a in range(num_lines):
    litre = int(input())
    capacity -= litre
    total_litre += litre
    if capacity < 0:
        print("Insufficient capacity!")
        capacity += litre
        total_litre -= litre
        continue
print(total_litre)
