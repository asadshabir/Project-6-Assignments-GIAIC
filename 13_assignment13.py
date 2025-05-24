# 13. Composition
# Assignment_13:

'''Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.'''


class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine object
    
    def start_car(self):
        self.engine.start()  # Access Engine's method via the engine object
        print("The car is running on the track!")

# Testing
engine = Engine()  # Create an Engine object
car = Car(engine)  # Pass Engine object to Car
car.start_car()  # Call Car's method, which uses Engine's method

# Additional test
another_engine = Engine()
another_car = Car(another_engine)
car.start_car()
