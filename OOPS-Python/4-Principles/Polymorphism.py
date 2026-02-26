class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):                # Same function name behaves differently.
        print("Bark")

d = Dog()
x = Animal()
x.sound()  
d.sound()

#operator overloading
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):           
        return self.x + other.x

p1 = Point(10)
p2 = Point(20)

print(p1 + p2)                  # __add__() is automatically called when we use +.
