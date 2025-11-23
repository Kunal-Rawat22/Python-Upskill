# Understanding the basics of input and output
print("\n-------- Understanding Input and Output in Python --------")
number = input("Enter a number: ")
print("Type of input:", type(number))  # Input is always a string


# By default, the output that print() produces separates objects by a single space and appends a newline to the end of the output
first_name = "John"
last_name = "Doe"
print("Name:", first_name, last_name)

# Printing arrays
numbers = [1, 2, 3]
print('Printing array:', numbers)

age = 42
print('Printing int:', age)

# Printing dictionaries
name = {"first": "John", "last": "Doe"}
print('Printing dict:', name)

# Printing the len() function
print('Printing len() function:', len)

# Separators and End Characters
print("in", "Python", "programming", sep="-")  # Custom separator
print("Hello", end="!!!\n")  # Custom end character
print("World")

#flush and file parameters of print() function
import sys
print("This is printed to standard output.", file=sys.stdout)
print("This is printed to standard error.", file=sys.stderr)    
print("This is printed immediately.", flush=True)

