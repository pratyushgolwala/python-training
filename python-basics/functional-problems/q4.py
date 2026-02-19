#Q4

from math import sqrt


print("If your quadratic equation is aX^2 + bX + c please enter the values of:")
a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

delta = b*b - (4*a*c)


root1 = (-b + sqrt(delta))/(2*a)
root2 = (-b - sqrt(delta))/(2*a)

print(f"roots of {a}X^2 + {b}X + {c} are: {root1},{root2}")

