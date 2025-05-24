# 14. Aggregation
# Assignment_14:
'''Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.'''



class Employee:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        return f"Employee: {self.name}"

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Aggregation: Store reference to Employee
    
    def show_employee(self):
        print(f"Department '{self.name}' has employee: {self.employee.introduce()}")

# Testing aggregation
# Create Employee objects independently
emp1 = Employee("Asad")
emp2 = Employee("Zain")

# Create Department, pass Employee object
dept = Department("Engineering", emp1)

# Show the relationship
dept.show_employee()

# Demonstrate Employee exists independently
print(f"Employee still exists: {emp1.introduce()}")

# Test with another Department and Employee
dept2 = Department("Marketing", emp2)
dept2.show_employee()

# Show Employee is unaffected if Department is deleted
del dept  # Delete the Department
print(f"After deleting Engineering dept, employee still exists: {emp1.introduce()}")

