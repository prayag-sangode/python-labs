# Lab 3.13.2: Abstraction using Vehicles

from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

# Concrete class: Bike
class Bike(Vehicle):
    def start(self):
        print("Kick-starting the bike!")

# Concrete class: Car
class Car(Vehicle):
    def start(self):
        print("Turning on the car with the key...")

# Main code
vehicles = [Bike(), Car()]

for v in vehicles:
    v.start()
