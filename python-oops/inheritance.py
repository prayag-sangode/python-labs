# Lab: Inheritance (Single) in Python

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks: Woof!")

# Create objects
generic_animal = Animal("Some Animal")
dog1 = Dog("Bruno")

# Call methods
generic_animal.speak()
dog1.speak()  # Inherited method
dog1.bark()   # Own method
