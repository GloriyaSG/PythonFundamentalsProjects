number = int(input())
even = []
odd = []
negative = []
positive = []

for n in range(number):
    integer = int(input())

    if integer >= 0:
        positive.append(integer)

        if integer % 2 == 0:
            even.append(integer)
        else:
            odd.append(integer)
    else:
        negative.append(integer)

        if integer % 2 == 0:
            even.append(integer)
        else:
            odd.append(integer)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
else:
    print(negative)
