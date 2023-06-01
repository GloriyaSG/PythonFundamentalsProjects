number_of_snowballs = int(input())
best_result = 0
best_weight = 0
best_time = 0
best_quality = 0
for snowball in range(1, number_of_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > best_result:
        best_result = value
        best_weight = weight
        best_time = time
        best_quality = quality
print(f"{best_weight} : {best_time} = {int(best_result)} ({best_quality})")

