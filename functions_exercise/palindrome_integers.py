def palindrome(some_list):
    for num in my_list:
        num = str(num)
        reversed_num = list(reversed(num))
        reversed_num = "".join(reversed_num)
        if num == reversed_num:
            print(True)
        else:
            print(False)

my_list = [int(x) for x in input().split(", ")]

palindrome(my_list)


