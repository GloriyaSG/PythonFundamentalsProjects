country_names = input().split(", ")
capital_cities = input().split(", ")
zipped = zip(country_names, capital_cities)

[print(f"{x} -> {y}") for (x,y) in zipped]