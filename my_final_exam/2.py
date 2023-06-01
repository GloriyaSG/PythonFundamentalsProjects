# Employees
import re

count_of_persons = int(input())

for match in range(count_of_persons):
    person = input()
    pattern = r"^(([A-Z][a-z]{2,}){1} ([A-Z][a-z]{2,}){1})#+(([A-Z][a-z]+\&?){1,3})[0-9]{2}([A-Z][A-Za-z0-9]+) (Ltd.|JSC)"
    matches = re.findall(pattern,person)
    for matching in matches:
        name = matching[0]
        job = matching[3]
        workplace = matching[5] + " " + matching[6]
        if "&" in job:
            job = job.split("&")
            print(f"{name} is {' '.join(job)} at {workplace}")
        else:
            print(f"{name} is {job} at {workplace}")