
#Write a python script to define a class student having members roll no, name,
#age, gender. Create a subclass called Test with member marks of 3 subjects.
#Create three objects of the Test class and display all the details of the student
#with total marks

class Student:
    def __init__(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

class Test(Student):
    def __init__(self, roll_no, name, age, gender, marks):
        super().__init__(roll_no, name, age, gender)
        self.marks = marks

    def display_details(self):
        total_marks = sum(self.marks)
        print("Student Details:")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Marks in Subjects:", self.marks)
        print("Total Marks:", total_marks)

# Creating objects of Test class and displaying details
students = [
    Test("S001", "Alice", 18, "Female", [85, 90, 92]),
    Test("S002", "Bob", 17, "Male", [78, 88, 95]),
    Test("S003", "Charlie", 19, "Male", [92, 80, 88])
]

for student in students:
    student.display_details()
    print()

