def perfect_number(number: int):
    new_list = []
    for divisor in range(1, number):
        if number % divisor == 0:
            new_list.append(divisor)
    if sum(new_list) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

integer = int(input())
print(perfect_number(integer))