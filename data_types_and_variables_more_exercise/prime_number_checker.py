number = int(input())
if number == 1:
    print(False)
elif number == 2:
    print(True)
elif number > 1:
    if number % number == 0:
        if number / 1 == number:
            if number % 2 == 0:
                print(False)
            elif number % 3 == 0:
                if number == 3:
                    print(True)
                else:
                    print(False)
else:
    print(False)