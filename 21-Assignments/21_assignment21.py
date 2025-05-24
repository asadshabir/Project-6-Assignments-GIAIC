'''21. Make a Custom Class Iterable
Assignment:
Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.'''
class Countdown:
    def __init__(self, start):
        self.start = start  # Store the starting number
        self.current = start  # Initialize current for iteration
    
    def __iter__(self):
        return self  # Return self as the iterator
    
    def __next__(self):
        if self.current < 0:  # Stop when current goes below 0
            raise StopIteration
        result = self.current  # Return current number
        self.current -= 1  # Decrement for next iteration
        return result

# Testing
countdown = Countdown(5)
for num in countdown:
    print(num)  # Output: 5, 4, 3, 2, 1, 0 (each on a new line)

# Additional test
print("\nAnother countdown Begins!:")
countdown2 = Countdown(3)
for num in countdown2:
    print(num)  # Output: 3, 2, 1, 0 (each on a new line)