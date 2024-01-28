#Write a python script to create a class Rectangle with data member’s length,
#width and methods area, perimeter which can compute the area and
#perimeter of rectangle.

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

r1 = Rectangle(length, width)
print("Area of the rectangle:", r1.area(),"sq. cm")
print("Perimeter of the rectangle:", r1.perimeter(), "cm")

