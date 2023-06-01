while True:
    string = input()
    if string == "End":
        break
    if string == "SoftUni":
        continue
    for ch in string:
        print(ch * 2, end="")
    print()
