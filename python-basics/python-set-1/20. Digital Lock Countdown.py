num = int(input())

while num >= 10:
    temp = num
    sum = 0
    
    while temp > 0:
        sum += temp%10
        temp //= 10
    
    num =sum

print(num)