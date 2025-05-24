# 8. The super() Function
# Assignment:


class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject

    def display(self):
        # Format subjects as a string if it's a list
        subjects = ", ".join(self.subject) if isinstance(self.subject, list) else self.subject
        print(f"Teacher '{self.name}' teaches: {subjects}")

# Testing the classes
person = Person("Zain Malik")  # Create a Person object
print(f"Person name: {person.name}")  # Show base class

teacher = Teacher("Asad Shabir", ["English", "Biology", "Chemistry", "Physics"])  # Create a Teacher object
teacher.display()  # Show inherited name and subject

# Alternative: If subject is a single value
teacher2 = Teacher("Sara Ahmed", "Mathematics")
teacher2.display()
