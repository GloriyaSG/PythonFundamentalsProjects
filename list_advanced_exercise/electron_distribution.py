number_of_electron = int(input()) #77
list_of_shells = [] #60
# 2,8,18, 32, 50
for shells in range(1, number_of_electron + 1):
    electron = 2 * (shells**2)
    diff = number_of_electron - sum(list_of_shells)
    if electron > diff:
        list_of_shells.append(diff)
    else:
        list_of_shells.append(electron)
    if sum(list_of_shells) == number_of_electron:
        break

print(list_of_shells)



