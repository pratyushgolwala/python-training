n = int(input())
seats = 40
while n > 0:
    req = int(input())
    seats -= req
    if seats>=0:
        print("CONFIRMED")
    else:
        print("WAITLISTED")
    n -=1