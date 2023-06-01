# 100%

num_pieces = int(input())
piano_pieces = {}
for x in range(num_pieces):
    piece, composer, key = input().split("|")
    piano_pieces[piece] = {"composer":composer, "key":key}

while True:
    line = input()
    if line == "Stop":
        break
    command = line.split("|")
    piece = command[1]
    if command[0] == "Add":
        composer = command[2]
        key = command[3]
        if piece not in piano_pieces:
            piano_pieces[piece] = {"composer":composer, "key":key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command[0] == "Remove":
        if piece in piano_pieces:
            piano_pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        new_key = command[2]
        if piece in piano_pieces:
            piano_pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for x in piano_pieces:
    print(f"{x} -> Composer: {piano_pieces[x]['composer']}, Key: {piano_pieces[x]['key']}")