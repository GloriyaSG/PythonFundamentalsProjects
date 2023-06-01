team_A = 11
team_B = 11

red_card_players = []
cards = input().split()
terminated_game = False

for el in cards:
    if el in red_card_players:
        continue

    if el[0] == "A":
        red_card_players.append(el)
        team_A -= 1
    else:
        red_card_players.append(el)
        team_B -= 1

    if team_A < 7 or team_B < 7:
        terminated_game = True
        break

if terminated_game:
    print(f"Team A - {team_A}; Team B - {team_B}")
    print("Game was terminated")
else:
    print(f"Team A - {team_A}; Team B - {team_B}")








