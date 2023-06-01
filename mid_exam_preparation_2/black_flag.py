days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_gained = 0

for plunder in range(1, days_of_plunder + 1):
    total_gained += daily_plunder
    if plunder % 3 == 0:
        total_gained += daily_plunder / 2
    if plunder % 5 == 0:
        total_gained = total_gained * 0.70
if total_gained >= expected_plunder:
    print(f"Ahoy! {total_gained:.2f} plunder gained.")
else:
    percentage = (total_gained/expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")