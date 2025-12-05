# Decorators in Python
# A decorator is a special type of function that modifies the behavior of another function.
# Decorators allow you to wrap another function to extend its behavior without modifying its code.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# wrapper() is used because without it, the decorator would execute where it is defined, not when the decorated function is called.
# You can also create decorators that accept arguments.

# Example of a decorator with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# In this example, the greet function will print the greeting three times because of the repeat decorator.
# Decorators are widely used in Python for logging, access control, instrumentation, and caching, among other things.
# You can also use built-in decorators like @staticmethod, @classmethod, and @property in classes.

# Multiple decorators can be applied to a single function as well.
def uppercase_decorator(func):
    def wrapper():
        print("Converting output to uppercase.")
        func()
    return wrapper

@my_decorator
@uppercase_decorator
def say_goodbye():
    print("Goodbye!")
say_goodbye()
# In this case, say_goodbye is first passed to uppercase_decorator, and then the result is passed to my_decorator.
# The order of decorators matters; they are applied from the bottom up.
# Note: Decorators can also be applied to functions with parameters by using *args and **kwargs in the wrapper function.

# Example of a decorator for functions with parameters
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@debug_decorator
def add(a, b):
    return a + b
print(add(5, 3))
# This debug_decorator will log the function name, its arguments, and the return value each time the add function is called.