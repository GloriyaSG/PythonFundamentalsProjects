sum_total = input().split(", ")
count_beggars = int(input())

beggars = [0] * count_beggars

for beggar in range(len(sum_total)):
    beggar_index = beggar % count_beggars
    beggars_money = int(sum_total[beggar])
    beggars[beggar_index] += beggars_money

print(beggars)