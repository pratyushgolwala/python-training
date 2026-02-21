pin = input()
attempts = 2
unlocking = input()
while attempts != 0:
    if unlocking == pin:
        print("ACCESS GRANTED")
        break
    else:
        attempts -= 1
    unlocking = input() 
if attempts == 0:
    print("LOCKED")