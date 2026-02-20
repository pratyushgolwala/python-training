inflow = list(map(int, input().split()))
capacity = 0
count = 0
while capacity < 1000:
    for i in inflow:
        capacity += i
        if capacity < 1000:
            count +=1
print(count)
        