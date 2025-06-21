# Lab 3.7: Method Overriding in Python

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (inherits from Animal)
class Cat(Animal):
    # Overriding the speak() method
    def speak(self):
        print(f"{self.name} says Meow!")

# Another child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Create objects
animal = Animal("Generic Animal")
cat = Cat("Whiskers")
dog = Dog("Bruno")

# Call speak() from each
animal.speak()
cat.speak()    # Overridden version
dog.speak()    # Overridden version
