'''7. Access Modifiers: Public, Private, and Protected'''
# Assignment:
'''Create a class Employee with:
a public variable name,
a protected variable _salary, and
a private variable __ssn.
Try accessing all three variables from an object of the class and document what happens.'''

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn          # Private variable

# Create an Employee object
obj = Employee("ASAD", 10222, "123-45-6789")

# Try accessing all three variables and document the results
try:
    print("Accessing public variable 'name':")
    print(f"Result: {obj.name}")  # Should work
except Exception as e:
    print(f"Error accessing name: {e}")

try:
    print("\nAccessing protected variable '_salary':")
    print(f"Result: {obj._salary}")  # Should work
except Exception as e:
    print(f"Error accessing _salary: {e}")

try:
    print("\nAccessing private variable '__ssn':")
    print(f"Result: {obj.__ssn}")  # Should raise AttributeError
except Exception as e:
    print(f"Error accessing __ssn: {e}")

# Optional: Show how to access private variable using name mangling (for learning)
try:
    print("\nAccessing private variable '__ssn' using name mangling:")
    print(f"Result: {obj._Employee__ssn}")  # Should work, but not recommended
except Exception as e:
    print(f"Error accessing _Employee__ssn: {e}")