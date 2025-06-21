# Lab 3.8: Using super() to call parent class methods

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a generic animal sound.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # Call parent method first
        super().speak()
        print(f"{self.name} the {self.breed} barks: Woof!")

# Create object
dog = Dog("Bruno", "Labrador")

# Call method
dog.speak()
