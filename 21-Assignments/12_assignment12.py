# 12. Static Methods
# Assignment_12:
'''Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.'''
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

# Testing
result = TemperatureConverter.celsius_to_fahrenheit(33.8)
print(f"33.8°C = {result}°F")  # Output: 33.8°C = 92.84°F

# Additional test cases
print(f"0°C = {TemperatureConverter.celsius_to_fahrenheit(0)}°F")      # Output: 0°C = 32°F
print(f"100°C = {TemperatureConverter.celsius_to_fahrenheit(100)}°F")  # Output: 100°C = 212°F