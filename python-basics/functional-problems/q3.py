#Q3

from math import sqrt


X = int(input("Enter value for X:"))
Y = int(input("Enter value for Y:"))

distance = sqrt(X*X + Y*Y)

print(f"Eucledian distance between {X,Y} and (0,0) is {distance}")
