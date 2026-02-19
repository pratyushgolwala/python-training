import random


stake = int(input("Enter the stake amount: "))
goal = int(input("Enter the goal amount: "))
trial = int(input("Enter the number of trials: "))
wins = 0
loss = 0

for i in range(trial):
    cash = stake
    while cash > 0 and cash < goal:
        if random.random() >0.5:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins +=1
    else:
        loss +=1
        
print(f"wins: {wins}, loss: {loss}, win percentage: {wins/trial*100}%, loss percentage: {loss/trial*100}%")
        
        