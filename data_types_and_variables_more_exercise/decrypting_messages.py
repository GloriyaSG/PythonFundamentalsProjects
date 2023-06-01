key = int(input())
number_of_lines = int(input())
decrypted_message = ""
decrypted_letter = ""
for n in range(1, number_of_lines+1):
    letter = input()
    number_of_letter = ord(letter) + key
    decrypted_letter = chr(number_of_letter)
    decrypted_message += decrypted_letter

print(decrypted_message)


