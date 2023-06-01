fire_cells = input().split("#")
water = int(input())
total_fire = 0
print("Cells:")
for part in fire_cells:
    fire_cells = part.split(" = ")
    number = int(fire_cells[-1])
    if water < number:
        continue
    if "High" in fire_cells:
        if 81 <= number <= 125:
            print(f" - {number}")
            total_fire += number
            water -= number
    elif "Medium" in fire_cells:
        if 51 <= number <= 80:
            print(f" - {number}")
            total_fire += number
            water -= number
    elif "Low" in fire_cells:
        if 1 <= number <= 50:
            print(f" - {number}")
            total_fire += number
            water -= number
effort = total_fire * 0.25
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")






