#single inheritance

class Parent:
    def display(self):
        print("Parent class")

class Child(Parent):
    pass

c = Child()
c.display()


#multiple inheritance
class X:
    def methodA(self):
        print("X")

class Y:
    def methodB(self):
        print("Y")

class Z(X, Y):
    pass

obj = Z()
obj.methodA()
obj.methodB()


#multi-level inheritance
class A:
    def methodA(self):
        print("A")          

class B(A):
    pass

class C(B):
    pass
