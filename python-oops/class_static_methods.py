# Lab 3.12: Classmethods vs Staticmethods

class Student:
    school_name = "Greenwood High"  # Class variable

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} is in grade {self.grade} at {Student.school_name}")

    # Class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static method
    @staticmethod
    def is_passed(score):
        return score >= 35

# Normal object usage
s1 = Student("Asha", "10th")
s1.display()

# Call class method to change shared class variable
Student.change_school("Sunrise Public School")
s1.display()

# Call static method (does not depend on object or class variables)
print("Marks: 45 - Passed?", Student.is_passed(45))
print("Marks: 30 - Passed?", Student.is_passed(30))
