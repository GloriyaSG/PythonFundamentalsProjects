people = int(input())
lift = [int(num) for num in input().split(' ')]

for wagon in range(len(lift)):
    while lift[wagon] < 4 and people > 0:
        lift[wagon] += 1
        people -= 1

total_lift_size = len(lift) * 4
if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif total_lift_size > sum(lift):
    print("The lift has empty spots!")
print(*lift, sep=' ')
