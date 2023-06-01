def chars(start, end):
    result = ""
    for nums in range(ord(start) + 1, ord(end)):
        result += f"{chr(nums)} "

    return result
input_start = input()
input_end = input()


print(chars(input_start,input_end))