from abc import ABC, abstractmethod
class shape(ABC):              # abstract base class
    @abstractmethod             #This means:
    def area(self):         # Any class inheriting Shape, must implement the area method.                      
        pass                   # Otherwise error
    def volume(self):         # Any class inheriting Shape, must implement the area method.                      
        pass                   # Otherwise error
    
class circle(shape):        #inheriting the abstract class
    
    def __init__(self, radius):
        self.radius = radius 
    def area(self):
        return 3.14 * self.radius ** 2
    def volume(self):
        return (4/3) * 3.14 * self.radius ** 3

c1 = circle(5)
print(c1.area())
print(c1.volume())
    