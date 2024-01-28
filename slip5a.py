#Write an anonymous function to find area of square and rectangle.

# Anonymous function to calculate the area of a square
square_area = lambda side: side * side

# Anonymous function to calculate the area of a rectangle
rectangle_area = lambda length, width: length * width

# Example usage:
side_length = 5
rectangle_length = 6
rectangle_width = 4

print("Area of square:", square_area(side_length))
print("Area of rectangle:", rectangle_area(rectangle_length, rectangle_width))
