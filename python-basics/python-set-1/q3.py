password = input("Enter password:")
digit_count = 0

lst = password.split()
contains_upper = any(c.isupper() for c in password)
is_digit = any(char.isdigit() for char in password)
length = len(password)

if contains_upper == True and is_digit == True and length>=8:
    print("STRONG")
else:
    print("WEAK")

