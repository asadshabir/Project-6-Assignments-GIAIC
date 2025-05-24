# 17. Class Decorators
# Assignment_17:
'''Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
'''
def add_greeting(cls):
    def greet(self):
        return f"Hello, Mr'{person.name} from Decorator!"
    setattr(cls, "greet", greet)  # Add greet method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Testing
person = Person("Asad")
print(person.greet())  # Output: Hello from Decorator!

# Additional test
another_person = Person("Zain")
print(another_person.greet())  # Output: Hello from Decorator!