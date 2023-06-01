number = int(input())
for a in range(1, number + 1):
    for b in range(0, a):
        print("*", end="")
    print()
for c in range(number-1, -1, -1):
    for d in range(c,0, -1):
        print("*", end="")
    print()