# Exception Handling
# Different types of blocks: try, except, else, finally, raise
print("Exception Handling Examples:")

# Example 1: Basic try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")    

# Example 2: Using else and finally
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
else:
    content = file.read()
    print("File content read successfully.")
finally:
    print("Execution of try-except block is complete.")
    
# Example 3: Raising an exception
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Your age is {age}.")
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as ve:
    print(f"Error: {ve}")

