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