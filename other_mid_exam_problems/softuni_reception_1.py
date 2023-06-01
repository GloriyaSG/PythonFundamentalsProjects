import math
# 90%
first_worker_per_hour = int(input())
second_worker_per_hour = int(input())
third_worker_per_hour = int(input())
students_count = int(input())

peoples_per_hour = first_worker_per_hour + second_worker_per_hour + third_worker_per_hour
hours = students_count / peoples_per_hour
if hours > 3:
    breaks = hours // 3
    total_time = math.ceil(hours + breaks)
else:
    total_time = math.ceil(hours)
print(f"Time needed: {total_time}h.")



