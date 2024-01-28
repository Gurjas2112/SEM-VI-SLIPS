#Define a class Employee having members id, name, department, salary.
#Create a subclass called Manager with member bonus. Define methods
#accept and display in both the classes. Create n objects of the Manager class
#and display the details of the Manager having the maximum total salary (salary+bonus).

class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def accept(self):
        self.id = input("Enter id: ")
        self.name = input("Enter name: ")
        self.department = input("Enter department: ")
        self.salary = int(input("Enter salary: "))

    def display(self):
        print("Id:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Manager(Employee):
    def __init__(self, id, name, department, salary, bonus):
        super().__init__(id, name, department, salary)
        self.bonus = bonus

    def accept(self):
        super().accept()
        self.bonus = int(input("Enter bonus: "))

    def display(self):
        super().display()
        print("Bonus:", self.bonus)

    def total(self):
        return self.salary + self.bonus

n = int(input("Enter number of employees: "))
m = []

for i in range(n):
    m.append(Manager(0, "", "", 0, 0))
    m[i].accept()

print("Details of employees:")
for i in range(n):
    m[i].display()
    print("Total salary:", m[i].total())
    print()

max_salary = m[0].total()
for i in range(n):
    if m[i].total() > max_salary:
        max_salary = m[i].total()

print("Details of manager having maximum total salary:")
for i in range(n):
    if m[i].total() == max_salary:
        m[i].display()
        print("Total salary:", m[i].total())
        break
