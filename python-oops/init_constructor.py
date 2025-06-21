# Lab: Using __init__() Constructor in Python

# Define a class with a constructor
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Create objects with data
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "City")

# Print object attributes
print("Car 1:", car1.brand, car1.model)
print("Car 2:", car2.brand, car2.model)
