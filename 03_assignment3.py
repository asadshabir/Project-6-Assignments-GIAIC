# 3. Public Variables and Methods
# Assignment_3:
'''Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.'''

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public instance variable

    def start(self):  # Public method
        print(f"The car {self.brand} has started....")

# Instantiate the class
brand1 = Car("CIVIC")  # Pass the brand when creating the object
brand2 = Car("TOYOTA")  # Pass the brand when creating the object
brand1.start()  # Call the method on the instance
brand2.start()  # Call the method on the instance
print(brand1.brand)