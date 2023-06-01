def loading_bar(number):
    if number == 100:
        print(f"100% Complete!")
    else:
        print(f"{number}% ", end="")
    print("[", end="")
    for digit in range(1,10+1):
        if number / 10 >= digit:
            print(f"%", end="")
        else:
            print(f".", end="")
    print("]")
    if number < 100:
        print("Still loading...")

number_input = int(input())
loading_bar(number_input)



