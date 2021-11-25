import numpy as np

pi = 3.14
print("Module top level 1")


def circle_area(radius):
    """A cool function"""
    print("In function")
    return pi * radius ** 2


print("Module top level 2")

if __name__ == "__main__":
    print("In main script")
    print("Area of circle: {}".format(circle_area(10)))
