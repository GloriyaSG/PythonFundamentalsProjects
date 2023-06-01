number_of_lines = int(input())
opening_bracket = 0
closing_bracket = 0
bracket = ""
balanced = 0
for n in range(1, number_of_lines+1):
    string = input()
    if string == "(":
        opening_bracket += 1
        bracket += "("
    elif string == ")":
        closing_bracket += 1
        bracket += ")"
    if bracket == "((" or bracket == "))" or bracket == ")(" or bracket == "()":
        if bracket == "((" or bracket == "))" or bracket == ")(":
            print("UNBALANCED")
            break
        elif bracket == "()":
            balanced += 1
            bracket = ""
if balanced == opening_bracket and balanced == closing_bracket:
    print("BALANCED")
