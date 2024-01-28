#Write a python script to define the class Person having members name,
#address. Create a subclass called Employee with member salary. Create 'n'
#objects of the Employee class and display all the details of the employees.

class Person(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Employee(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, address)
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Salary:", self.salary)

n = int(input("Enter the number of employees: "))

for i in range(n):
    name = input("Enter the name of the employee: ")
    address = input("Enter the address of the employee: ")
    salary = int(input("Enter the salary of the employee: "))
    e = Employee(name, address, salary)
    e.display()
    print()
