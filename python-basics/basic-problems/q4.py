#Q4

user_input = input("Enter a number between 0-30: ")
if not user_input.isdigit():
    print("Please enter a valid number.")
elif int(user_input) < 0 or int(user_input) > 30:
    print("Please enter a number between 0 and 30.")
else:
    print(f"You entered: {user_input}")
    
power_value = 1
n = int(user_input)
for i in range(0, n+1):
    print(f"i:{i}, 2^i: {power_value}")
    power_value *= 2
    