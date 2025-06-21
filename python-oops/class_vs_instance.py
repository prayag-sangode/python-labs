# Lab: Class vs Instance Variables

class Student:
    # Class variable (shared by all students)
    school_name = "Greenwood High"

    def __init__(self, name, grade):
        # Instance variables (unique to each student)
        self.name = name
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")

# Create student objects
student1 = Student("Alice", "10th")
student2 = Student("Bob", "12th")

# Display info
student1.display()
student2.display()

# Update instance variable
student1.grade = "11th"
# Update class variable
Student.school_name = "Sunrise Public School"

# Display again to see the difference
student1.display()
student2.display()
