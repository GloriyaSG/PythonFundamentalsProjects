products = input().split()
searched = input().split()
bakery = {}

for x in range(0,len(products), 2):
    key = products[x]
    value = products[x + 1]
    bakery[key] = int(value)

for x in searched:
    if x in bakery:
            print(f"We have {bakery[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")
