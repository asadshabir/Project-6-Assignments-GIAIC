# 9. Abstract Classes and Methods
# Assignment_09:

'''Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().'''

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, no implementation

# Concrete class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # Implement the abstract method
        return self.length * self.width

# Testing
rect = Rectangle(5, 3)  # Create a Rectangle object
print(f"Rectangle area: {rect.area()}")  # Output: Rectangle area: 15

# Optional: Try to instantiate Shape (will fail)
try:
    shape = Shape()  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
