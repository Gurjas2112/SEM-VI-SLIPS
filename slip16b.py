#Define a class named Shape and its subclass Square. The subclass
#has an init function which takes an argument Length. Both classes
#should have methods to calculate area and perimeter of a given shape.

class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length

t = int(input("Enter a length: "))
s = Square(t)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())
