# Polymorphism Example: Same method name, different logic

import math

class Shape:
    def area(self):
        print("Cannot calculate area of unknown shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Function that works on any shape
def print_area(shape):
    print(f"Area: {shape.area():.2f}")

# Create shape objects
circle = Circle(5)
rectangle = Rectangle(10, 4)
square = Square(3)

# Call same method on different shapes
print_area(circle)
print_area(rectangle)
print_area(square)
