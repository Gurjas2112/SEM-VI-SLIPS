#Write a Python class named Student with two attributes student_name,
#marks. Modify the attribute values of the said class and print the original and
#modified values of the said attributes.

class Student:
	def __init__(self, student_name, marks):
		self.student_name = student_name
		self.marks = marks

# Create an instance of the Student class
n=input('Enter the name of the Student:')
m=input('Enter the marks of the Student:')
student = Student(n, m)

# Print the original attribute values
print("Original Name:", student.student_name)
print("Original Marks:", student.marks)

# Modify the attribute values
student.student_name = input( 'Enter the name of the Student:')

student.marks = input('Enter the marks of the Student:')

# Print the modified attribute values
print("Modified Name:", student.student_name)
print("Modified Marks:", student.marks)

