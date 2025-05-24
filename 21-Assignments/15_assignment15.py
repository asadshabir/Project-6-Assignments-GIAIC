'''15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.

Example:
  
            A
           / \
          B   C
           \ /
            D

'''

# ____________________________________________________
class A:
    def show(self):
        print("A: Data Available!")

class B(A):
    def show(self):
        print("B: Data Processed!")
 
class C(A):
    def show(self):
        print("C: Data Analyzed!")

class D(B, C):
    pass  # No need to override show() to observe MRO

# Testing MRO
print("MRO for class D:", [cls.__name__ for cls in D.__mro__])  # Show MRO
obj = D()  # Create D object
obj.show()  # Call show() to see which method is used
print([cls.__name__ for cls in D.__mro__])
print(D.__mro__) 