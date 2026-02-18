#Q1

name = input("Enter your name: ")
print(f"Hello, {name}!")


#Q2

import random
n = int(input("Enter a number: "))
heads = 0
tails = 0

for i in range(n):
    if random.random() < 0.5:
        tails += 1
    else:
        heads += 1

print(f"Heads percentage: {heads/n*100}%, Tails percentage: {tails/n*100}%")


#Q3

year = int(input("Enter a year: "))
if len(str(year)) != 4:
    print("Please enter a valid 4-digit year.")
    
elif(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
    
else:
    print(f"{year} is not a leap year.")
    
    

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
    
    

#Q5

num = int(input("Enter a number for harmonic sum: "))
result = 0
if num < 0:
    print("not defined for negative numbers.")
if num == 1:
    print(f"result: {result}")
for i in range(1, num + 1):
    result += 1/i
print(f"result: {result}")


#Q6

num = int(input("Enter a number for prime factorial: "))
factors = []
divisor = 2
while num>1:
    while num % divisor == 0:
        factors.append(divisor)
        num //= divisor
    divisor += 1
    
print(set(factors))