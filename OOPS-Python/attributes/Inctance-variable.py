class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=student("sachin",34)
s2 =student("virat",31)
print(s1.name   ,end=",")
print(s1.age)
print(s2.name, end=",") 
print(s2.age)