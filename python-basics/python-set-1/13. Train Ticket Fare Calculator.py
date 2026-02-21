distance = int(input())
age = int(input())
price = 0
price += distance*2
if age>=60:
    price -= price*0.3
elif age < 12:
    price -= price*0.5
    
print(price)