time = int(input("Enter time:"))
time = time%90

if time >1 and time <= 30:
    print("red")
elif time >30 and time <= 45:
    print("yellow")
if time >45 and time <= 90:
    print("green")
    