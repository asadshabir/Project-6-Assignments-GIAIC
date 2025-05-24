# 5. Static Variables and Static Methods
# Assignment_5:

'''Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.'''


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # Return the sum, not print it

# Testing the static method
result = MathUtils.add(10, 5)
print(f"Sum: {result}")  # Output: Sum: 15

# Additional test
print(f"Sum of 20 and 30: {MathUtils.add(20, 30)}")  # Output: Sum of 20 and 30: 50
