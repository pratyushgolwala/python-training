p = int(input("Enter P:"))
y = int(input("Enter Y:"))
r = int(input("Enter R:"))

def payment(p,y,r):
    n = 12 * y
    R = r / (12 * 100)
    denominator = 1 - (1 + R)**(-n)
    payment = (p * R) / denominator
    return payment

print(payment(p,y,r))