programing_courses = {}

while True:
    command = input()

    if command == "end":
        break
    else:
        command = command.split(" : ")
        course = command[0]
        name = command[1]

        if course not in programing_courses:
            programing_courses[course] = []
        programing_courses[course].append(name)

for x in programing_courses:
    print(f"{x}: {len(programing_courses[x])}")
    for y in programing_courses[x]:
        print(''.join(f"-- {y}"))