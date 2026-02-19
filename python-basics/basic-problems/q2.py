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
