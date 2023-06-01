def valid_password_checker(password):
    valid = 0
    digit = 0
    if 6 <= len(password) <= 10:
        valid += 1
    else:
        valid -= 1
        print("Password must be between 6 and 10 characters")
    if password.isalnum():
        valid += 1
    else:
        valid -= 1
        print("Password must consist only of letters and digits")
    for digits in password:
        if digits.isdigit():
            digit += 1
    if digit >= 2:
        valid += 1
    else:
        valid -= 1
        print("Password must have at least 2 digits")
    if valid == 3:
        print("Password is valid")
input_password = input()

valid_password_checker(input_password)