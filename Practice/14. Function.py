# Function = A block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
def happy_birthday(name):
    print(f"Happy Birthday {name}!")
    print("Wishing you a day filled with happiness and a year filled with joy.", end="\n\n")

happy_birthday("Alice")
happy_birthday("Bob")
print(happy_birthday("Charlie"))  # This will print None since the function does not return anything
print(happy_birthday, end='\n\n')             # This will print the function object location

# Function with return value
def add_numbers(num1, num2):
    return num1 + num2
result = add_numbers(5, 10)
print(f"The sum is: {result}", end='\n\n')

# Function with default parameter
def greet(name, message="Hello"):
    print(f"{message}, {name}!", end='\n\n')
greet("Charlie")
greet("Diana", "Good Morning")

# Function with variable number of arguments
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(f"Multiplication result: {multiply(2, 3, 4)}")
print(f"Multiplication result: {multiply(5, 6)}", end='\n\n')

# Lambda Function (Anonymous Function)
square = lambda x: x * x
print(f"Square of 5: {square(5)}")
print(f"Square of 10: {square(10)}", end='\n\n')

# Nested Function
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()
print(outer_function("hello"))
print(outer_function("world"), end='\n\n')

# Recursive Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 7: {factorial(7)}", end='\n\n')

# Function Annotations
def greet_user(name: str) -> str:
    return f"Hello, {name}!"
print(greet_user("Eve"))
print(greet_user("Frank"), end='\n\n')

# Higher-Order Function
# A function that takes another function as an argument or returns a function as a result.
def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x * 2, 10))
print(apply_function(lambda x: x + 5, 20), end='\n\n')

# keyword Arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.", end='\n\n')
describe_person(age=30, city="New York", name="Alice")
describe_person(name="Bob", city="Los Angeles", age=25)

# Docstrings
def multiply_numbers(a, b):
    """This function multiplies two numbers and returns the result."""
    return a * b        
print(multiply_numbers(4, 5))
print(multiply_numbers.__doc__)
print(multiply_numbers, end='\n\n')

# Variable Scope
x = 10  # Global variable
def modify_variable():
    global x
    x = 20  # Modifying the global variable
    print(f"Inside function, x = {x}")
modify_variable()
print(f"Outside function, x = {x}")

# kwrgs and args
# *args = allows a function to accept any number of positional arguments as a tuple.
# **kwargs = allows a function to accept any number of keyword arguments as a dictionary.
# positional arguments = arguments that need to be in a specific position when passed to a function.
# keyword arguments = arguments that are passed to a function by explicitly naming each parameter and its value
def func_with_args_kwargs(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs, end='\n\n')

func_with_args_kwargs(1, 2, 3, name="Alice", age=30)
func_with_args_kwargs('a', 'b', key1="value1", key2="value2")  

courses = ['Math', 'Science', 'History', 'CompSci']
info = {'name': 'John', 'age': 25}
func_with_args_kwargs(*courses, **info)
