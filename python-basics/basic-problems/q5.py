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
