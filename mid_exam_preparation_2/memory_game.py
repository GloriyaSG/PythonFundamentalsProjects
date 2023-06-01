def if_indexes_are_in_range(index, len_cards):
    if 0 <= index < len_cards:
        return True
    return False

sequence_elements = input().split()
command = input()

counter = 0
while command != "end":

    counter += 1
    index_one = int(command.split()[0])
    index_two = int(command.split()[1])
    if index_one == index_two:
        middle_index = len(sequence_elements) // 2
        element_add = f"-{counter}a"
        sequence_elements.insert(middle_index, element_add)
        print("Invalid input! Adding additional elements to the board")
    if not if_indexes_are_in_range(index_one, len(sequence_elements)) \
            or not if_indexes_are_in_range(index_two, len(sequence_elements)):
        middle_index = len(sequence_elements) // 2
        element_add = f"-{counter}a"
        sequence_elements.insert(middle_index, element_add)
        sequence_elements.insert(middle_index, element_add)
        print("Invalid input! Adding additional elements to the board")

    elif sequence_elements[index_one] == sequence_elements[index_two]:
        element_add = sequence_elements[index_two]
        sequence_elements.pop(index_one)
        sequence_elements.remove(element_add)
        print(f"Congrats! You have found matching elements - {element_add}!")
    else:
        print("Try again!")

    if len(sequence_elements) == 0:
        print(f"You have won in {counter} turns!")
        exit(0)
    command = input()

sequence_elements = " ".join(sequence_elements)
print(f"Sorry you lose :(")
print(f"{sequence_elements}")
