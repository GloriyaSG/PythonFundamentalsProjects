number = int(input())
word = input()
my_list = []
my_word_list = []
for _ in range(number):
    string = input()
    my_list.append(string)

    if word in string:
        my_word_list.append(string)

print(my_list)
print(my_word_list)


