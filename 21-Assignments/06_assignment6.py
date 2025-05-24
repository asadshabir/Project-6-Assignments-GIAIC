# 6. Constructors and Destructors
# Assignment_6:
'''Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).'''



class Logger:
    def __init__(self):
        print("Object created")  # Message when object is created

    def __del__(self):
        print("Object destroyed")  # Message when object is destroyed

# Testing the class
print("Creating first object:")
obj1 = Logger()  # Triggers __init__, prints "Object created"

print("\nCreating second object:")
obj2 = Logger()  # Triggers __init__, prints "Object created"

print("\nDeleting first object:")
del obj1  # Triggers __del__, prints "Object destroyed"

print("\nEnd of program")
# obj2 will be destroyed automatically when the program ends


