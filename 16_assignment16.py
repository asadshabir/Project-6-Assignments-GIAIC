# 16. Function Decorators
# Assignment:
'''Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().'''


def log_function_call(func):
    def wrapper():
        print(f"The Function '{func.__name__}' is being called!")
        print("Check!")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print(f"Hello,World!")

say_hello()