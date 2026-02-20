d = int(input("enter the day:"))
m = int(input("enter the month:"))
y = int(input("enter the year:"))

def calculate(d,m,y):
    y1 = y - (14-m) // 12
    x = y1 + y1//4 -y1//100 + y1//400
    m1 = m + 12 *((14-m) //12) -2
    d1 = (d + x + 31 * (m1//12)) % 7 
    return (d1)

print(calculate(d,m,y))
    
    