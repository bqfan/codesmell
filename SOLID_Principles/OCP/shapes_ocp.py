# shapes_ocp.py
"""
Open/closed principle (OCP):
This principle states that software entities should be open for extension, but closed for modification.

class Shape violates the OCP principle because if we want to add a new type of shape,
we have to modify the source code of the Shape class, which can introduce bugs and 
make the code difficult to maintain.
"""
from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

if __name__ == '__main__':
    # rectangle
    width = 2
    height = 4
    rectangle = Shape("rectangle", width=width, height=height)
    print(f"The area of the rectangle with width {width} and height {height} is {rectangle.area()}")    # Output: The area of the rectangle with width 2 and height 4 is 8

    # circle
    radius = 4
    circle = Shape("circle", radius=radius)
    print(f"The area of the circle with radius {radius} is {circle.area()}")    # Output: The area of the circle with radius 4 is 50.26548245743669
