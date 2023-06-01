price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_items = input()
entry = price_ratings[entry_point]
left = price_ratings[:entry_point]
right = price_ratings[entry_point+1:]
left_side = 0
right_side = 0

if type_of_items == "cheap":
    for x in left:
        if x < entry:
            left_side += x

    for x in right:
        if x < entry:
            right_side += x

elif type_of_items == "expensive":
    for x in left:
        if x >= entry:
            left_side += x
    for x in right:
        if x >= entry:
            right_side += x

if left_side >= right_side:
    print(f"Left - {left_side}")
else:
    print(f"Right - {right_side}")

