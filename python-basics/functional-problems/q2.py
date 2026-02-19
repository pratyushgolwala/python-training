
#Q2

N = int(input("Enter length of array: "))
arr = input("Enter the elements of the array: ").split(",")
result = []

if len(arr) != N:
    print("Please enter the correct number of elements.")
else:
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (int(arr[i]) + int(arr[j]) + int(arr[k])) == 0:
                    result.append((arr[i], arr[j], arr[k]))

for i in range(len(result)):
    for j in range(i+1, len(result)):
        if set(result[i]) == set(result[j]):
            result.pop(j)
            break

print(f"number of distinct triplets: {len(set(result))}")
print(f"distinct triplets: {set(result)}")    

