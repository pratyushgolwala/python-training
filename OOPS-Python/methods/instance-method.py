class student:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello my name is {self.name}")
        
s1 = student("sachin")
s1.greet()  # calling the instance method using the object s1