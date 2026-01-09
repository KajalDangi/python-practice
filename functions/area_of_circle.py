import math

def area_of_circle(radius):
    """Returns the area of a circle for the given radius"""
    return math.pi * radius * radius

r = float(input("Enter the radius of the circle: "))
print(area_of_circle(r))

