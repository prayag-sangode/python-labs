# Lab: Adding Methods to a Class in Python

# Define a class with methods
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display details
    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"{self.brand} {self.model} engine started.")

# Create objects
car1 = Car("Toyota", "Fortuner")
car2 = Car("Tesla", "Model 3")

# Call methods
car1.display_info()
car1.start_engine()

car2.display_info()
car2.start_engine()
