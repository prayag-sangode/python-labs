# Lab 3.4: Working with self and instance variables

class Student:
    def __init__(self, name, age):
        # self.name and self.age are instance variables
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Create two student objects
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Display initial info
student1.display_info()
student2.display_info()

# Call birthday method
student1.birthday()
student2.birthday()
