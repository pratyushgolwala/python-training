import math
a = int(input())
b = int(input())
count = 0


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0:
            return False
    return True
        
        
for i in range(a, b+1):
    if is_prime(i) == True:
        count += 1
print(count)
        