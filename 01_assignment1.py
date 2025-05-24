# Assignment_1:
'''Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.'''



class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}\n\t Student Marks: {self.marks}")

data = Student("Asad Shabir",97)
data.display()