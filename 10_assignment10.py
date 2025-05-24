# 10. Instance Methods
# Assignment_10:
'''Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name'''

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says woof!")  # Simple message with name

# Testing
dog1 = Dog("Poppy", "Golden Retriever")
dog1.bark()  # Output: Poppy says woof!

dog2 = Dog("Max", "Labrador")
dog2.bark()  # Output: Max says woof!
