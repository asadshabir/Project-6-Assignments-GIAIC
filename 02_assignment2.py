# 2. Using cls
# Assignment_2:
'''Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.'''

class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")  # Display the count

# Testing the class
c1 = Counter()  # Create first object
Counter.show_count()  # Should print: Total objects created: 1

c2 = Counter()  # Create second object
Counter.show_count()  # Should print: Total objects created: 2

c3 = Counter()  # Create third object
Counter.show_count()  # Should print: Total objects created: 3