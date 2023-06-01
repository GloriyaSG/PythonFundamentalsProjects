year = int(input())
year_as_string = str(year)
while True:
    next_year = year + 1
    next_year_str = str(next_year)
    set_of_next = set(next_year_str)
    if len(set_of_next) != len(next_year_str):
        year = next_year
    else:
        print(next_year)
        break
