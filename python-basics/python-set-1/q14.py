numbers = input()

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        print("NO")
        break
else:
    print("YES")
