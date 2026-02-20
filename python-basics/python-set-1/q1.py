amount = int(input("Enter initial balance:"))
n = int(input("Enter number of amounts:"))
for i in range(n):
    w = int(input())
    if amount>=w and amount%100 == 0:
        amount -= w
        print("SUCESS")
    else:
        print("FAILED")
print(f"Final balance {amount}")