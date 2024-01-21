# shapes_ocp_refactored.py
"""
Open/closed principle (OCP):
This principle states that software entities should be open for extension, but closed for modification.

To comply with the OCP principle, we can modify the Shape class to use a strategy pattern.
We can create an abstract Shape class and have specific Shape classes extend it.
The Shape class can then accept a shape of the Shape class, which will be used to calculate the area.
"""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def area(self):
        return self.side**2

if __name__ == '__main__':
    # rectangle
    width = 2
    height = 4
    rectangle = Rectangle(width, height)
    print(f"The area of the rectangle with width {width} and height {height} is {rectangle.area()}")    # Output: The area of the rectangle with width 2 and height 4 is 8

    # circle
    radius = 4
    circle = Circle(4)
    print(f"The area of the circle with radius {radius} is {circle.area()}")    # Output: The area of the circle with radius 4 is 50.26548245743669
