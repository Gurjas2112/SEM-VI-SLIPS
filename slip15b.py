#Write a python program to create a class Circle and compute the Area and the circumferences of the circle.(use parameterized constructor).

class Circle(object):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius
radius=int(input("Enter the radius of the circle: "))
c=Circle(radius)
print("Area of the circle is: ",c.area())
print("Circumference of the circle is: ",c.circumference())
