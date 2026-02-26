class student:
    school = "ABC School"  # class variable
    
    @classmethod
    def get_school(cls):
        print(f"The school name is {cls.school}")
        
student.get_school()  # calling the class method using the class name