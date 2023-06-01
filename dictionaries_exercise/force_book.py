side_by_players = {}
players_by_side = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    else:
        if "|" in command:
            command = command.split(" | ")
            force_side = command[0]
            force_user = command[1]
            if force_side not in players_by_side:
                players_by_side[force_side] = []
            if force_user not in side_by_players:
                side_by_players[force_user] = force_side
                players_by_side[force_side].append(force_user)
        if " -> " in command:
            command = command.split(" -> ")
            force_user = command[0]
            force_side = command[1]

            if force_side not in players_by_side:
                players_by_side[force_side] = []
            players_by_side[force_side].append(force_user)
            if force_user in side_by_players:
                other_side = side_by_players[force_user]
                players_by_side[other_side].remove(force_user)
                side_by_players[force_user] = force_side
            else:
                side_by_players[force_user] = force_side
            print(f"{force_user} joins the {force_side} side!")

for side, members in players_by_side.items():
    if len(members) == 0:
        continue
    print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")



