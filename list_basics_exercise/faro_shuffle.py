cards = input().split()
count_shuffles = int(input())

middle_value = len(cards) // 2

for i in range(count_shuffles):
    result = []

    for index in range(middle_value):
        first_card = cards[index]

        current_index_second_deck = index + middle_value
        second_card = cards[current_index_second_deck]

        result.append(first_card)
        result.append(second_card)

    cards = result
print(result)
