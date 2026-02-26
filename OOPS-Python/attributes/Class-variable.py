class student:
    school = "ABC School"  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
        
s1 = student("sachin", 34)
s2 = student("virat", 31)   
print(s1.name, end=",")  # instance variable
print(s1.age)   # instance variable
print(s1.school)         # class variable