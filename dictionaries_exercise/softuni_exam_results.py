exams = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break
    elif "banned" not in command:
        command = command.split("-")
        name = command[0]
        language = command[1]
        points = command[2]
        if name not in exams:
            exams[name] = []
        exams[name].append(points)
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1
    if "banned" in command:
        command = command.split("-")
        name = command[0]
        if name in exams:
            exams.pop(name)

print("Results:")
for person in exams:
    print(f"{person} | {max(exams[person])}")
print("Submissions:")
for lang in languages:
    print(f"{lang} - {languages[lang]}")
