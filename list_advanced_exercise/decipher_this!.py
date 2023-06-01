secret_message = input().split()
decoded_word = []
decoded_digits = ""

for decode in secret_message:
    for letters in decode:
        if letters.isdigit():
            decoded_digits += letters
        else:
            decoded_word.append(letters)
    decoded_word[0], decoded_word[-1] = decoded_word[-1], decoded_word[0]
    decoded_word.insert(0, chr(int(decoded_digits)))
    print("".join(decoded_word), end=" ")
    decoded_word = []
    decoded_digits = ""